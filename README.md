# Wikipedia Category Word Frequency Analyzer

This project analyzes the frequency of non-common words across all Wikipedia pages in a specified category and displays the results as a word cloud.

## Features

- Retrieves all pages in a given Wikipedia category using the MediaWiki API
- Extracts text content from each page
- Removes common words (stopwords) and punctuation
- Counts the frequency of remaining words
- Outputs the top 50 most frequent non-common words
- Implements local caching to avoid redundant API requests
- Provides a web interface to visualize word frequencies as a word cloud

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

### Command-line Script

Run the script with a Wikipedia category name as a command-line argument:

```
python wiki_word_frequency.py <Wikipedia_Category>
```

Example:

```
python wiki_word_frequency.py Large_language_models
```

Note: The category name should be provided without the "Category:" prefix. Spaces in the category name should be replaced with underscores.

### Web Application

To run the web application:

```
python app.py
```

Then open a web browser and navigate to http://127.0.0.1:5000

The web application allows you to:
- Select from previously analyzed categories
- Enter a new Wikipedia category to analyze
- View word frequencies as an interactive word cloud
- Hover over words to see their exact frequency

## Caching

The script implements a local caching mechanism to avoid redundant API requests:

- Category pages and page content are cached in a `cache` directory
- Cache files are stored as JSON with timestamps
- Cache validity is set to 7 days by default
- When running the script again with the same category, it will use the cached data if available and valid

This significantly improves performance for repeated analyses of the same category.

## Output

### Command-line Script

The script will output:
- The total number of unique non-common words found
- A list of the top 50 most frequent non-common words with their frequencies

### Web Application

The web application displays:
- An interactive word cloud where word size corresponds to frequency
- Color coding to indicate relative frequency
- Tooltips showing exact word counts on hover
- Statistics about the analyzed category
