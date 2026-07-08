import threading

class AppConfig:
    def __init__(self):
        self.lock = threading.Lock()
        self.min_pace = 7.0
        self.max_pace = 30.0
        self.search_engines = [
            "https://www.google.com/search?q=",
            "https://www.bing.com/search?q="
        ]
        self.dictionary_path = "dictionary.txt"

    def get_config(self):
        with self.lock:
            return self._get_config_unlocked()

    def update_config(self, data):
        with self.lock:
            if "min_pace" in data:
                self.min_pace = float(data["min_pace"])
            if "max_pace" in data:
                self.max_pace = float(data["max_pace"])
            if "search_engines" in data:
                self.search_engines = list(data["search_engines"])
            if "dictionary_path" in data:
                self.dictionary_path = str(data["dictionary_path"])
            return self._get_config_unlocked()

    def _get_config_unlocked(self):
        return {
            "min_pace": self.min_pace,
            "max_pace": self.max_pace,
            "search_engines": list(self.search_engines),
            "dictionary_path": self.dictionary_path
        }

    def set_pace(self, min_pace, max_pace):
        with self.lock:
            self.min_pace = float(min_pace)
            self.max_pace = float(max_pace)

    def add_search_engine(self, url):
        with self.lock:
            if url not in self.search_engines:
                self.search_engines.append(url)

    def remove_search_engine(self, url):
        with self.lock:
            if url in self.search_engines:
                self.search_engines.remove(url)

config = AppConfig()
