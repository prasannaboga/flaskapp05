import os
from os.path import join, dirname
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# For options config variables use os.getenv('key') or os.environ.get('key')
# For mandatory config variables use os.eniron['key']

MONGODB_HOST_URI = os.environ['MONGODB_HOST_URI']
MONGODB_DATABASE = os.environ['MONGODB_DATABASE']
SECRET_KEY = os.environ['SECRET_KEY']
SOMETHING = os.getenv('SOMETHING')
THREE = os.environ['THREE']

