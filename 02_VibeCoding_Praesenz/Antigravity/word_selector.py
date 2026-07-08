import random
import logging

# Curated fallback list to keep the engine functional even if the dictionary file is lost or cleared.
FALLBACK_WORDS = [
    "numismatics", "macrame", "spelunking", "quantum", "mitochondria", 
    "nebula", "epistemology", "nihilism", "stoicism", "renaissance", 
    "byzantine", "mesopotamia", "myocardium", "synapses", "leukocytes", 
    "kubernetes", "multiplexer", "semiconductor", "espresso", "sourdough", 
    "gardening", "phenomenology", "cartography", "cryptology", "taxonomy", 
    "hermeneutics", "thermodynamics", "paleontology", "astrophysics", 
    "cybernetics", "cryptography", "biosynthesis", "metallurgy", "hydroponics", 
    "aerodynamics", "nanobot", "supercapacitor", "photosynthesis", "geophysics"
]

def load_dictionary(filepath):
    """Loads, cleans, and returns words from a local dictionary text file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            words = [line.strip() for line in f if line.strip()]
            logging.info(f"Loaded {len(words)} words from dictionary file: {filepath}")
            return words
    except FileNotFoundError:
        logging.warning(f"Dictionary file not found at: {filepath}")
        return []
    except Exception as e:
        logging.error(f"Error loading dictionary file: {e}")
        return []

class WordSelector:
    """Manages loading, re-loading and selecting words for searches."""
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.words = []
        self.reload()

    def reload(self):
        """Reloads the words from the dictionary file. Falls back to default words if empty."""
        self.words = load_dictionary(self.filepath)
        if not self.words:
            logging.warning("Dictionary is empty or missing. Falling back to built-in default words.")
            self.words = FALLBACK_WORDS.copy()

    def get_random_word(self):
        """Selects and returns a random word from the current list."""
        if not self.words:
            self.reload()
        return random.choice(self.words)
