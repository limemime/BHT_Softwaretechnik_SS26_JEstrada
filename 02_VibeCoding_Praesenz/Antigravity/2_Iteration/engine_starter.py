import threading
import logging
from config import EngineConfig
from word_selector import WordSelector
from search_loop import run_search_loop

class EngineStarter:
    """Coordinates and controls the background thread and components of the Entropy Engine."""
    
    def __init__(self, config=None, word_selector=None):
        # Allow passing existing instances, or instantiate defaults
        self.config = config if config is not None else EngineConfig()
        
        # Instantiate word selector based on current config's dictionary path
        self.word_selector = (
            word_selector 
            if word_selector is not None 
            else WordSelector(self.config.dictionary_file)
        )
        
        self.running = False
        self.thread = None
        self.stop_event = threading.Event()
        self.on_search_callbacks = []

    def register_on_search_callback(self, callback):
        """Registers a callback function to be called after each search."""
        self.on_search_callbacks.append(callback)

    def _notify_search_listeners(self, word, engine_name):
        """Invokes all registered search callbacks with search information."""
        for callback in self.on_search_callbacks:
            try:
                callback(word, engine_name)
            except Exception as cb_err:
                logging.error(f"Failed to execute registered callback: {cb_err}")

    def start(self):
        """Launches the background search execution loop thread."""
        if self.running:
            logging.warning("Start requested but the search loop is already running.")
            return False
            
        # Verify and reload words if the dictionary was modified or empty
        self.word_selector.reload()
        if not self.word_selector.words:
            logging.error("Failed to start engine: word list is empty.")
            return False
            
        self.running = True
        self.stop_event.clear()
        
        # Instantiate and kick off background daemon thread
        self.thread = threading.Thread(
            target=run_search_loop,
            args=(
                self.config, 
                self.word_selector, 
                self.stop_event, 
                self._notify_search_listeners
            ),
            daemon=True
        )
        self.thread.start()
        logging.info("Engine starter successfully launched search thread.")
        return True

    def stop(self):
        """Issues an immediate stop signal to terminate the search loop."""
        if not self.running:
            return False
            
        self.running = False
        self.stop_event.set()
        logging.info("Engine starter issued stop signal to thread.")
        return True

    def force_single_search(self):
        """Triggers a single search immediately (outside the loop) on a separate thread."""
        def run_once():
            try:
                word = self.word_selector.get_random_word()
                url = self.config.get_search_url(word)
                logging.info(f"Forcing immediate search: '{word}' using {self.config.search_engine}")
                import webbrowser
                webbrowser.open(url, new=0)
                self._notify_search_listeners(word, self.config.search_engine)
            except Exception as e:
                logging.error(f"Error executing forced search: {e}")
                
        # Launch single search asynchronously to avoid freezing the GUI
        t = threading.Thread(target=run_once, daemon=True)
        t.start()
        return True
