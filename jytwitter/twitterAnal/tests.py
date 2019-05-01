import os, json
import redis
# Create your tests here.


redis_host = "localhost"
redis_port = 6379
redis_password = ""

def hello_redis():
    try:
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        r.set('a', '내 이름은 안주영!')
        r.set('a', '내 이름은 안주영ss!')

        msg = r.get('a')
        print(r.keys())
    except Exception as e:
        print(e)

hello_redis()