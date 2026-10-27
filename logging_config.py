import logging
import os

"""
    I will not push the local logs so if someone clone the repo
    the absence of it will trigger it's creation
"""
os.makedirs("logs", exist_ok=True)

logging.basicConfig(filename="logs/app.log", level=logging.INFO)

log = logging.getLogger("shop")