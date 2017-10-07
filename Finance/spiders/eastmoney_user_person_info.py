import scrapy
from scrapy.spider import spiders
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
import re
import requests
import json


class DFCFW_persion_info(scrapy.Spider):
    name = 'DFCFW_persion'
