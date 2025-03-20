#!/usr/bin/env python3
"""
Sort words in word_all.txt by frequency (count) in descending order
and write the result to word_all_sort.txt
"""

def sort_word_counts(input_file, output_file):
    """
    Sort words from input file by their count in descending order
    and write to output file
    """
    # Read the input file and parse word counts
    word_counts = {}
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    parts = line.strip().split()
                    if len(parts) >= 2:
                        word = parts[0]
                        try:
                            count = int(parts[1])
                            word_counts[word] = count
                        except ValueError:
                            # Skip lines with non-integer counts
                            continue
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return
    
    # Sort word counts by count in descending order
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Write sorted words to output file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for word, count in sorted_words:
                f.write(f"{word} {count}\n")
        print(f"Sorted word counts written to {output_file}")
    except Exception as e:
        print(f"Error writing to output file: {e}")

if __name__ == "__main__":
    input_file = "word_all.txt"
    output_file = "word_all_sort.txt"
    sort_word_counts(input_file, output_file)
