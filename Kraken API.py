#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

pair = 'XBTUSD' # pair to retrieve data for
url = f'https://api.kraken.com/0/public/Depth?pair={pair}' # API endpoint

response = requests.get(url) # make request to API endpoint
data = response.json() # parse response as JSON

bids = data['result'][pair]['bids'] # extract bids from the response data

print(bids) # print the bids


# In[2]:


import requests

pair = 'XBTUSD' # pair to retrieve data for
url = f'https://api.kraken.com/0/public/Depth?pair={pair}' # API endpoint

response = requests.get(url) # make request to API endpoint

if response.status_code != 200:
    raise Exception(f'Request failed with status code {response.status_code}')

data = response.json() # parse response as JSON

if 'error' in data:
    raise Exception(data['error'])

if 'result' not in data or pair not in data['result']:
    raise Exception(f'Pair {pair} not found in response data')

bids = data['result'][pair]['bids'] # extract bids from the response data

print(bids) # print the bids


# In[3]:


import requests

pair = 'XBTUSD' # pair to retrieve data for
url = f'https://api.kraken.com/0/public/Depth?pair={pair}' # API endpoint

response = requests.get(url) # make request to API endpoint

if response.status_code != 200:
    raise Exception(f'Request failed with status code {response.status_code}')

data = response.json() # parse response as JSON

if isinstance(data, list) and not data:
    raise Exception('Response data is empty')

if 'error' in data:
    raise Exception(data['error'])

if not data.get('result') or not data['result'].get(pair):
    raise Exception(f'Pair {pair} not found in response data')

bids = data['result'][pair]['bids'] # extract bids from the response data

print(bids) # print the bids


# In[ ]:




