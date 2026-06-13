import logging
import os

logger = logging.getLogger(__name__)

def validate_stores():
    """Load store URLs from CSV"""
    logger.info("Loading store URLs from CSV...")
    
    stores = []
    csv_path = "config/stores.csv"
    
    # Check if file exists
    if not os.path.exists(csv_path):
        logger.error(f"CSV file not found: {csv_path}")
        return stores
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            for line in file:
                url = line.strip()
                
                # Skip empty lines and header
                if not url or url.lower() == 'url':
                    continue
                
                # Add protocol if missing
                if not url.startswith('http'):
                    url = 'https://' + url
                
                stores.append({
                    'url': url,
                    'name': url.replace('https://', '').replace('http://', '').replace('.com', '').replace('.org', '').replace('.net', '').replace('.biz', '').replace('.shop', '').title()
                })
        
        logger.info(f"Loaded {len(stores)} store URLs from CSV")
        return stores
    
    except Exception as e:
        logger.error(f"Error reading CSV: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())
        return stores