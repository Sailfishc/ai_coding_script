# Wikipedia Category Word Frequency Analyzer

This script analyzes the frequency of non-common words across all Wikipedia pages in a specified category.

## Features

- Retrieves all pages in a given Wikipedia category using the MediaWiki API
- Extracts text content from each page
- Removes common words (stopwords) and punctuation
- Counts the frequency of remaining words
- Outputs the top 50 most frequent non-common words

## Requirements

- Python 3.6+
- Required Python packages (see requirements.txt)

## Installation

1. Clone this repository
2. Install the required packages:

```
pip install -r requirements.txt
```

## Usage

Run the script with a Wikipedia category name as a command-line argument:

```
python wiki_word_frequency.py <Wikipedia_Category>
```

Example:

```
python wiki_word_frequency.py Large_language_models
```

Note: The category name should be provided without the "Category:" prefix. Spaces in the category name should be replaced with underscores.

## Output

The script will output:
- The total number of unique non-common words found
- A list of the top 50 most frequent non-common words with their frequencies
