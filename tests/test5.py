import redis

# Connect to Redis server
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Test connection
try:
    r.ping()
    print("Connected to Redis successfully!")
except redis.ConnectionError:
    print("Failed to connect to Redis.")
