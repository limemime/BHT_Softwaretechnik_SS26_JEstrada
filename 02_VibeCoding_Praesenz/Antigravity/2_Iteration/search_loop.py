import random
import webbrowser
import logging

def run_search_loop(config, word_selector, stop_event, on_search_callback=None):
    """Executes the background search loop.
    
    Args:
        config (EngineConfig): Configuration instance containing settings.
        word_selector (WordSelector): Selector instance to retrieve next search term.
        stop_event (threading.Event): Event to signal the loop to stop instantly.
        on_search_callback (callable, optional): Callback triggered after each search.
            Receives (word, engine_name) as arguments.
    """
    logging.info("Background search loop initiated.")
    
    while not stop_event.is_set():
        try:
            # 1. Fetch a random word
            word = word_selector.get_random_word()
            
            # 2. Build URL based on current configuration
            url = config.get_search_url(word)
            
            # 3. Log and execute the browser open
            logging.info(f"Opening browser search for: '{word}' using {config.search_engine}")
            webbrowser.open(url, new=0)
            
            # 4. Notify listener/GUI
            if on_search_callback:
                try:
                    on_search_callback(word, config.search_engine)
                except Exception as cb_err:
                    logging.error(f"Error executing search callback: {cb_err}")
            
            # 5. Compute sleep duration dynamically from current config
            sleep_time = random.uniform(config.min_sleep, config.max_sleep)
            logging.info(f"Sleeping for {sleep_time:.2f} seconds...")
            
            # 6. Thread-safe pause using event waiting.
            # If stop_event is set while waiting, this returns True immediately.
            is_stopped = stop_event.wait(sleep_time)
            if is_stopped:
                logging.info("Stop signal received during sleep.")
                break
                
        except Exception as e:
            logging.error(f"Unexpected error in search loop cycle: {e}")
            # If an error happens (e.g. word list is empty or browser issue),
            # wait briefly to prevent high-frequency loop spin before retrying.
            if stop_event.wait(3.0):
                break
                
    logging.info("Background search loop has terminated cleanly.")
