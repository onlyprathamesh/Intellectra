#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import Intellectra
from dotenv import load_dotenv
load_dotenv()
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run(problem_statement=None):
    """
    Run the crew.
    Args:
        problem_statement (str): The problem statement to process. 
                               If None, uses default value.
    """
    if problem_statement is None:
        problem_statement = "Built an RAG platform for Q&A"
    
    inputs = {
        'problem_statement': problem_statement,
    }
    
    try:
        result = Intellectra().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

# This allows the script to be run directly or imported
if __name__ == "__main__":
    # Run with default parameters when called directly
    run()