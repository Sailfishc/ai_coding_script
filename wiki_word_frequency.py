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
import os
import json
import hashlib
from bs4 import BeautifulSoup
from datetime import datetime

def download_nltk_resources():
    """Download required NLTK resources if not already downloaded."""
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/stopwords')
    except LookupError:
        print("Downloading required NLTK resources...")
        nltk.download('punkt')
        nltk.download('stopwords')

def create_cache_dir():
    """Create a cache directory if it doesn't exist."""
    cache_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    return cache_dir

def get_cache_filename(category, content_type):
    """
    Generate a cache filename for a category and content type.
    
    Args:
        category (str): The Wikipedia category name
        content_type (str): The type of content ('pages' or 'content')
        
    Returns:
        str: The cache filename
    """
    # Create a hash of the category name to use in the filename
    category_hash = hashlib.md5(category.encode()).hexdigest()
    return f"{category_hash}_{content_type}.json"

def load_from_cache(category, content_type):
    """
    Load data from cache if available.
    
    Args:
        category (str): The Wikipedia category name
        content_type (str): The type of content ('pages' or 'content')
        
    Returns:
        dict or None: The cached data if available, None otherwise
    """
    cache_dir = create_cache_dir()
    cache_file = os.path.join(cache_dir, get_cache_filename(category, content_type))
    
    if os.path.exists(cache_file):
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                cached_data = json.load(f)
            
            # Check if the cache is still valid (less than 7 days old)
            cache_timestamp = cached_data.get('timestamp', 0)
            current_time = datetime.now().timestamp()
            
            # 7 days in seconds
            cache_validity = 7 * 24 * 60 * 60
            
            if current_time - cache_timestamp < cache_validity:
                print(f"Loading {content_type} from cache...")
                return cached_data
            else:
                print(f"Cache for {content_type} is outdated. Fetching fresh data...")
                return None
        except Exception as e:
            print(f"Error loading from cache: {e}")
            return None
    else:
        print(f"No cache found for {content_type}.")
        return None

def save_to_cache(category, content_type, data):
    """
    Save data to cache.
    
    Args:
        category (str): The Wikipedia category name
        content_type (str): The type of content ('pages' or 'content')
        data: The data to cache
    """
    cache_dir = create_cache_dir()
    cache_file = os.path.join(cache_dir, get_cache_filename(category, content_type))
    
    # Add timestamp to the data
    data_to_cache = {
        'timestamp': datetime.now().timestamp(),
        'data': data
    }
    
    try:
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(data_to_cache, f, ensure_ascii=False, indent=2)
        print(f"Saved {content_type} to cache.")
    except Exception as e:
        print(f"Error saving to cache: {e}")

def get_pages_in_category(category):
    """
    Get all pages in a Wikipedia category using the MediaWiki API.
    
    Args:
        category (str): The Wikipedia category name (without the 'Category:' prefix)
        
    Returns:
        list: A list of page titles in the category
    """
    # Add 'Category:' prefix if not present
    full_category = category
    if not category.startswith("Category:"):
        full_category = f"Category:{category}"
    
    # Check cache first
    cached_data = load_from_cache(full_category, 'pages')
    if cached_data:
        return cached_data['data']
    
    print(f"Retrieving pages in category: {category}")
    
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
            "cmtitle": full_category,
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
    
    # Save to cache
    save_to_cache(full_category, 'pages', all_pages)
    
    return all_pages

def get_page_content(page_title):
    """
    Get the content of a Wikipedia page using the MediaWiki API.
    
    Args:
        page_title (str): The title of the Wikipedia page
        
    Returns:
        str: The text content of the page
    """
    # Check cache first
    cached_data = load_from_cache(page_title, 'content')
    if cached_data:
        return cached_data['data']
    
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
    
    content = ""
    if "extract" in pages[page_id]:
        content = pages[page_id]["extract"]
    
    # Save to cache
    save_to_cache(page_title, 'content', content)
    
    return content

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
    
    # Create cache directory if it doesn't exist
    create_cache_dir()
    
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
