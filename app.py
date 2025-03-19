#!/usr/bin/env python3
"""
Wikipedia Category Word Frequency Web Application

This Flask application displays word clouds for Wikipedia categories
using the data from the wiki_word_frequency.py script.
"""

import os
import json
import base64
from io import BytesIO
from datetime import datetime
from collections import Counter
from flask import Flask, render_template, request, jsonify, send_from_directory

# Import functions from our wiki_word_frequency.py script
from wiki_word_frequency import (
    download_nltk_resources, get_pages_in_category, 
    get_page_content, analyze_text, create_cache_dir,
    load_from_cache, save_to_cache, get_cache_filename
)

app = Flask(__name__)

# Make sure NLTK resources are downloaded
download_nltk_resources()

def get_word_frequencies(category):
    """
    Get word frequencies for a category, either from cache or by computing them.
    
    Args:
        category (str): The Wikipedia category name
        
    Returns:
        dict: A dictionary with word frequencies
    """
    # Create cache directory if it doesn't exist
    cache_dir = create_cache_dir()
    
    # Check if we have already cached the word frequencies
    full_category = category
    if not category.startswith("Category:"):
        full_category = f"Category:{category}"
    
    frequencies_cache_file = os.path.join(
        cache_dir, 
        f"{get_cache_filename(full_category, 'frequencies').split('.')[0]}.json"
    )
    
    # Try to load from frequencies cache
    if os.path.exists(frequencies_cache_file):
        try:
            with open(frequencies_cache_file, 'r', encoding='utf-8') as f:
                cached_data = json.load(f)
            
            # Check if the cache is still valid (less than 7 days old)
            cache_timestamp = cached_data.get('timestamp', 0)
            current_time = datetime.now().timestamp()
            
            # 7 days in seconds
            cache_validity = 7 * 24 * 60 * 60
            
            if current_time - cache_timestamp < cache_validity:
                print(f"Loading word frequencies from cache...")
                return cached_data['data']
        except Exception as e:
            print(f"Error loading frequencies from cache: {e}")
    
    # If we don't have cached frequencies, compute them
    print(f"Computing word frequencies for category: {category}")
    
    # Get all pages in the category
    pages = get_pages_in_category(category)
    
    if not pages:
        return {}
    
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
    
    # Convert Counter to dictionary
    word_frequencies = dict(total_word_count)
    
    # Save frequencies to cache
    data_to_cache = {
        'timestamp': datetime.now().timestamp(),
        'data': word_frequencies
    }
    
    try:
        with open(frequencies_cache_file, 'w', encoding='utf-8') as f:
            json.dump(data_to_cache, f, ensure_ascii=False, indent=2)
        print(f"Saved word frequencies to cache.")
    except Exception as e:
        print(f"Error saving frequencies to cache: {e}")
    
    return word_frequencies

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/api/categories')
def get_available_categories():
    """Get a list of categories that have cached data."""
    cache_dir = create_cache_dir()
    categories = []
    
    if os.path.exists(cache_dir):
        for filename in os.listdir(cache_dir):
            if filename.endswith('_pages.json'):
                try:
                    with open(os.path.join(cache_dir, filename), 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    # Extract category name from cache data if possible
                    if 'category' in data:
                        categories.append(data['category'])
                except Exception:
                    continue
    
    # Add some default categories if we don't have any
    if not categories:
        categories = ["Large_language_models", "Artificial_intelligence", "Machine_learning"]
    
    return jsonify(categories)

@app.route('/api/wordcloud')
def get_wordcloud_data():
    """Get word frequency data for a category."""
    category = request.args.get('category', 'Large_language_models')
    
    # Get word frequencies
    word_frequencies = get_word_frequencies(category)
    
    # Return the top 100 words for the word cloud
    top_words = dict(Counter(word_frequencies).most_common(100))
    
    return jsonify(top_words)

@app.route('/static/<path:path>')
def send_static(path):
    """Serve static files."""
    return send_from_directory('static', path)

if __name__ == '__main__':
    # Create necessary directories
    if not os.path.exists('templates'):
        os.makedirs('templates')
    if not os.path.exists('static'):
        os.makedirs('static')
    
    app.run(debug=True)
