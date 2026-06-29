import requests

from auth import URL_BASE_SERVER, authorized_request

# server settings for connectivity
URL_IMAGE = f'{URL_BASE_SERVER}/image'


def download_images(_images=None):
    # download the file for each image
    if _images is None:
        _images = []
    for image in _images:
        if 'url' in image and image.get('url', None) is not None:
            r = requests.get(image.get('url'), stream=True)
            if r.status_code == 200:
                # this will just save to current directory
                with open(image.get('file_name_os'), 'wb') as f:
                    for chunk in r.iter_content(1024):
                        f.write(chunk)


def get_pending_images(query: str = None) -> list:
    # send to closet is a field selected by the end user
    # closet_status is a field populated by the integration
    query_params = 'filter_param=' + query

    url = f"{URL_IMAGE}?{query_params}"

    response = authorized_request('GET', url)
    if not response.ok:
        print(response.status_code, response.content)
        raise ValueError('Unable to retrieve image(s).', response.content)

    return response.json()


# get the images that are ready to send
images = get_pending_images('send_to_closet eq Yes and closet_status ne sent and is_option eq False')

download_images(images)