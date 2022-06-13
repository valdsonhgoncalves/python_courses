import yaml

users = [{'name': 'John Doe', 'occupation': 'gardener'},
         {'name':'Lucy Black', 'occupation': 'teacher'}]

with open('./yaml/users.yaml', 'w') as f:
    data = yaml.dump(users, f)