import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(dirname(__file__)), '.env')
load_dotenv(dotenv_path)

BASE_DIR = dirname(dirname(os.path.abspath(__file__)))



try:
    from local_settings import *
except ImportError:
    pass
