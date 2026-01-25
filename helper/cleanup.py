import os
import time
import shutil
import asyncio
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def cleanup_old_files(path, minutes=360): # 360 minutes = 6 hours
    """Deletes files and folders in 'path' older than 'minutes'."""
    while True:
        try:
            now = time.time()
            cutoff = now - (minutes * 60)
            
            if os.path.exists(path):
                logger.info(f"Running scheduled cleanup for {path}...")
                for item in os.listdir(path):
                    item_path = os.path.join(path, item)
                    # Get last modified time
                    mtime = os.path.getmtime(item_path)
                    
                    if mtime < cutoff:
                        try:
                            if os.path.isfile(item_path) or os.path.islink(item_path):
                                os.unlink(item_path)
                                logger.info(f"Deleted file/link: {item_path}")
                            elif os.path.isdir(item_path):
                                shutil.rmtree(item_path)
                                logger.info(f"Deleted directory: {item_path}")
                        except Exception as e:
                            logger.error(f"Failed to delete {item_path}: {e}")
            
        except Exception as e:
            logger.error(f"Cleanup error: {e}")
            
        # Wait for 1 hour before checking again
        await asyncio.sleep(3600)
