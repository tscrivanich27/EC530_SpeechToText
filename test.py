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

# Unit Test #3: Testing the queue system with four valid audio files 
def test_queue_system():
    logging.info("Running Unit Test #3")
    try:
        # Have celery run the speech to text task
        speech_to_text.delay("Test #3.wav")
        speech_to_text.delay("Test #4.wav")
        speech_to_text.delay("Test #5.wav")
        speech_to_text.delay("Test #6.wav")
        # Set text message to variable result
        result = speech_to_text("Test #3.wav") + " " + speech_to_text("Test #4.wav") +  " " + speech_to_text("Test #5.wav" ) + " " + speech_to_text("Test #6.wav")
        # Use an assertion to check the result of speech_to_text function
        assert result == "Converting audio to text...\nhello my name is Thomas Converting audio to text...\nthe temperature outside is 44 degrees Fahrenheit Converting audio to text...\nit is very sunny today it is a beautiful day Converting audio to text...\nI hope you are having a good day today"
        # Print success message
        logging.info("Unit Test #3 Succeeded\nResults:\n" + speech_to_text("Test #3.wav") + "\n" + speech_to_text("Test #4.wav") +
            "\n" + speech_to_text("Test #5.wav") + "\n" + speech_to_text("Test #6.wav"))
    # If the assertion returns false...
    except (AssertionError):
        # Print error message
        logging.error("Unit Test #3 Failed")

# Unit Test #4: Testing the queue system with three valid audio files and one invalid file
def test_queue_system_with_invalid():
    logging.info("Running Unit Test #4")
    try:
        # Have celery run the speech to text task
        speech_to_text.delay("Test #2.wav")
        speech_to_text.delay("Test #4.wav")
        speech_to_text.delay("Test #5.wav")
        speech_to_text.delay("Test #6.wav")
        # Set text message to variable result
        result = speech_to_text("Test #2.wav") + " " + speech_to_text("Test #4.wav") +  " " + speech_to_text("Test #5.wav" ) + " " + speech_to_text("Test #6.wav")
        # Use an assertion to check the result of speech_to_text function
        assert result == "Sorry...please try again. Converting audio to text...\nthe temperature outside is 44 degrees Fahrenheit Converting audio to text...\nit is very sunny today it is a beautiful day Converting audio to text...\nI hope you are having a good day today"
        # Print success message
        logging.info("Unit Test #4 Succeeded\nResults:\n" + speech_to_text("Test #2.wav") + "\n" + speech_to_text("Test #4.wav") +
            "\n" + speech_to_text("Test #5.wav") + "\n" + speech_to_text("Test #6.wav"))
     # If the assertion returns false...
    except (AssertionError):
        # Print error message
        logging.error("Unit Test #4 Failed")

# Main Function
if __name__ == "__main__":
    test_single_valid_audio()
    test_single_invalid_audio()
    test_queue_system()
    test_queue_system_with_invalid()
    logging.info("Ran All Tests")