import scrapy
from scrapy.crawler import CrawlerProcess
import sys
import json
from pprint import pprint
from typing import List, Union, Dict

if __name__ == "__main__":
    from api import RedditApi, SUBREDDITS
    from deep_key_test import deep_key_test
else:
    try:
        from .api import RedditApi, SUBREDDITS
        from .deep_key_test import deep_key_test
    except Exception:
        from api import RedditApi, SUBREDDITS
        from deep_key_test import deep_key_test

class RedditSpider(scrapy.Spider):
    name = 'reddit'
    total_results = 0 # DEBUG

    def __init__(self, subreddit='cooking', *args, **kwargs):
        # this allows to pass the subreddit as an argument of the script (scrapy crawl reddit_get_first_id -a category=electronics)
        super(RedditSpider, self).__init__(*args, **kwargs)
        self.name = subreddit
        self.api = RedditApi(subreddit)
        self.start_urls = [self.api.request_url()]

    def parse(self, response):
        first_id = [div.attrib['id'] for div in response.css("div[id^='t3']")][0]

        yield scrapy.Request(url=self.api.request_url(first_id), callback=self.parse_next)

    def parse_next(self, response):
        data = json.loads(response.text)
        next_postId = ''
        if len(data['postIds']) > 0:
            next_postId = data['postIds'][-1]

        for post in data['postIds']:
            if deep_key_test(data, ['posts', post, 'media', 'richtextContent', 'document']):
                # more powerfull equivalent to: `if data['posts'][post]['media']['richtextContent']['document']:`
                # it test each and every level instead of testing the last one and throwing an error if a key inbetween doen't exist

                texts = []
                for x in data['posts'][post]['media']['richtextContent']['document']:
                    # we can use data['posts'][post]['media']['richtextContent']['document'] without fear because we tested its existance right above

                    if deep_key_test(x, ['c', 0, 't']):
                        # equivalent to: `if x['c'] and len(x['c']) > 0 and ('t' in x['c'][0]):`
                        text = x['c'][0]['t']
                        texts.append(text)
                yield {
                    "postId" : post,
                    "text" : texts,
                    #"richtextContent" : data['posts'][post]['media']['richtextContent']['document']
                }

            else:
                yield {
                    "postId" : post,
                    "text" : None,
                    #"richtextContent" : None
                }

                self.total_results += 1 # DEBUG

        
        if next_postId:
            yield scrapy.Request(url=self.api.request_url(next_postId), callback=self.parse_next)

            
        print('total', self.total_results) # DEBUG

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(RedditSpider)
    process.start()