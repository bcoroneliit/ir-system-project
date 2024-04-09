from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
import requests

class CrawlingSpider(CrawlSpider):

    name = "mycrawler"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Illinois_Institute_of_Technology"]
    max_pages = 5
    max_depth = 5

    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': max_pages,
        'DEPTH_LIMIT': max_depth,
    }

    output_file = 'raw_paragraphs.txt'  # Output file name

    rules = (
        Rule(LinkExtractor(allow="wiki/"), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        url = response.url
        paragraphs = self.extract_paragraphs(url)
        with open(self.output_file, 'a', encoding='utf-8') as f:
            for paragraph in paragraphs:
                f.write(paragraph + '\n')
        for paragraph in paragraphs:
            yield {
                "paragraph": paragraph
            }

    def extract_paragraphs(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.find(id="mw-content-text")
        paragraphs = content.find_all('p')
        text = '\n'.join([paragraph.get_text() for paragraph in paragraphs])
        return text.split('\n')
