import scrapy
from items import SlowmistItem


class SlowmistSpider(scrapy.Spider):
    name = 'slowmist-spider'
    start_urls = [
        'https://hacked.slowmist.io/',
    ]

    def parse(self, response):
        for li in response.xpath('//div[@class="case-content"]//ul//li'):
            yield SlowmistItem(
                time=li.xpath('.//span[@class="time"]/text()').extract_first(),
                target=li.xpath(
                    './/h3/em[contains(text(),"Hacked target:")]/following-sibling::text()').get().strip(),
                description=li.xpath(
                    './/p/em[contains(text(),"Description of the event:")]/following-sibling::text()').get().strip(),
                amount_of_loss=li.xpath('.//p/span[1]/text()').extract_first().strip(),
                attack_method=li.xpath('.//p/span[2]/text()').extract_first().strip(),
                reference_url=li.xpath('.//p[@class="link-reference"]/a/@href').extract_first()
            )
