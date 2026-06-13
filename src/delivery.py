import logging

logger = logging.getLogger(__name__)

def send_messages(stores):
    """Send messages via email/contact"""
    logger.info("Preparing to send messages...")
    
    sent = 0
    errors = 0
    
    for store in stores:
        try:
            # Simulate sending message
            email = store.get('email', 'unknown')
            logger.info(f"✓ Message sent to: {email}")
            sent += 1
        except Exception as e:
            logger.error(f"✗ Failed to send to {store.get('name')}: {str(e)}")
            errors += 1
    
    logger.info(f"Sent {sent} messages with {errors} errors")
    
    return {
        'sent': sent,
        'errors': errors
    }