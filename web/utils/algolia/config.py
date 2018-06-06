import os
from algoliasearch import algoliasearch

client = algoliasearch.Client(os.environ.get('KEY_APP_ALGOLIA'), os.environ.get('API_KEY_ALGOLIA'))