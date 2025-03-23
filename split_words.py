#!/usr/bin/env python3
"""
This script reads word_all.txt and compares each word against COCA60000.txt.
It creates two output files:
1. words_in_coca.txt - Words that exist in COCA60000.txt (with their counts)
2. words_not_in_coca.txt - Words that don't exist in COCA60000.txt (with their counts)
"""

import os
import time
from pathlib import Path

def load_coca_words(coca_file_path):
    """Load words from COCA60000.txt into a set for efficient lookup"""
    coca_words = set()
    try:
        with open(coca_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                word = line.strip().lower()
                if word:  # Skip empty lines
                    coca_words.add(word)
        return coca_words
    except Exception as e:
        print(f"Error loading COCA word list: {e}")
        return set()

def split_words_by_coca(word_all_path, coca_words, output_dir):
    """Split words in word_all.txt based on presence in COCA wordlist"""
    # Prepare output files
    in_coca_path = os.path.join(output_dir, "words_in_coca.txt")
    not_in_coca_path = os.path.join(output_dir, "words_not_in_coca.txt")
    
    in_coca_count = 0
    not_in_coca_count = 0
    
    try:
        with open(word_all_path, 'r', encoding='utf-8') as f_in, \
             open(in_coca_path, 'w', encoding='utf-8') as f_in_coca, \
             open(not_in_coca_path, 'w', encoding='utf-8') as f_not_in_coca:
            
            for line in f_in:
                if line.strip():
                    parts = line.strip().split()
                    if len(parts) >= 2:
                        word = parts[0].lower()
                        count = parts[1]
                        
                        if word in coca_words:
                            f_in_coca.write(f"{word} {count}\n")
                            in_coca_count += 1
                        else:
                            f_not_in_coca.write(f"{word} {count}\n")
                            not_in_coca_count += 1
        
        print(f"Words found in COCA: {in_coca_count} (written to {in_coca_path})")
        print(f"Words not found in COCA: {not_in_coca_count} (written to {not_in_coca_path})")
        
    except Exception as e:
        print(f"Error processing files: {e}")

def main():
    """Main function"""
    start_time = time.time()
    
    # Set up paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    coca_file_path = os.path.join(base_dir, "library", "COCA60000.txt")
    words_dir = os.path.join(base_dir, "words")
    word_all_path = os.path.join(words_dir, "word_all.txt")
    
    # Ensure words directory exists
    os.makedirs(words_dir, exist_ok=True)
    
    # Check if input file exists
    if not os.path.exists(word_all_path):
        print(f"Error: {word_all_path} not found")
        return
    
    # Load COCA words
    coca_words = load_coca_words(coca_file_path)
    print(f"Loaded {len(coca_words)} words from COCA60000.txt")
    
    # Split words by COCA presence
    split_words_by_coca(word_all_path, coca_words, words_dir)
    
    # Log execution time
    end_time = time.time()
    print(f"Processing completed in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
