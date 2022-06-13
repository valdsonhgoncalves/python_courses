from importlib.abc import Loader
import yaml

with open('./yaml/items.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data['raincoat'])
