from auth import URL_BASE_SERVER, authorized_request

# server settings for connectivity
URL_PALETTE = f'{URL_BASE_SERVER}/palette'


def get_palettes(query: str = None) -> list:
    query_params = 'filter_param=' + query if query else ''

    url = f"{URL_PALETTE}?{query_params}"

    response = authorized_request('GET', url)
    if not response.ok:
        print(response.status_code, response.content)
        raise ValueError('Unable to retrieve palette(s).', response.content)

    return response.json()


def get_palette_items(palette_id: str = None) -> list:
    # for a colors-scoped palette these items are the resolved color records
    url = f"{URL_PALETTE}/{palette_id}/items"

    response = authorized_request('GET', url)
    if not response.ok:
        print(response.status_code, response.content)
        raise ValueError('Unable to retrieve palette items.', response.content)

    return response.json()


# get all color palettes (scope can also be 'prints' or 'materials')
palettes = get_palettes('scope eq colors')

print('Found palette(s):', palettes)

# each palette's items endpoint returns the resolved color records directly
colors = []
for palette in palettes:
    colors.extend(get_palette_items(palette['_id']))

print('Found color(s):', colors)
