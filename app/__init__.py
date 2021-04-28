import logging
from app.db import init_db
from app import main
from bottle import run, TEMPLATE_PATH
import config

init_db()
TEMPLATE_PATH.insert(0, 'app/templates')
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger('news_parser')
logger.setLevel(config.log_level)

