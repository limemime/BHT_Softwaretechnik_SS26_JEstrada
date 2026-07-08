import json
import os
import logging

# We define the available search engine URL templates.
# The placeholder '{}' will be replaced by the URL-encoded search term.
SEARCH_ENGINES = {
    "Google": "https://www.google.com/search?q={}",
    "Bing": "https://www.bing.com/search?q={}",
    "DuckDuckGo": "https://duckduckgo.com/?q={}",
    "Yahoo": "https://search.yahoo.com/search?p={}",
    "Ecosia": "https://www.ecosia.org/search?q={}"
}

DEFAULT_MIN_SLEEP = 7
DEFAULT_MAX_SLEEP = 30
DEFAULT_DICTIONARY_FILE = "dictionary.txt"
DEFAULT_SEARCH_ENGINE = "Google"

CONFIG_FILE = "config.json"

class EngineConfig:
    """Manages the configuration parameters for the Entropy Engine."""
    
    def __init__(self, config_file=CONFIG_FILE):
        self.config_file = config_file
        
        # Initialize default values in memory
        self.min_sleep = DEFAULT_MIN_SLEEP
        self.max_sleep = DEFAULT_MAX_SLEEP
        self.dictionary_file = DEFAULT_DICTIONARY_FILE
        self.search_engine = DEFAULT_SEARCH_ENGINE
        
        # Load custom configurations if file exists
        self.load()

    def get_search_url(self, word):
        """Constructs a search URL for the specified word based on current settings."""
        template = SEARCH_ENGINES.get(self.search_engine, SEARCH_ENGINES["Google"])
        from urllib.parse import quote_plus
        return template.format(quote_plus(word))

    def load(self):
        """Loads configuration from JSON file."""
        if not os.path.exists(self.config_file):
            return
            
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            self.min_sleep = float(data.get("min_sleep", DEFAULT_MIN_SLEEP))
            self.max_sleep = float(data.get("max_sleep", DEFAULT_MAX_SLEEP))
            self.dictionary_file = str(data.get("dictionary_file", DEFAULT_DICTIONARY_FILE))
            
            engine = str(data.get("search_engine", DEFAULT_SEARCH_ENGINE))
            if engine in SEARCH_ENGINES:
                self.search_engine = engine
            else:
                self.search_engine = DEFAULT_SEARCH_ENGINE
                
            logging.info(f"Configuration loaded from {self.config_file}")
        except Exception as e:
            logging.error(f"Failed to load config: {e}. Using defaults.")

    def save(self):
        """Saves current configuration to JSON file."""
        try:
            data = {
                "min_sleep": self.min_sleep,
                "max_sleep": self.max_sleep,
                "dictionary_file": self.dictionary_file,
                "search_engine": self.search_engine
            }
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            logging.info(f"Configuration saved to {self.config_file}")
        except Exception as e:
            logging.error(f"Failed to save config: {e}")

    def update_pace(self, new_min, new_max):
        """Updates the min/max sleep configuration and saves it."""
        self.min_sleep = float(new_min)
        self.max_sleep = float(new_max)
        self.save()

    def update_engine(self, engine_name):
        """Updates the active search engine configuration and saves it."""
        if engine_name in SEARCH_ENGINES:
            self.search_engine = engine_name
            self.save()
            return True
        return False
