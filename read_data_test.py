train_file_path = 'train.json'

import json

train_data_file = open(train_file_path)
train_data = json.load(train_data_file)


print('number of papers in train data:', len(train_data))


authors = train_data["0"]['author']
year = train_data["0"]['year']
venue = train_data["0"]['venue']
keywords = train_data["0"]['keywords']

print('about paper 0:')
print('authors', authors)
print('year', year)
print('venue', venue)
print('keywords', keywords)


