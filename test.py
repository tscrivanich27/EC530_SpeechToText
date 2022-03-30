# test.py Dependencies
from app import speech_to_text
import logging

# Initialize the log file, example.log
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

# Unit Test #1: Single Valid Audio File 
def test_single_valid_audio():
    logging.info("Running Unit Test #1")
    try:
        # Have celery run the speech to text task
        speech_to_text.delay("Test #1.wav")
        # Use an assertion to check the result of speech_to_text function
        assert speech_to_text("Test #1.wav") == "Converting audio to text...\n" + "hello how are you doing today"
        # Print success message
        logging.info("Unit Test #1 Succeeded\nResults:\n" + speech_to_text("Test #1.wav"))
    # If the assertion returns false...
    except (AssertionError):
        # Print error message
        logging.error("Unit Test #1 Failed")

# Unit Test #2: Single Invalid Audio File 
def test_single_invalid_audio():
    logging.info("Running Unit Test #2")
    try:
        # Have celery run the speech to text task
        speech_to_text.delay("Test #2.wav")
        # Use an assertion to check the result of speech_to_text function
        assert speech_to_text("Test #2.wav") == "Sorry...please try again."
        # Print success message
        logging.info("Unit Test #2 Succeeded\nResults:\n" + speech_to_text("Test #2.wav"))
    # If the assertion returns false...
    except (AssertionError):
         # Print error message
        logging.error("Unit Test #2 Failed")

# Main Function
if __name__ == "__main__":
    test_single_valid_audio()
    test_single_invalid_audio()
    logging.info("Ran All Tests")