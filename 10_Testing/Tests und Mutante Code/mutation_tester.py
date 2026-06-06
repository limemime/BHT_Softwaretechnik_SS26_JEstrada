import os
import sys
import subprocess
import shutil

# Paths to the target and test files
ENGINE_PATH = 'engine.py'
ENGINE_BACKUP_PATH = 'engine.py.bak'
TEST_COMMAND = [sys.executable, '-m', 'unittest', 'test_engine.py']

# List of mutants to inject into engine.py
MUTATIONS = [
    {
        "name": "Mutant 1: Swap sleep assignment (self.min_sleep = max_sleep)",
        "target": "self.min_sleep = min_sleep",
        "replacement": "self.min_sleep = max_sleep"
    },
    {
        "name": "Mutant 2: Initial running status set to True",
        "target": "self.running = False",
        "replacement": "self.running = True"
    },
    {
        "name": "Mutant 3: Initial search_count starts at 1 instead of 0",
        "target": "self.search_count = 0",
        "replacement": "self.search_count = 1"
    },
    {
        "name": "Mutant 4: Load dictionary without stripping leading/trailing whitespace",
        "target": "return [line.strip() for line in f if line.strip()]",
        "replacement": "return [line for line in f if line.strip()]"
    },
    {
        "name": "Mutant 5: Load dictionary without filtering empty lines",
        "target": "return [line.strip() for line in f if line.strip()]",
        "replacement": "return [line.strip() for line in f]"
    },
    {
        "name": "Mutant 6: Re-raise FileNotFoundError instead of handling it",
        "target": "except FileNotFoundError:\n            # We log a clear warning to the user terminal.\n            logging.error(f\"Dictionary file '{self.filepath}' not found.\")\n            # We return an empty list as a safe fallback.\n            return []",
        "replacement": "except FileNotFoundError:\n            raise"
    },
    {
        "name": "Mutant 7: Re-raise general Exception instead of handling it",
        "target": "except Exception as e:\n            # We log the specific error to aid in debugging.\n            logging.error(f\"Error reading dictionary: {e}\")\n            # We return an empty list to prevent application crashes.\n            return []",
        "replacement": "except Exception as e:\n            raise"
    },
    {
        "name": "Mutant 8: Change dictionary loading file encoding from utf-8 to ascii (Expected to SURVIVE)",
        "target": "encoding='utf-8'",
        "replacement": "encoding='ascii'"
    },
    {
        "name": "Mutant 9: Swap min/max assignments in update_pace() (Expected to SURVIVE)",
        "target": "self.min_sleep = new_min\n        # We update the instance variable for maximum sleep time.\n        self.max_sleep = new_max",
        "replacement": "self.min_sleep = new_max\n        # We update the instance variable for maximum sleep time.\n        self.max_sleep = new_min"
    },
    {
        "name": "Mutant 10: Invert running logic in stop() (set self.running = True) (Expected to SURVIVE)",
        "target": "def stop(self):\n        # We set the running flag to False to break loop.\n        self.running = False",
        "replacement": "def stop(self):\n        # We set the running flag to False to break loop.\n        self.running = True"
    },
    {
        "name": "Mutant 11: Disable daemon thread behavior in start() (daemon=False) (Expected to SURVIVE)",
        "target": "daemon=True",
        "replacement": "daemon=False"
    },
    {
        "name": "Mutant 12: Modify Selenium options to run in non-headless mode (Expected to SURVIVE)",
        "target": "chrome_options.add_argument(\"--headless\")",
        "replacement": "chrome_options.add_argument(\"--some-other-arg\")"
    }
]

def run_mutation_tests():
    # Verify files exist
    if not os.path.exists(ENGINE_PATH):
        print(f"Error: {ENGINE_PATH} not found.")
        sys.exit(1)

    print("=" * 70)
    print("MUTATION TESTING REPORT FOR EntropyEngine.__init__")
    print("=" * 70)

    # 1. Run baseline tests to make sure everything passes initially
    print("Running baseline tests...")
    baseline = subprocess.run(TEST_COMMAND, capture_output=True, text=True)
    if baseline.returncode != 0:
        print("Error: Baseline tests are failing! Fix tests first.")
        print(baseline.stderr or baseline.stdout)
        sys.exit(1)
    print("Baseline tests passed successfully. Starting mutation trials...\n")

    killed_count = 0
    total_mutants = len(MUTATIONS)

    # Backup original engine.py
    shutil.copy2(ENGINE_PATH, ENGINE_BACKUP_PATH)

    try:
        for i, mutation in enumerate(MUTATIONS, 1):
            name = mutation["name"]
            target = mutation["target"]
            replacement = mutation["replacement"]

            # Read backup content
            with open(ENGINE_BACKUP_PATH, 'r', encoding='utf-8') as f:
                content = f.read()

            # Ensure target string exists in the code
            if target not in content:
                print(f"[{i}/{total_mutants}] SURVIVED (Target pattern not found in source file!)")
                print(f"  Mutation: {name}\n")
                continue

            # Apply mutation
            mutated_content = content.replace(target, replacement, 1)
            with open(ENGINE_PATH, 'w', encoding='utf-8') as f:
                f.write(mutated_content)

            # Run the test suite on the mutated code
            result = subprocess.run(TEST_COMMAND, capture_output=True, text=True)

            if result.returncode != 0:
                killed_count += 1
                # Find which test failed from the output
                failure_reason = "Test suite failed (mutant killed)."
                for line in result.stderr.splitlines():
                    if line.startswith("FAIL:") or line.startswith("ERROR:"):
                        failure_reason = line.strip()
                        break
                print(f"[{i}/{total_mutants}] KILLED: {name}")
                print(f"  Reason: {failure_reason}\n")
            else:
                print(f"[{i}/{total_mutants}] SURVIVED: {name}")
                print("  WARNING: Test suite passed. Mutation was NOT caught!\n")

    finally:
        # Restore the original engine.py
        shutil.copy2(ENGINE_BACKUP_PATH, ENGINE_PATH)
        if os.path.exists(ENGINE_BACKUP_PATH):
            os.remove(ENGINE_BACKUP_PATH)

    # Summary
    score = (killed_count / total_mutants) * 100
    print("=" * 70)
    print("MUTATION SUMMARY")
    print("=" * 70)
    print(f"Total Mutants Generated: {total_mutants}")
    print(f"Total Mutants Killed:    {killed_count}")
    print(f"Total Mutants Survived:  {total_mutants - killed_count}")
    print(f"Mutation Score:          {score:.2f}%")
    print("=" * 70)

if __name__ == '__main__':
    run_mutation_tests()
