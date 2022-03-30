from app import speech_to_text
import logging

logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

# Unit Test #1: Single Valid Audio File 
def test_single_valid_audio():
    logging.info("Running Unit Test #1")
    try:
        speech_to_text.delay("Test #1.wav")
        assert speech_to_text("Test #1.wav") == "hello how are you doing today"
        logging.info("Unit Test #1 Succeeded")
    except (AssertionError):
        logging.error("Unit Test #1 Failed")
    
if __name__ == "__main__":
    test_single_valid_audio()
    logging.info("Ran All Tests")