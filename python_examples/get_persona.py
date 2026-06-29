from auth import URL_BASE_SERVER, authorized_request

# server settings for connectivity
URL_PERSONA = f'{URL_BASE_SERVER}/persona'


def get_persona_by_name(name: str) -> dict:
    # the name is wrapped in double quotes so values containing spaces (or the
    # words 'and'/'or') are matched as a single literal value
    query_params = {'filter_param': f'name eq "{name}"'}

    response = authorized_request('GET', URL_PERSONA, params=query_params)
    if not response.ok:
        print(response.status_code, response.content)
        raise ValueError('Unable to retrieve persona(s).', response.content)

    personas = response.json()
    # the persona list endpoint returns an array; return the first match, if any
    return personas[0] if personas else None


# look up a persona by its name
persona = get_persona_by_name('Studio Woman')

if persona is None:
    print('No persona found with the specified name.')
else:
    print('Found persona:', persona)
