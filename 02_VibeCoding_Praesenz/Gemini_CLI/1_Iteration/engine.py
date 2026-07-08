import threading
import time
import random
import webbrowser
import os

class SearchEngine:
    def __init__(self, dictionary_path='dictionary.txt'):
        self.dictionary_path = dictionary_path
        self.words = self._load_dictionary()
        self.is_running = False
        self.thread = None
        self.search_count = 0

    def _load_dictionary(self):
        if not os.path.exists(self.dictionary_path):
            return ["entropy", "semantic", "chaos", "order"]
        with open(self.dictionary_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.thread = threading.Thread(target=self._run, daemon=True)
            self.thread.start()
            print("Engine started.")

    def stop(self):
        self.is_running = False
        if self.thread:
            self.thread.join(timeout=1)
        print("Engine stopped.")

    def _run(self):
        search_engines = [
            "https://www.google.com/search?q=",
            "https://www.bing.com/search?q="
        ]
        
        while self.is_running:
            word = random.choice(self.words)
            engine_url = random.choice(search_engines)
            full_url = f"{engine_url}{word}"
            
            print(f"Searching for: {word} on {engine_url}")
            webbrowser.open(full_url)
            self.search_count += 1
            
            # Random sleep between 7 and 30 seconds
            sleep_time = random.uniform(7, 30)
            print(f"Next search in {sleep_time:.2f} seconds...")
            
            start_sleep = time.time()
            while time.time() - start_sleep < sleep_time:
                if not self.is_running:
                    break
                time.sleep(0.5)

engine = SearchEngine()
