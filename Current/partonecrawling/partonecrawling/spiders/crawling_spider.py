from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
import requests

class CrawlingSpider(CrawlSpider):

    # req initialize using seed URL
    name = "mycrawler"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Illinois_Institute_of_Technology"]

    # req max pages and max depth
    max_pages = 100
    max_depth = 100

    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': max_pages,
        'DEPTH_LIMIT': max_depth,
    }

    output_file = 'raw_titles.txt'

    rules = (
        Rule(LinkExtractor(allow="wiki/"), callback='parse_page', follow=True),
    )

    # scraping titles of the wiki pages
    def parse_page(self, response):
        title = self.extract_title(response)
        with open(self.output_file, 'a', encoding='utf-8') as f:
            f.write(title + '\n')
        yield {
            "title": title
        }

    def extract_title(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1', id='firstHeading').get_text()
        return title
