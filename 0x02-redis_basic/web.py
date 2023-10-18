import requests
from functools import lru_cache
import time

@lru_cache(maxsize=None)
def get_page(url: str) -> str:
    d
    count_key = f"count:{url}"
    count = cache.get(count_key, 0)
    cache.set(count_key, count + 1, ex=10)

    
    page_key = f"page:{url}"
    page = cache.get(page_key)
    if page is None:
        time.sleep(2)  # Simulate a slow response
        page = requests.get(url).text
        cache.set(page_key, page, ex=10)

    return page

