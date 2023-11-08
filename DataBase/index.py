import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

i = 0
while i <= 100000:
  i += 1
  print(i)
  redis_client.set(i, 'Data')  

test = redis_client.dbsize()
print(test)

# value = redis_client.get('my_key')

# if value is not None:
#   value = value.decode('utf-8')

# print(f'Retrieved value: {value}')

redis_client.connection_pool.disconnect()