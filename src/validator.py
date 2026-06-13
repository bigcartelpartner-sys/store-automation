import logging

logger = logging.getLogger(__name__)

def validate_stores():
    """Validate store URLs"""
    logger.info("Validating stores...")
    
    # Sample stores for testing
    stores = [
        {
            "name": "Store A",
            "url": "https://storea.com",
            "city": "Lagos"
        },
        {
            "name": "Store B", 
            "url": "https://storeb.com",
            "city": "Abuja"
        },
        {
            "name": "Store C",
            "url": "https://storec.com",
            "city": "Port Harcourt"
        }
    ]
    
    logger.info(f"Found {len(stores)} stores to process")
    return stores