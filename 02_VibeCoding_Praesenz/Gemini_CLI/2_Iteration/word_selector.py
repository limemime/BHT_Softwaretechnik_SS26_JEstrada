import os
import random
from config import config

class WordSelector:
    def __init__(self):
        self._cached_words = []
        self._cached_path = None
        self._cached_mtime = None

    def _load_dictionary(self):
        cfg = config.get_config()
        path = cfg["dictionary_path"]
        
        # Resolve path relative to this script directory if not absolute
        if not os.path.isabs(path):
            base_dir = os.path.dirname(os.path.abspath(__file__))
            path = os.path.join(base_dir, path)

        # Check if file exists
        if not os.path.exists(path):
            return ["entropy", "semantic", "chaos", "order"]

        # Check if we can use cached words
        try:
            mtime = os.path.getmtime(path)
        except Exception:
            mtime = None

        if self._cached_path == path and self._cached_mtime == mtime and self._cached_words:
            return self._cached_words

        # Reload file
        try:
            with open(path, 'r', encoding='utf-8') as f:
                words = [line.strip() for line in f if line.strip()]
            self._cached_words = words
            self._cached_path = path
            self._cached_mtime = mtime
            return words
        except Exception as e:
            print(f"Error reading dictionary file: {e}")
            if self._cached_words:
                return self._cached_words
            return ["entropy", "semantic", "chaos", "order"]

    def get_random_word(self):
        words = self._load_dictionary()
        if not words:
            return "entropy"
        return random.choice(words)

    def get_words_count(self):
        return len(self._load_dictionary())

    def get_all_words(self):
        return self._load_dictionary()

    def add_word(self, word):
        word = word.strip()
        if not word:
            return False
        cfg = config.get_config()
        path = cfg["dictionary_path"]
        if not os.path.isabs(path):
            base_dir = os.path.dirname(os.path.abspath(__file__))
            path = os.path.join(base_dir, path)
            
        words = self._load_dictionary()
        if word in words:
            return True
            
        try:
            with open(path, 'a', encoding='utf-8') as f:
                # Add newline if needed
                if words:
                    f.write(f"\n{word}")
                else:
                    f.write(word)
            # Invalidate cache
            self._cached_mtime = None
            return True
        except Exception as e:
            print(f"Error adding word: {e}")
            return False

    def remove_word(self, word):
        word = word.strip()
        if not word:
            return False
        cfg = config.get_config()
        path = cfg["dictionary_path"]
        if not os.path.isabs(path):
            base_dir = os.path.dirname(os.path.abspath(__file__))
            path = os.path.join(base_dir, path)
            
        words = self._load_dictionary()
        if word not in words:
            return False
            
        try:
            words.remove(word)
            with open(path, 'w', encoding='utf-8') as f:
                f.write("\n".join(words) + "\n")
            # Invalidate cache
            self._cached_mtime = None
            return True
        except Exception as e:
            print(f"Error removing word: {e}")
            return False

word_selector = WordSelector()
