from typing import Optional

SUBREDDITS = {
    "Cooking",
    
}

# API urls
PAGE_URL = 'https://www.reddit.com/r/{subreddit}'
API_URL = 'https://gateway.reddit.com/desktopapi/v1/subreddits/{subreddit}?rtj=only&redditWebClient=web2x&app=web2x-client-production&allow_over18=&include=prefsSubreddit&after={post_id}&dist=12&layout=card&sort=hot'

class RedditApi:
    subreddit: str
    
    def __init__(self, subreddit: str):
        self.subreddit = subreddit

    def request_url(self, post_id: Optional[str]=None) -> str:
        if post_id:
            return API_URL.format(
                subreddit = self.subreddit,
                post_id   = post_id
            )

        else:
            return PAGE_URL.format(subreddit = self.subreddit)
