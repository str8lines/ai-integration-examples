import os

import requests

# server settings for connectivity
URL_BASE_SERVER = os.getenv("SERVER_URL", "https://secret.str8lines.com")
URL_ASSET = f'{URL_BASE_SERVER}/marketing_asset'
API_KEY = os.environ.get("API_KEY", None)


def headers():
    return {
        'Authorization': f'{API_KEY}'
    }


def create_asset():
    payload = {
        "prompt": "Professional photo of a woman wearing a sleek black button-down dress and black sandals, standing "
                  "confidently in a minimalist white studio. She has a short black hair in a stylish, tousled cut and "
                  "a subtle, natural makeup look. The image should be ultra-realistic, capturing fine details such as "
                  "the texture of the fabric, the shine on her shoes, and the natural expressions of her face",
        "retain_elements": "shirt,shoes",
        "gender": "",
        "category": ""
    }

    url = f"{URL_ASSET}"

    response = requests.post(url, json=payload, headers=headers())
    if not response.ok:
        print(response.status_code, response.content)
        raise ValueError('Unable to create asset', response.content)

    return response.json()


def upload_asset(asset_id: dict, file_name: str):
    url = f"{URL_ASSET}/{asset_id}/upload_single"
    with open(file_name, 'rb') as file:
        files = {'file': (file_name, file)}
        response = requests.post(url, files=files, headers=headers())

    print(response.status_code)
    print(response)


# create the marketing asset image
marketing_asset = create_asset()
upload_asset(marketing_asset['_id'], 'image.png')
