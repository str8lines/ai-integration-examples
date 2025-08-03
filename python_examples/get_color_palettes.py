import os

import requests

# server settings for connectivity
URL_BASE_SERVER = os.getenv("SERVER_URL", "https://secret.str8lines.com/api")
URL_COLLECTION = f'{URL_BASE_SERVER}/collection'
URL_COLOR = f'{URL_BASE_SERVER}/color'
API_KEY = os.environ.get("API_KEY", None)


def headers():
    """
    Generate headers for HTTP requests with authorization.

    Returns:
        dict: A dictionary containing the 'Authorization' key with an API key as its value.
    """
    return {
        'Authorization': f'{API_KEY}'
    }


def get_collections(query: str = None) -> list:
    query_params = 'filter_param=' + query

    url = f"{URL_COLLECTION}?{query_params}"

    response = requests.get(url, headers=headers())
    if not response.ok:
        print(response.status_code, response.content)
        raise ValueError('Unable to retrieve collections(s).', response.content)

    return response.json()


def get_color(_id: str = None) -> list:

    url = f"{URL_COLOR}/{_id}"

    response = requests.get(url, headers=headers())
    if not response.ok:
        print(response.status_code, response.content)
        raise ValueError('Unable to retrieve color.', response.content)

    return response.json()


# get all active palettes
collections = get_collections('active eq True')
palettes = []

# filter out palettes that do not have colors
for collection in collections:
    if 'color' in collection and len(collection['color']) > 0:
        palettes.append(collection)

print('Found palette(s):', palettes)
colors = []
for palette in palettes:
    for color in palette['color']:
        colors.append(get_color(color))

print('Found color(s):', colors)
