#!/usr/bin/env python3
"""
Script to download content from Anthropic's prompt library and save it to a local markdown file.
This script will crawl the website and extract the content from all relevant pages.
"""

import requests
import os
import sys
import time
import json
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from datetime import datetime

class AnthropicDocsDownloader:
    def __init__(self, base_url="https://docs.anthropic.com", output_file="anthropic_prompt_library.md"):
        self.base_url = base_url
        self.output_file = output_file
        self.visited_urls = set()
        self.prompt_library_content = []
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
        }
    
    def download_page(self, url):
        """Download page content from URL with retry logic"""
        max_retries = 3
        retry_delay = 1
        
        for attempt in range(max_retries):
            try:
                response = requests.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                return response.text
            except requests.RequestException as e:
                print(f"Error downloading {url} (attempt {attempt+1}/{max_retries}): {e}")
                if attempt < max_retries - 1:
                    print(f"Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                    retry_delay *= 2  # Exponential backoff
                else:
                    print(f"Failed to download {url} after {max_retries} attempts")
        return None
    
    def extract_page_content(self, page_content, url):
        """Extract relevant content from page HTML"""
        if not page_content:
            return None
        
        soup = BeautifulSoup(page_content, 'html.parser')
        
        # Get the title
        title_elem = soup.find('h1')
        title = title_elem.text.strip() if title_elem else os.path.basename(urlparse(url).path)
        
        # Get main content
        main_content = soup.find('main')
        if not main_content:
            return None
        
        # Extract text content
        content = self._extract_content(main_content)
        
        return {
            "title": title,
            "url": url,
            "content": content
        }
    
    def _extract_content(self, element):
        """Recursively extract text content, preserving headers and structure"""
        # Check if element is a NavigableString
        if not hasattr(element, 'name'):
            return element.string.strip() if element.string else ""
            
        if element.name in ['script', 'style']:
            return ""
        
        if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            # Add markdown heading markers based on level
            level = int(element.name[1])
            return f"\n{'#' * level} {element.text.strip()}\n"
        
        if element.name == 'p':
            return f"\n{element.text.strip()}\n"
        
        if element.name == 'code':
            return f"`{element.text.strip()}`"
        
        if element.name == 'pre':
            code = element.text.strip()
            return f"\n```\n{code}\n```\n"
        
        if element.name == 'a' and element.has_attr('href'):
            href = element['href']
            if not href.startswith(('http://', 'https://')):
                href = urljoin(self.base_url, href)
            return f"[{element.text.strip()}]({href})"
            
        # Handle lists
        if element.name == 'ul':
            content = "\n"
            for li in element.find_all('li', recursive=False):
                content += f"* {li.text.strip()}\n"
            return content
            
        if element.name == 'ol':
            content = "\n"
            for i, li in enumerate(element.find_all('li', recursive=False), 1):
                content += f"{i}. {li.text.strip()}\n"
            return content
        
        # Recursively process child elements
        content = ""
        try:
            for child in element.children:
                content += self._extract_content(child)
        except AttributeError:
            # If element doesn't have children/contents attribute
            content += element.text.strip() if hasattr(element, 'text') else ""
        
        return content
    
    def find_links(self, page_content, current_url):
        """Extract links from page content"""
        soup = BeautifulSoup(page_content, 'html.parser')
        links = []
        
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            # Skip non-HTTP links, anchors, etc.
            if href.startswith('#') or href.startswith('javascript:'):
                continue
                
            # Resolve relative URLs
            absolute_url = urljoin(current_url, href)
            
            # Only follow links within the same domain
            if urlparse(absolute_url).netloc == urlparse(self.base_url).netloc:
                links.append(absolute_url)
        
        return links
    
    def is_prompt_library_page(self, url):
        """Check if the URL is part of the prompt library"""
        parsed_url = urlparse(url)
        path = parsed_url.path
        
        # Check if the URL is in the prompt library section or is a prompt-related page
        if "/prompt-library/" in path:
            return True
            
        # Also include these relevant sections that contain prompt engineering guidelines
        relevant_sections = [
            "/docs/build-with-claude/prompt-engineering/",
            "/docs/prompt-library/",
            "/docs/build-with-claude/define-success/",
            "/docs/build-with-claude/develop-tests/"
        ]
        
        for section in relevant_sections:
            if section in path:
                return True
                
        return False
    
    def crawl(self, start_url, max_pages=100):
        """Crawl the website starting from the given URL"""
        # Use a queue instead of recursion to avoid stack overflow
        queue = [start_url]
        page_count = 0
        
        while queue and page_count < max_pages:
            url = queue.pop(0)
            
            if url in self.visited_urls:
                continue
                
            print(f"Crawling: {url} (page {page_count+1}/{max_pages})")
            self.visited_urls.add(url)
            page_count += 1
            
            page_content = self.download_page(url)
            if not page_content:
                continue
            
            # If this is a prompt library page, extract and save content
            if self.is_prompt_library_page(url):
                try:
                    content_data = self.extract_page_content(page_content, url)
                    if content_data:
                        self.prompt_library_content.append(content_data)
                        print(f"  Added content: {content_data['title']}")
                except Exception as e:
                    print(f"  Error extracting content from {url}: {e}")
            
            # Find and follow links
            links = self.find_links(page_content, url)
            for link in links:
                if link not in self.visited_urls and link not in queue:
                    # Filter out irrelevant URLs
                    if "/api/" not in link and not link.endswith(".png") and not link.endswith(".jpg"):
                        queue.append(link)
            
            # Add a small delay to be nice to the server
            time.sleep(0.5)
        
        if page_count >= max_pages:
            print(f"Reached maximum number of pages ({max_pages})")
    
    def save_to_markdown(self):
        """Save all collected content to a markdown file"""
        if not self.prompt_library_content:
            print("No content was collected")
            return
        
        # Sort content by title for better organization
        self.prompt_library_content.sort(key=lambda x: x['title'])
        
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write("# Anthropic Prompt Library\n\n")
            f.write("This document contains all prompts and guides from the Anthropic Prompt Library.\n\n")
            
            # Create table of contents
            f.write("## Table of Contents\n\n")
            for i, item in enumerate(self.prompt_library_content):
                f.write(f"{i+1}. [{item['title']}](#{item['title'].lower().replace(' ', '-')})\n")
            
            f.write("\n---\n\n")
            
            # Write content
            for item in self.prompt_library_content:
                f.write(f"## {item['title']}\n\n")
                f.write(f"Source: {item['url']}\n\n")
                f.write(f"{item['content']}\n\n")
                f.write("---\n\n")
            
            print(f"Content saved to {self.output_file}")

def main():
    # Set default output file
    output_file = "anthropic_prompt_library.md"
    
    # Set max pages to crawl (default: 100)
    max_pages = 100
    if len(sys.argv) > 1:
        try:
            max_pages = int(sys.argv[1])
            print(f"Setting max pages to crawl: {max_pages}")
        except ValueError:
            print(f"Invalid max_pages argument: {sys.argv[1]}. Using default: 100")
    
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    print(f"Starting download at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Base URL: https://docs.anthropic.com")
    print(f"Output file: {output_file}")
    print("-" * 50)
    
    # Create downloader
    downloader = AnthropicDocsDownloader(output_file=output_file)
    
    # Start crawling from the prompt library page
    start_url = "https://docs.anthropic.com/en/prompt-library/library"
    downloader.crawl(start_url, max_pages=max_pages)
    
    # Save all content to markdown file
    downloader.save_to_markdown()
    
    print("-" * 50)
    print(f"Download complete at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}!")
    print(f"Content saved to {output_file}")
    print(f"Total pages crawled: {len(downloader.visited_urls)}")
    print(f"Total content items saved: {len(downloader.prompt_library_content)}")

if __name__ == "__main__":
    main()
