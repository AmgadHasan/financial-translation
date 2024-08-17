from utils import calculate_cosine_similarity, get_logger

from langfuse.decorators import langfuse_context, observe
from langfuse.openai import openai

logger = get_logger(logger_name="openai", log_file="openai.log", log_level="info")

@observe()
def translate(text: str, language: str, model: str="gpt-4o-mini", **kwargs):
    prediction = openai.chat.completions.create(
        model=model,
        max_tokens=512,
        messages=[
            {"role": "system", "content": "You are an expert at translating text into English. Text that is placed inside two square brackets [] is a placeholder text and should NOT be translated; leave it as it is.\nFor example, [broker] should be translated as [broker]."},
            {"role": "user", "content": f"Translate the following text from English to {language}:\n{text}"}
            ],
        **kwargs
    ).choices[0].message.content
    try:
        cosine_similarity = measure_similarity(text, prediction)
        logger.debug(f"Similarity:\t{cosine_similarity}")
        langfuse_context.score_current_observation(
            name="semantic_smiliarity_text-embedding-3-small",
            value=cosine_similarity,
            comment="I like how personalized the response is",
        )
    except Exception as e:
        logger.exception(e)
        
    return prediction

@observe()
def measure_similarity(inp: str, prediction: str):
    try:
        response = openai.embeddings.create(
            input=[inp, prediction],
            model="text-embedding-3-small"
        )
        embeddings = [x.embedding for x in response.data]
    except Exception as e:
        logger.exception(e)
    cosine_similarity = calculate_cosine_similarity(embeddings[0], embeddings[1])

    return cosine_similarity
