from auth import URL_BASE_SERVER, authorized_request

# server settings for connectivity
URL_WORKFLOW = f'{URL_BASE_SERVER}/workflow'


def search_workflows_by_name(name: str) -> list:
    # 'contains' is a case-insensitive partial match, so this searches for any
    # workflow whose name contains the given text. Use 'name eq "<name>"' for an
    # exact match instead.
    query_params = {'filter_param': f'name contains "{name}"'}

    response = authorized_request('GET', URL_WORKFLOW, params=query_params)
    if not response.ok:
        print(response.status_code, response.content)
        raise ValueError('Unable to retrieve workflow(s).', response.content)

    return response.json()


def get_workflow_by_name(name: str) -> dict:
    # 'eq' is an exact match; returns the first matching workflow, or None
    query_params = {'filter_param': f'name eq "{name}"'}

    response = authorized_request('GET', URL_WORKFLOW, params=query_params)
    if not response.ok:
        print(response.status_code, response.content)
        raise ValueError('Unable to retrieve workflow(s).', response.content)

    workflows = response.json()
    return workflows[0] if workflows else None


if __name__ == '__main__':
    # search for AI workflows by name
    workflows = search_workflows_by_name('Outfit')

    if not workflows:
        print('No workflow found matching the specified name.')
    else:
        print(f'Found {len(workflows)} workflow(s):', workflows)
