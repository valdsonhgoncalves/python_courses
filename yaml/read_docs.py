from unittest import loader
import yaml

with open('./yaml/data.yaml') as f:
    docs = yaml.load_all(f, Loader=yaml.FullLoader)
    for doc in docs:
        for k,v in doc.items():
            print(k, "->", v)