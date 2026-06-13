import logging

logger = logging.getLogger(__name__)

def generate_messages(stores):
    """Generate personalized messages for stores"""
    logger.info("Generating personalized messages...")
    
    for store in stores:
        message = f"""
Hello {store.get('contact_name', 'Store Manager')},

I noticed your store in {store.get('city', 'your city')} has great potential!

I can help you:
- Increase online presence
- Engage more customers
- Boost sales conversion

Let's talk about how we can help your business grow!

Best regards,
Store Automation Team
        """
        store['message'] = message.strip()
    
    logger.info(f"Generated messages for {len(stores)} stores")
    return stores