"""
A script to load, download and cach the eval scripts
"""

import evaluate

ter = evaluate.load("ter")

sacrebleu = evaluate.load("sacrebleu")