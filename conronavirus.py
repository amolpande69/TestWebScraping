import scrapy


class ConronavirusSpider(scrapy.Spider):
    name = "coronavirus"
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        for country in response.xpath("//td/a"):
            print(country.xpath(".//text()").get())
            link = country.xpath(".//@href").get()
            print(link)
            absolute_url = response.urljoin(link)
            print(absolute_url)
            yield
            {
                # 'country-name': country.xpath(".//text()").get(),
                'country-link': absolute_url
            }
