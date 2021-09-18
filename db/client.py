import os
import yaml
from pymongo import MongoClient

config_path = os.path.dirname(__file__)[:-2] + "conf.yaml"
with open(config_path) as config:
    result = yaml.safe_load(config)
    HOST = result.get("host")
    PORT = result.get("port")
client = MongoClient(host=HOST, port=PORT)
