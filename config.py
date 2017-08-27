import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


REDDIT_SECRET = os.environ.get("REDDIT_SECRET")
REDDIT_ID = os.environ.get("REDDIT_ID")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
