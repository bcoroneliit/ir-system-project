from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup

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

    output_file = 'paragraphs.txt'  # Output file name

    rules = (
        Rule(LinkExtractor(allow="wiki/"), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        with open(self.output_file, 'a', encoding='utf-8') as f:
            for paragraph in paragraphs:
                f.write(paragraph.get_text() + '\n')
        for paragraph in paragraphs:
            yield {
                "paragraph": paragraph.get_text()
            }
