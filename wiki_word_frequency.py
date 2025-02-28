#!/usr/bin/env python3
"""
Wikipedia Category Word Frequency Analyzer

This script takes a Wikipedia category as input and outputs the cumulative frequency
of non-common words across all pages in that category.
"""

import sys
import requests
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string
import time

def download_nltk_resources():
    """Download required NLTK resources if not already downloaded."""
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/stopwords')
    except LookupError:
        print("Downloading required NLTK resources...")
        nltk.download('punkt')
        nltk.download('stopwords')

def get_pages_in_category(category):
    """
    Get all pages in a Wikipedia category using the MediaWiki API.
    
    Args:
        category (str): The Wikipedia category name (without the 'Category:' prefix)
        
    Returns:
        list: A list of page titles in the category
    """
    print(f"Retrieving pages in category: {category}")
    
    # Add 'Category:' prefix if not present
    if not category.startswith("Category:"):
        category = f"Category:{category}"
    
    session = requests.Session()
    url = "https://en.wikipedia.org/w/api.php"
    
    # Get all pages in the category
    cmcontinue = None
    all_pages = []
    
    while True:
        params = {
            "action": "query",
            "format": "json",
            "list": "categorymembers",
            "cmtitle": category,
            "cmlimit": 500,  # Maximum allowed by the API
            "cmtype": "page"  # Only get pages, not subcategories
        }
        
        if cmcontinue:
            params["cmcontinue"] = cmcontinue
        
        response = session.get(url=url, params=params)
        data = response.json()
        
        if "query" in data and "categorymembers" in data["query"]:
            pages = [page["title"] for page in data["query"]["categorymembers"]]
            all_pages.extend(pages)
            
            print(f"Retrieved {len(pages)} pages...")
            
            if "continue" in data and "cmcontinue" in data["continue"]:
                cmcontinue = data["continue"]["cmcontinue"]
                # Add a small delay to avoid hitting API rate limits
                time.sleep(0.5)
            else:
                break
        else:
            break
    
    print(f"Total pages found: {len(all_pages)}")
    return all_pages

def get_page_content(page_title):
    """
    Get the content of a Wikipedia page using the MediaWiki API.
    
    Args:
        page_title (str): The title of the Wikipedia page
        
    Returns:
        str: The text content of the page
    """
    session = requests.Session()
    url = "https://en.wikipedia.org/w/api.php"
    
    params = {
        "action": "query",
        "format": "json",
        "titles": page_title,
        "prop": "extracts",
        "explaintext": True,  # Get plain text content
        "exsectionformat": "plain"
    }
    
    response = session.get(url=url, params=params)
    data = response.json()
    
    # Extract the page content
    pages = data["query"]["pages"]
    page_id = list(pages.keys())[0]
    
    if "extract" in pages[page_id]:
        return pages[page_id]["extract"]
    else:
        return ""

def analyze_text(text):
    """
    Analyze text to count non-common words.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        Counter: A Counter object with word frequencies
    """
    # Tokenize the text
    tokens = word_tokenize(text.lower())
    
    # Remove punctuation and numbers
    tokens = [word for word in tokens if word not in string.punctuation and not word.isdigit()]
    
    # Remove stopwords (common words)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and len(word) > 1]
    
    # Count word frequencies
    return Counter(tokens)

def main():
    """Main function to run the script."""
    # Check command line arguments
    if len(sys.argv) < 2:
        print("Usage: python wiki_word_frequency.py <Wikipedia_Category>")
        print("Example: python wiki_word_frequency.py Large_language_models")
        sys.exit(1)
    
    # Get the category from command line arguments
    category = sys.argv[1]
    
    # Download NLTK resources if needed
    download_nltk_resources()
    
    # Get all pages in the category
    pages = get_pages_in_category(category)
    
    if not pages:
        print(f"No pages found in category: {category}")
        sys.exit(1)
    
    # Process each page and count word frequencies
    total_word_count = Counter()
    
    for i, page in enumerate(pages):
        print(f"Processing page {i+1}/{len(pages)}: {page}")
        content = get_page_content(page)
        
        if content:
            word_counts = analyze_text(content)
            total_word_count.update(word_counts)
        else:
            print(f"No content found for page: {page}")
    
    # Output the results
    print("\nWord frequency analysis complete!")
    print(f"Total unique non-common words: {len(total_word_count)}")
    
    # Get the top 50 most common words
    most_common = total_word_count.most_common(50)
    
    print("\nTop 50 most frequent non-common words:")
    print("-" * 40)
    print(f"{'WORD':<20} {'FREQUENCY':<10}")
    print("-" * 40)
    
    for word, count in most_common:
        print(f"{word:<20} {count:<10}")

if __name__ == "__main__":
    main()
