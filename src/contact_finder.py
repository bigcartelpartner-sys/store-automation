import logging
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

def find_contacts(stores):
    """Extract contact information from store URLs"""
    logger.info("Extracting contact information from URLs...")
    
    for store in stores:
        url = store['url']
        
        # Extract domain name
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.replace('www.', '').replace('.com', '')
        
        # Generate probable email addresses
        emails = [
            f"contact@{parsed_url.netloc}",
            f"info@{parsed_url.netloc}",
            f"owner@{parsed_url.netloc}",
            f"hello@{parsed_url.netloc}"
        ]
        
        store['probable_emails'] = emails
        store['primary_email'] = emails[0]  # Use first one as primary
        store['domain'] = domain
    
    logger.info(f"Extracted contacts for {len(stores)} stores")
    return stores