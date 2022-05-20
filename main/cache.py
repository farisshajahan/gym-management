import redis
from django.conf import settings


class Cache:
    def __init__(self):
        self.redis = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_BLACKLIST_DB,
        )

    def add_key(self, key, value):
        self.redis.set(key, value)

    def set_ttl(self, key, time_left):
        if self.redis.get(key) is not None:
            self.redis.expire(key, time_left)

    def exists(self, key):
        return bool(self.redis.get(key))

    def get_value(self, key):
        return self.redis.get(key)


cache = Cache()
