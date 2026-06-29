from auth import URL_BASE_SERVER, authorized_request


def create_scenario(asset_id: str, fields: dict) -> dict:
    """
    Create a scenario under a parent marketing asset.

    Args:
        asset_id: The '_id' of the parent marketing asset.
        fields: The scenario field values, for example:
            {
                'prompt': '...',
                'model': '<ai model id>',
                'workflow_id': '<workflow id>',
                'width': 1024,
                'height': 1024,
                'num_images': 1,
                'scenario_type': '3d_to_real',
                'input_file_ids': [
                    {'_id': '<file id>', 'asset_type': 'detail'},
                    {'_id': '<file id>', 'asset_type': 'base_model'},
                    {'_id': '<file id>', 'asset_type': 'supporting_product'},
                ],
            }

    Returns:
        dict: The created scenario.
    """
    url = f"{URL_BASE_SERVER}/marketing_asset/{asset_id}/scenario"

    response = authorized_request('POST', url, json=fields)
    if not response.ok:
        print(response.status_code, response.content)
        raise ValueError('Unable to create scenario.', response.content)

    return response.json()


if __name__ == '__main__':
    # create a simple scenario under an existing marketing asset
    scenario = create_scenario('<marketing_asset_id>', {
        'prompt': 'A studio product photo',
        'model': '<ai model id>',
        'width': 1024,
        'height': 1024,
        'num_images': 1,
        'scenario_type': '3d_to_real',
        'input_file_ids': [],
    })
    print('Created scenario id:', scenario.get('_id'))
