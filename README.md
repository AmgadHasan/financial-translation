# brookerchooser-translation
A translation engine for the BrookerChooser website.
![](static/translation-app.png)

## Setup
### Dependencies
Install the dependcies:
```bash
# Create a virtual environment
# python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```
### Set up environment variables
Set up your environment variables in a file named `.env`
```bash
cp .example.env .env
```

### Running the webapp:
```bash
python3 src/main.py --host 0.0.0.0 --port 8080
```

Go to http://0.0.0.0:8080

## Docker
Alternatively, you can run using docker
### Build
```bash
docker build . -t brokerchooser-translation
```

### Create env file
```bash
cp .example.env .env
```

### Run container
```bash
docker run --env-file .env -p 8080:8080 brokerchooser-translation
```

Go to http://localhost:8080

## Evaluation
To evaluate a model on a labeled test set, the test set should be a csv file with a column containing the inputs and another column containing the labels (aka the ground-truth translation).

To run evaluation:
```bash
python src/eval.py --file path/to/test_set.csv --input-column name_of_input_column --label-column name_of_output_column --language target_language
```

### Docker
Run the following commands with the correct arguments for  `--volumne` `--input-column` `--label-column` `--language`
```bash
docker run --volume path/to/test_set.csv:/test.csv --env-file .env -p 8080:8080 brokerchooser-translation python3 src/eval.py --file /test.csv --input-column input-column-name --label-column label-column-name --language language
```

# Tracing
This project uses langfuse for LLM tracing. It traces inputs, model outputs, token usage, cost, latencies and more.
![](static/langfuse-llm-tracing.png)