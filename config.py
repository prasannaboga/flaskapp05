import os
from os.path import join, dirname
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# For options config variables use os.getenv('key') or os.environ.get('key')
# For mandatory config variables use os.eniron['key']

SOMETHING = os.getenv('SOMETHING')
THREE = os.environ['THREE']

