#!/usr/bin/env python3
"""
Daily Store Automation - Main Entry Point
Runs every day via GitHub Actions
"""

import os
import sys
import logging
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/automation.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def main():
    """Main automation workflow"""
    logger.info("=" * 60)
    logger.info("STARTING DAILY STORE AUTOMATION")
    logger.info(f"Run time: {datetime.now()}")
    logger.info("=" * 60)
    
    try:
                # Import modules
        from src.validator import validate_stores
        from src.contact_finder import find_contacts
        from src.research import conduct_research
        from src.message_generator import generate_messages
        from src.delivery import send_messages
        # Phase 1: Validate stores
        logger.info("\nPHASE 1: Validating stores...")
        stores = validate_stores()
        logger.info(f"✓ Validated {len(stores)} stores")
        
        # Phase 2: Find contacts
        logger.info("\nPHASE 2: Finding contacts...")
        stores = find_contacts(stores)
        logger.info(f"✓ Found contacts for {len(stores)} stores")
        
        # Phase 3: Conduct research
        logger.info("\nPHASE 3: Conducting research...")
        stores = conduct_research(stores)
        logger.info(f"✓ Completed research on {len(stores)} stores")
        
        # Phase 4: Generate messages
        logger.info("\nPHASE 4: Generating messages...")
        stores = generate_messages(stores)
        logger.info(f"✓ Generated messages for {len(stores)} stores")
        
        # Phase 5: Send messages
        logger.info("\nPHASE 5: Sending messages...")
        results = send_messages(stores)
        logger.info(f"✓ Sent {results['sent']} messages")
        
        # Summary
        logger.info("\n" + "=" * 60)
        logger.info("✅ AUTOMATION COMPLETED SUCCESSFULLY")
        logger.info("=" * 60)
        logger.info(f"Stores processed: {len(stores)}")
        logger.info(f"Messages sent: {results['sent']}")
        logger.info(f"Errors: {results['errors']}")
        logger.info("=" * 60)
        
        return 0
        
    except Exception as e:
        logger.error(f"❌ AUTOMATION FAILED: {str(e)}", exc_info=True)
        return 1

if __name__ == "__main__":
    sys.exit(main())