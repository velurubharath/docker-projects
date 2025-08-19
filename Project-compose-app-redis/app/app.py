from flask import Flask
import redis, os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST","redis")
r = redis.Redis(host=redis_host,port=6379,decode_responses=True)

app.route("/")
def home():
    count = r.incr("hits")
    return f"Hello from Bharath Docker's portfolio!. PageViews: {count}"

if __name__=="__main__":
    app.run(host="0.0.0.0" , port="5000")