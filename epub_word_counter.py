import ebooklib
from ebooklib import epub
import re
import os
import sys
import json
from bs4 import BeautifulSoup
from pathlib import Path
import time
import hashlib

def extract_text_from_epub(epub_path):
    """Extract text content from an EPUB file."""
    book = epub.read_epub(epub_path)
    text = ""
    
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            content = item.get_content()
            soup = BeautifulSoup(content, 'html.parser')
            text += soup.get_text() + "\n"
    
    return text

def load_coca_words(coca_file_path):
    """Load allowed words from COCA60000.txt"""
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

def count_words(text, coca_words):
    """Count English words in text that appear in the COCA word list."""
    # Define pattern for English words (letters only)
    pattern = re.compile(r'\b[a-zA-Z]+\b')
    words = pattern.findall(text)
    
    # Count word occurrences
    word_count = {}
    filtered_count = 0
    
    for word in words:
        word = word.lower()  # Convert to lowercase
        
        # Only count words that appear in the COCA wordlist
        if word in coca_words:
            word_count[word] = word_count.get(word, 0) + 1
        else:
            filtered_count += 1
    
    print(f"Filtered out {filtered_count} words not found in COCA60000.txt")
    return word_count

def write_word_count_to_file(word_counts, output_file):
    """Write word counts to a file."""
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Write counts to file
    with open(output_file, 'w', encoding='utf-8') as f:
        for word, count in sorted(word_counts.items()):
            f.write(f"{word} {count}\n")
    
    print(f"Word counts written to {output_file}")

def update_word_count_file(new_counts, output_file, sort_by_frequency=False):
    """Update the word count file with new counts."""
    existing_counts = {}
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Read existing counts if file exists
    if os.path.exists(output_file):
        with open(output_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    parts = line.strip().split()
                    if len(parts) >= 2:
                        word = parts[0]
                        count = int(parts[1])
                        existing_counts[word] = count
    
    # Update counts with new data
    for word, count in new_counts.items():
        existing_counts[word] = existing_counts.get(word, 0) + count
    
    # Write updated counts to file
    with open(output_file, 'w', encoding='utf-8') as f:
        # Sort items either alphabetically or by frequency (descending)
        if sort_by_frequency:
            items = sorted(existing_counts.items(), key=lambda x: (-x[1], x[0]))
        else:
            items = sorted(existing_counts.items())
            
        for word, count in items:
            f.write(f"{word} {count}\n")
    
    print(f"Word count updated in {output_file}")

def get_epub_filename(epub_path):
    """Extract the base filename from the EPUB path without extension."""
    return Path(epub_path).stem

def get_file_hash(file_path):
    """Generate a hash of the file to identify it uniquely"""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(65536)
    return hasher.hexdigest()

def is_file_processed(epub_path, processed_files_json):
    """Check if a file has already been processed based on its hash"""
    # Calculate file hash
    file_hash = get_file_hash(epub_path)
    
    # Load processed files database
    processed_files = {}
    if os.path.exists(processed_files_json):
        try:
            with open(processed_files_json, 'r', encoding='utf-8') as f:
                processed_files = json.load(f)
        except json.JSONDecodeError:
            print(f"Warning: Could not parse {processed_files_json}, treating as empty")
    
    # Check if file hash exists in database
    return file_hash in processed_files, file_hash, processed_files

def update_processed_files(processed_files, file_hash, epub_path, processed_files_json):
    """Update the processed files database with a new file"""
    # Add file to database
    processed_files[file_hash] = {
        'path': epub_path,
        'filename': Path(epub_path).name,
        'processed_date': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # Save database
    with open(processed_files_json, 'w', encoding='utf-8') as f:
        json.dump(processed_files, f, indent=2)

def main(epub_path):
    """Main function to process an EPUB file and update word counts."""
    start_time = time.time()
    
    # Create words directory if it doesn't exist
    words_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "words")
    os.makedirs(words_dir, exist_ok=True)
    
    # Set paths for processed files tracking
    processed_files_json = os.path.join(words_dir, "processed_files.json")
    
    # Check if file has already been processed
    already_processed, file_hash, processed_files = is_file_processed(epub_path, processed_files_json)
    if already_processed:
        print(f"File '{epub_path}' has already been processed. Skipping.")
        return
    
    # Get EPUB filename (without extension)
    epub_filename = get_epub_filename(epub_path)
    
    # Set output paths
    individual_output_file = os.path.join(words_dir, f"{epub_filename}.txt")
    consolidated_output_file = os.path.join(words_dir, "words_in_coca.txt")
    
    # Load COCA wordlist
    coca_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "library", "COCA60000.txt")
    coca_words = load_coca_words(coca_file_path)
    print(f"Loaded {len(coca_words)} words from COCA60000.txt")
    
    # Extract text from EPUB
    text = extract_text_from_epub(epub_path)
    
    # Count words (filtering out words not in COCA list)
    word_counts = count_words(text, coca_words)
    
    # Write individual word counts to file
    write_word_count_to_file(word_counts, individual_output_file)
    
    # Update consolidated word count file (sorted by frequency)
    update_word_count_file(word_counts, consolidated_output_file, sort_by_frequency=True)
    
    # Record this file as processed
    update_processed_files(processed_files, file_hash, epub_path, processed_files_json)
    
    # Log execution time
    end_time = time.time()
    print(f"Processing completed in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <epub_file_path>")
        sys.exit(1)
    
    epub_path = sys.argv[1]
    
    main(epub_path)
