import threading
import time
import random
import webbrowser
from config import config
from word_selector import word_selector

class SearchLoopManager:
    def __init__(self):
        self.is_running = False
        self.thread = None
        self.search_count = 0
        self.last_word = None
        self.current_search_engine = None
        self.next_search_time = 0
        self.lock = threading.Lock()

    def start(self):
        with self.lock:
            if not self.is_running:
                self.is_running = True
                self.thread = threading.Thread(target=self._run_loop, daemon=True)
                self.thread.start()
                print("Search loop manager started.")

    def stop(self):
        with self.lock:
            self.is_running = False
        if self.thread:
            # Join without holding the lock to avoid deadlocks
            self.thread.join(timeout=1)
        print("Search loop manager stopped.")

    def get_status(self):
        with self.lock:
            now = time.time()
            time_remaining = max(0.0, self.next_search_time - now) if self.is_running else 0.0
            return {
                "is_running": self.is_running,
                "search_count": self.search_count,
                "last_word": self.last_word,
                "current_search_engine": self.current_search_engine,
                "next_search_time": self.next_search_time,
                "time_remaining": round(time_remaining, 1)
            }

    def _run_loop(self):
        while True:
            with self.lock:
                if not self.is_running:
                    break
            
            cfg = config.get_config()
            engines = cfg["search_engines"]
            if not engines:
                engines = ["https://www.google.com/search?q="]

            word = word_selector.get_random_word()
            engine_url = random.choice(engines)
            full_url = f"{engine_url}{word}"

            print(f"Searching: '{word}' via {engine_url}")
            try:
                webbrowser.open(full_url)
                with self.lock:
                    self.search_count += 1
                    self.last_word = word
                    self.current_search_engine = engine_url
            except Exception as e:
                print(f"Failed to open browser search: {e}")

            # Sleep
            min_p = cfg["min_pace"]
            max_p = cfg["max_pace"]
            sleep_time = random.uniform(min_p, max_p)
            
            with self.lock:
                self.next_search_time = time.time() + sleep_time
            
            # Sub-sleep checks to respond quickly to stop requests
            start_sleep = time.time()
            while time.time() - start_sleep < sleep_time:
                with self.lock:
                    if not self.is_running:
                        break
                time.sleep(0.2)

search_loop = SearchLoopManager()
