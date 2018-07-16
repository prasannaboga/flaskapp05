import os
from os.path import join, dirname
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SOMETHING = os.getenv('SOMETHING')
THREE = os.environ['THREE']
DEBUG = os.environ['DEBUG']
