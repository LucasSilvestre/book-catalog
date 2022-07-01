import redis

from typing import Union, Optional, Any

from app.settings import CACHE_URL


class Cache:
    def __init__(self,
                 url):
        try:
            self.client = redis.Redis.from_url(f"{url}", health_check_interval=30)
            self.client.ping()
        except redis.ConnectionError as error:
            raise Exception(f"Error trying to connect redis instance: {url}") from error

    def get_value(self,
                  key: str) -> str:
        return self.client.get(key)

    def set_value(self,
                  key: str,
                  value: Union[int, str],
                  ttl: int = None) -> Optional[bool]:
        return self.client.set(key, value, ex=ttl)

    def __del__(self):
        self.client.close()


cache = Cache(CACHE_URL)
