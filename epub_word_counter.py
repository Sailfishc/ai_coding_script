import ebooklib
from ebooklib import epub
import re
import os
import sys
from bs4 import BeautifulSoup
from pathlib import Path

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

def count_words(text):
    """Count English words in text."""
    # Define pattern for English words (letters only)
    pattern = re.compile(r'\b[a-zA-Z]+\b')
    words = pattern.findall(text)
    
    # Count word occurrences
    word_count = {}
    for word in words:
        word = word.lower()  # Convert to lowercase
        word_count[word] = word_count.get(word, 0) + 1
    
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

def update_word_count_file(new_counts, output_file):
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
        for word, count in sorted(existing_counts.items()):
            f.write(f"{word} {count}\n")
    
    print(f"Word count updated in {output_file}")

def get_epub_filename(epub_path):
    """Extract the base filename from the EPUB path without extension."""
    return Path(epub_path).stem

def main(epub_path):
    """Main function to process an EPUB file and update word counts."""
    # Create words directory if it doesn't exist
    words_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "words")
    os.makedirs(words_dir, exist_ok=True)
    
    # Get EPUB filename (without extension)
    epub_filename = get_epub_filename(epub_path)
    
    # Set output paths
    individual_output_file = os.path.join(words_dir, f"{epub_filename}.txt")
    consolidated_output_file = os.path.join(words_dir, "word_all.txt")
    
    # Extract text from EPUB
    text = extract_text_from_epub(epub_path)
    
    # Count words
    word_counts = count_words(text)
    
    # Write individual word counts to file
    write_word_count_to_file(word_counts, individual_output_file)
    
    # Update consolidated word count file
    update_word_count_file(word_counts, consolidated_output_file)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <epub_file_path>")
        sys.exit(1)
    
    epub_path = sys.argv[1]
    
    main(epub_path)
