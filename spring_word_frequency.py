#!/usr/bin/env python3
"""
Spring Framework Documentation Word Frequency Analyzer

This script scrapes the Spring Framework documentation from the specified URL and its subdirectories,
extracts all words, counts their frequencies, and writes them to a file in descending order of frequency.
"""

import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string
import time
import os
from urllib.parse import urljoin

def download_nltk_resources():
    """Download required NLTK resources if not already downloaded."""
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/stopwords')
    except LookupError:
        print("Downloading required NLTK resources...")
        nltk.download('punkt')
        nltk.download('stopwords')

def get_html_links(url):
    """
    Get all HTML links from a page.
    
    Args:
        url (str): The URL to scrape
        
    Returns:
        list: A list of HTML file URLs found on the page
    """
    print(f"Getting links from: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        links = []
        # Find all links in the page
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            # Only include HTML files
            if href.endswith('.html'):
                # Convert relative URLs to absolute URLs
                absolute_url = urljoin(url, href)
                # Only include URLs from the same domain
                if 'docs.spring.io/spring-framework/reference/core' in absolute_url:
                    links.append(absolute_url)
        
        return links
    except Exception as e:
        print(f"Error getting links from {url}: {e}")
        return []

def get_page_content(url):
    """
    Get the text content of a web page.
    
    Args:
        url (str): The URL of the page
        
    Returns:
        str: The text content of the page
    """
    print(f"Getting content from: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.extract()
        
        # Get text
        text = soup.get_text()
        
        # Break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # Break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # Drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text
    except Exception as e:
        print(f"Error getting content from {url}: {e}")
        return ""

def extract_words(text):
    """
    Extract words from text.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        list: A list of words
    """
    # Tokenize text
    tokens = word_tokenize(text.lower())
    
    # Remove punctuation and non-alphabetic tokens
    words = [word for word in tokens if word.isalpha()]
    
    return words

def process_spring_docs():
    """
    Process the Spring Framework documentation.
    
    Returns:
        Counter: A Counter object with word frequencies
    """
    base_url = "https://docs.spring.io/spring-framework/reference/core"
    all_words = []
    visited_urls = set()
    
    # Start with the main HTML files in the core directory
    initial_html_files = [
        f"{base_url}/aop-api.html",
        f"{base_url}/aop.html",
        f"{base_url}/aot.html",
        f"{base_url}/appendix.html",
        f"{base_url}/beans.html",
        f"{base_url}/databuffer-codec.html",
        f"{base_url}/expressions.html",
        f"{base_url}/null-safety.html",
        f"{base_url}/resources.html",
        f"{base_url}/spring-jcl.html",
        f"{base_url}/validation.html"
    ]
    
    # Process each HTML file
    for html_file in initial_html_files:
        if html_file in visited_urls:
            continue
            
        visited_urls.add(html_file)
        
        # Get content and extract words
        content = get_page_content(html_file)
        words = extract_words(content)
        all_words.extend(words)
        
        # Get links to other HTML files
        links = get_html_links(html_file)
        
        # Process each linked HTML file
        for link in links:
            if link in visited_urls:
                continue
                
            visited_urls.add(link)
            
            # Get content and extract words
            content = get_page_content(link)
            words = extract_words(content)
            all_words.extend(words)
            
            # Be nice to the server
            time.sleep(1)
    
    return Counter(all_words)

def main():
    """Main function to run the script."""
    # Download NLTK resources if needed
    download_nltk_resources()
    
    print("Starting to process Spring Framework documentation")
    word_counts = process_spring_docs()
    
    # Sort words by frequency (highest first)
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Write results to file
    output_file = "spring_words.md"
    print(f"Writing results to {output_file}")
    with open(output_file, 'w') as f:
        for word, count in sorted_words:
            f.write(f"{word}\n")
    
    print(f"Analysis complete. Found {len(sorted_words)} unique words.")
    print(f"Top 10 most frequent words:")
    for word, count in sorted_words[:10]:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
