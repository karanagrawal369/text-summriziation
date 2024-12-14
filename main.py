import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from textSummarizer.pipeline.Stage_01_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger

# Define the stage name
STAGE_NAME = "Data Ingestion stage"

if __name__ == "__main__":
    try:
        # Log the start of the stage
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        
        # Create and run the data ingestion pipeline
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        
        # Log the completion of the stage
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Log and raise any exceptions
        logger.exception(f"An error occurred during {STAGE_NAME}: {e}")
        raise
