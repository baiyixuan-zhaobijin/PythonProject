import arrow
from bs4 import BeautifulSoup
from peewee import *
yesterday = arrow.utcnow().shift(days=-1).format('YYYY-MM-DD')

