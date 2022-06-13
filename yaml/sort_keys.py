from re import T
from numpy import sort
import yaml

with open('./yaml/items.yaml') as f:
    data =  yaml.load(f, Loader=yaml.FullLoader)
    print(data)
    
    sorted = yaml.dump(data, sort_keys=True)
    print(sorted)