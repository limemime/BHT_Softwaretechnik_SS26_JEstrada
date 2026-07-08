# We import the built-in threading module to allow our engine
# to run in the background without freezing the GUI window.
import threading

# We import the time module to handle the pacing delays
# between each arbitrary search request sent to the browser.
import time

# The random module provides unpredictability, allowing us to select
# random dictionary words and compute random sleep durations.
import random

# The webbrowser module allows us to securely ask the
# operating system to open URLs in the default browser.
import webbrowser

# We import the logging module to keep track of engine
# events and print them safely to the standard console.
import logging

# We import quote_plus from urllib.parse to securely format special
# characters and spaces inside our arbitrary dictionary words.
from urllib.parse import quote_plus

# We configure our standard logging format to display timestamps
# alongside all informational and error messages in the terminal.
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# This constant points to the local text file containing
# the 100 diverse, arbitrary words we will search for.
DICTIONARY_FILE = 'dictionary.txt'

# These constants set the default minimum and maximum sleep
# boundaries when the engine first boots up.
MIN_SLEEP_SECONDS = 7
MAX_SLEEP_SECONDS = 30

# This constant defines the standard Google search query URL
# structure, with a placeholder for the URL-encoded word.
SEARCH_URL_TEMPLATE = "https://www.google.com/search?q={}"

# We define the EntropyEngine class to encapsulate the search
# logic into a controllable, thread-safe object for the GUI.
class EntropyEngine:
    # The initialization method runs when the engine is created.
    # It takes the filepath and initial pace boundaries.
    def __init__(self, filepath, min_sleep, max_sleep):
        # We store the dictionary filepath as an instance variable.
        self.filepath = filepath
        # We store the current minimum sleep time in seconds.
        self.min_sleep = min_sleep
        # We store the current maximum sleep time in seconds.
        self.max_sleep = max_sleep
        
        # We initialize the running flag to False, indicating the
        # engine is currently stopped and waiting for user input.
        self.running = False
        # We declare a thread variable to hold the background
        # process later when the start button is pressed.
        self.thread = None
        
        # We call our internal method to load the words
        # from the file into memory upon instantiation.
        self.words = self._load_dictionary()

    # This internal method handles opening and reading the file.
    # It catches missing file errors and returns a list.
    def _load_dictionary(self):
        try:
            # We open the text file with utf-8 encoding safely.
            with open(self.filepath, 'r', encoding='utf-8') as f:
                # We strip whitespace and empty lines, creating a list.
                return [line.strip() for line in f if line.strip()]
        # If the file is missing, we catch the error.
        except FileNotFoundError:
            # We log a clear warning to the user terminal.
            logging.error(f"Dictionary file '{self.filepath}' not found.")
            # We return an empty list as a safe fallback.
            return []
        # We catch any other unexpected errors during file reading.
        except Exception as e:
            # We log the specific error to aid in debugging.
            logging.error(f"Error reading dictionary: {e}")
            # We return an empty list to prevent application crashes.
            return []

    # The start method is triggered by the GUI button.
    # It checks if we have words and starts the thread.
    def start(self):
        # We refuse to start if the engine is already running.
        if self.running:
            return
            
        # We refuse to start if the dictionary is completely empty.
        if not self.words:
            logging.error("No words loaded. Cannot start the engine.")
            return

        # We set the running flag to True to authorize loop.
        self.running = True
        # We create a new daemon thread targeting our main loop.
        # Daemon threads die automatically when the main program closes.
        self.thread = threading.Thread(target=self._run_loop, daemon=True)
        # We explicitly start the background thread execution.
        self.thread.start()
        # We log that the engine has successfully booted up.
        logging.info("Engine thread started.")

    # The stop method is triggered by the GUI button.
    # It safely signals the background thread to terminate.
    def stop(self):
        # We set the running flag to False to break loop.
        self.running = False
        # We log that a stop signal was successfully issued.
        logging.info("Engine stop signal issued. Waiting for current sleep cycle to end.")

    # This method allows the GUI to update the pacing variables
    # dynamically while the engine is actively running in background.
    def update_pace(self, new_min, new_max):
        # We update the instance variable for minimum sleep time.
        self.min_sleep = new_min
        # We update the instance variable for maximum sleep time.
        self.max_sleep = new_max
        # We log that the pace boundaries have been successfully changed.
        logging.info(f"Pace updated: Min {new_min}s, Max {new_max}s.")

    # This is the core private loop executed by the thread.
    # It continuously searches and sleeps while the flag is True.
    def _run_loop(self):
        # We enter a continuous loop reliant on the running flag.
        while self.running:
            # We select a completely random word from our list.
            word = random.choice(self.words)
            # We build the full URL by safely quoting the word.
            url = SEARCH_URL_TEMPLATE.format(quote_plus(word))
            
            # We log the specific word being searched right now.
            logging.info(f"Executing search for: '{word}'")
            # We use the open method with new=0 to politely
            # ask the OS to use the current browser tab.
            webbrowser.open(url, new=0)
            
            # We compute a random float between our current boundaries.
            sleep_time = random.uniform(self.min_sleep, self.max_sleep)
            # We log the upcoming sleep duration for user visibility.
            logging.info(f"Sleeping for {sleep_time:.2f} seconds...")
            
            # Instead of a single long sleep, we sleep in
            # short 1-second chunks. This allows the thread to stop
            # almost immediately if the user presses the stop button.
            elapsed = 0
            while elapsed < sleep_time and self.running:
                # We sleep for one second and increment the elapsed counter.
                time.sleep(1)
                elapsed += 1
                
        # When the loop breaks, we log that it has stopped.
        logging.info("Engine thread has fully stopped.")
