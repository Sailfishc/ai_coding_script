#!/usr/bin/env python3
"""
Script to download content from Anthropic's user guides and save it to a local markdown file.
This script will crawl the welcome page, find all guide links, and extract the content from each page.
"""

import requests
import os
import sys
import time
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from datetime import datetime

class AnthropicGuidesDownloader:
    def __init__(self, base_url="https://docs.anthropic.com", output_file="user_guide.md"):
        self.base_url = base_url
        self.output_file = output_file
        self.visited_urls = set()
        self.guide_content = []
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
    
    def find_guide_links(self, welcome_page_content, welcome_url):
        """Extract guide links from the welcome page"""
        soup = BeautifulSoup(welcome_page_content, 'html.parser')
        links = []
        
        # Find all links on the page
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            # Skip non-HTTP links, anchors, etc.
            if href.startswith('#') or href.startswith('javascript:'):
                continue
                
            # Resolve relative URLs
            absolute_url = urljoin(welcome_url, href)
            
            # Only include guide links
            if ("/docs/" in absolute_url and 
                urlparse(absolute_url).netloc == urlparse(self.base_url).netloc and
                "/api/" not in absolute_url):
                links.append(absolute_url)
        
        return links
    
    def process_guides(self, welcome_url):
        """Process all guide links from the welcome page"""
        print(f"Downloading content from: {welcome_url}")
        welcome_content = self.download_page(welcome_url)
        if not welcome_content:
            print("Failed to download the welcome page")
            return
        
        # Find all guide links
        guide_links = self.find_guide_links(welcome_content, welcome_url)
        print(f"Found {len(guide_links)} guide links")
        
        # Process each guide link
        for i, url in enumerate(guide_links, 1):
            if url in self.visited_urls:
                continue
                
            print(f"Processing guide {i}/{len(guide_links)}: {url}")
            self.visited_urls.add(url)
            
            page_content = self.download_page(url)
            if not page_content:
                continue
                
            try:
                content_data = self.extract_page_content(page_content, url)
                if content_data:
                    self.guide_content.append(content_data)
                    print(f"  Added content: {content_data['title']}")
            except Exception as e:
                print(f"  Error extracting content from {url}: {e}")
                
            # Add a small delay to be nice to the server
            time.sleep(1)
    
    def save_to_markdown(self):
        """Save all collected content to a markdown file"""
        if not self.guide_content:
            print("No content was collected")
            return
        
        # Sort content by title for better organization
        self.guide_content.sort(key=lambda x: x['title'])
        
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write("# Anthropic User Guides\n\n")
            f.write("This document contains all user guides from the Anthropic documentation.\n\n")
            
            # Create table of contents
            f.write("## Table of Contents\n\n")
            for i, item in enumerate(self.guide_content, 1):
                title = item['title']
                anchor = title.lower().replace(' ', '-').replace('?', '').replace('!', '').replace('.', '')
                f.write(f"{i}. [{title}](#{anchor})\n")
            
            f.write("\n---\n\n")
            
            # Write each content section
            for item in self.guide_content:
                title = item['title']
                content = item['content']
                url = item['url']
                
                f.write(f"## {title}\n\n")
                f.write(f"Source: {url}\n\n")
                f.write(f"{content}\n\n")
                f.write("---\n\n")
            
            print(f"Content saved to {self.output_file}")

def main():
    # Set default output file
    output_file = "user_guide.md"
    
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    print(f"Starting download at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Base URL: https://docs.anthropic.com")
    print(f"Output file: {output_file}")
    print("-" * 50)
    
    # Create downloader
    downloader = AnthropicGuidesDownloader(output_file=output_file)
    
    # Start processing from the welcome page
    welcome_url = "https://docs.anthropic.com/en/docs/welcome"
    downloader.process_guides(welcome_url)
    
    # Save all content to markdown file
    downloader.save_to_markdown()
    
    print("-" * 50)
    print(f"Download complete at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}!")
    print(f"Content saved to {output_file}")
    print(f"Total pages crawled: {len(downloader.visited_urls)}")
    print(f"Total content items saved: {len(downloader.guide_content)}")

if __name__ == "__main__":
    main()
