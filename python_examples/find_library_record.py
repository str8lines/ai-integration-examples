from auth import URL_BASE_SERVER, authorized_request


def find_library_record_by_name(library_key: str, name: str, asset_type: str = None) -> dict:
    """
    Find a single record in a library by its name (and optionally asset_type).

    Args:
        library_key: The library to search, e.g. 'supporting_assets'.
        name: The exact record name to match.
        asset_type: Optional asset_type to further restrict the match,
            e.g. 'base_model' or 'supporting_product'.

    Returns:
        dict: The first matching record, or None if nothing matches.
    """
    # names are wrapped in double quotes so values with spaces (or the words
    # 'and'/'or') are matched as a single literal value
    filter_param = f'name eq "{name}"'
    if asset_type:
        filter_param += f' and asset_type eq "{asset_type}"'

    url = f"{URL_BASE_SERVER}/libraries/{library_key}/items"

    response = authorized_request('GET', url, params={'filter_param': filter_param})
    if not response.ok:
        print(response.status_code, response.content)
        raise ValueError('Unable to retrieve library record(s).', response.content)

    records = response.json()
    return records[0] if records else None


if __name__ == '__main__':
    # find a base model in the supporting_assets library by name
    record = find_library_record_by_name('supporting_assets', 'Studio Model', 'base_model')

    if record is None:
        print('No library record found with the specified name.')
    else:
        print('Found library record:', record)
