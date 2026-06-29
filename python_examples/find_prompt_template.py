from auth import URL_BASE_SERVER, authorized_request

# server settings for connectivity
URL_PROMPT_TEMPLATE = f'{URL_BASE_SERVER}/prompt_template'


def find_prompt_template_by_name(name: str) -> dict:
    """
    Find a prompt template by its name.

    The returned template's 'prompt_text' is the prompt to use, for example as a
    scenario's prompt.

    Args:
        name: The exact template name to match.

    Returns:
        dict: The first matching prompt template, or None if nothing matches.
    """
    # the name is wrapped in double quotes so values with spaces (or the words
    # 'and'/'or') are matched as a single literal value
    query_params = {'filter_param': f'name eq "{name}"'}

    response = authorized_request('GET', URL_PROMPT_TEMPLATE, params=query_params)
    if not response.ok:
        print(response.status_code, response.content)
        raise ValueError('Unable to retrieve prompt template(s).', response.content)

    templates = response.json()
    return templates[0] if templates else None


if __name__ == '__main__':
    # look up a prompt template by name and print its prompt text
    template = find_prompt_template_by_name('Studio Seamless - Pure White')

    if template is None:
        print('No prompt template found with the specified name.')
    else:
        print('Found prompt template:', template)
        print('Prompt text:', template.get('prompt_text'))
