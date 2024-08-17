from utils import parse_eval_args, get_logger
from translation.openai import translate, measure_similarity

import pandas as pd
import evaluate

def main(args):
    sacrebleu = evaluate.load("sacrebleu")
    ter = evaluate.load("ter")
    df = pd.read_csv(args.file)
    inputs = df[args.input_column].tolist()
    labels = df[args.label_column].tolist()
    labels_list = [[lbl] for lbl in labels]

    preds = []
    logger.info(f"Running evals on {df.shape[0]} rows")
    if args.prediction_column:
        preds = df[args.prediction_column].tolist()
    else:
        for text in inputs:
            logger.debug(f"Input:\t{text}")
            try:
                pred = translate(text=text, language=args.language)
                logger.debug(f"Prediction:\t{pred}")
            except Exception as e:
                logger.exception(e)
                pred = ""
            
            preds.append(pred)
    
    sacrebleu_score = sacrebleu.compute(predictions=preds, references=labels_list)['score']
    ter_score = ter.compute(predictions=preds, references=labels)['score']
    cosine_similarities = [measure_similarity(pred, label) for pred, label in zip(preds, labels)]
    
    result = {"sacrebleu": sacrebleu_score, "ter": ter_score, "cosine_similarity": sum(cosine_similarities) / len(cosine_similarities)}
    logger.warning(f"Evaluation finished. Results:\t {result}")

    return result
    
if __name__ == "__main__":
    args = parse_eval_args()
    logger = get_logger(logger_name="eval", log_file="eval.log", log_level="DEBUG")
    main(args)