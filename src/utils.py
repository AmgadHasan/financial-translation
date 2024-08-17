import argparse
import logging

import numpy as np
import os

def calculate_cosine_similarity(vector1, vector2):
    cos_sim = float(np.dot(vector1, vector2)/(np.linalg.norm(vector1)*np.linalg.norm(vector2)))
    return cos_sim

def get_logger(logger_name, log_file, log_level):
    # Set up logging
    LOG_FORMAT = '[%(asctime)s | %(name)s | %(levelname)s | %(message)s]'
    log_level = getattr(logging, log_level.upper())  # convert to uppercase

    # Create a logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)  # set the logger level to DEBUG

    # Add a console handler to log to the console with INFO level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(console_handler)

    return logger

# Parse CLI arguments
def parse_app_args():

    parser = argparse.ArgumentParser(description='Start the API server')
    parser.add_argument('--host', type=str, default='0.0.0.0',
                    help='Specify the host')
    parser.add_argument('--port', type=int, default=8000,
                    help='Specify the port')
    parser.add_argument('--reload', action='store_true', default=False,
                    help='Enable hot reloading for debugging')
    args = parser.parse_args()
    
    return args

def parse_eval_args():

    parser = argparse.ArgumentParser(description='Start the API server')
    parser.add_argument('--file', type=str,
                    help='Specify the csv file location')
    parser.add_argument('--language', type=str, default="Hungarian",
                    help='Specify the target language')
    parser.add_argument('--input-column', type=str, default="english",
                    help='Specify the input column')
    parser.add_argument('--label-column', type=str, default="translated_value",
                    help='Specify the label column')
    parser.add_argument('--openai-model', type=str, default=None,
                    help='Specify the label column')
    args = parser.parse_args()
    
    return args