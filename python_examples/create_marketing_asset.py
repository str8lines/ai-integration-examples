from auth import URL_BASE_SERVER, authorized_request

# server settings for connectivity
URL_ASSET = f'{URL_BASE_SERVER}/marketing_asset'


def create_marketing_asset(fields: dict) -> dict:
    """
    Create a parent marketing asset.

    The fields dict is sent as-is, so any customer-specific custom fields
    (configured per environment) can be set here.

    Args:
        fields: The field values to set on the new marketing asset.

    Returns:
        dict: The created marketing asset, including its '_id'.
    """
    response = authorized_request('POST', URL_ASSET, json=fields)
    if not response.ok:
        print(response.status_code, response.content)
        raise ValueError('Unable to create marketing asset.', response.content)

    return response.json()


if __name__ == '__main__':
    # create a marketing asset, setting customer-specific custom fields
    asset = create_marketing_asset({'fieldA': 'example-a', 'fieldB': 'example-b'})
    print('Created marketing asset id:', asset.get('_id'))
