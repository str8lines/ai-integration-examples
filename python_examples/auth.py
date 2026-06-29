"""
Shared authentication helper for the Straight Lines Platform examples.

Authentication uses a service account identified by a Client ID and a Secret Key.
These are exchanged once for a short-lived JWT via ``POST /signin/token``; that JWT
is then sent as ``Authorization: Bearer <jwt>`` on every API request.

Set the following environment variables before running any example:

    SERVER_URL   the dedicated server you want to access
    CLIENT_ID    the service account's Client ID (its account_id)
    SECRET_KEY   the service account's Secret Key (shown once on creation/rotation)
"""
import os

import requests

# server settings for connectivity
URL_BASE_SERVER = os.getenv("SERVER_URL", "https://secret.str8lines.com")

# service account credentials
CLIENT_ID = os.environ.get("CLIENT_ID", None)
SECRET_KEY = os.environ.get("SECRET_KEY", None)

# cached token so we only exchange credentials when needed
_token = None


def get_token(force_refresh: bool = False) -> str:
    """
    Exchange the Client ID / Secret Key for a JWT access token.

    The token is cached after the first call. Pass ``force_refresh=True`` to
    request a new token (for example, after the current one expires).

    Returns:
        str: A JWT to send as a Bearer token on subsequent requests.
    """
    global _token
    if _token is not None and not force_refresh:
        return _token

    response = requests.post(
        f"{URL_BASE_SERVER}/signin/token",
        json={"client_id": CLIENT_ID, "secret_key": SECRET_KEY},
        timeout=30,
    )
    if not response.ok:
        print(response.status_code, response.content)
        raise ValueError('Unable to obtain access token.', response.content)

    _token = response.json()
    if not _token:
        # the endpoint returns null when the credentials are invalid
        raise ValueError('Invalid Client ID or Secret Key.')

    return _token


def headers() -> dict:
    """
    Generate headers for HTTP requests with Bearer authorization.

    Returns:
        dict: A dictionary containing the 'Authorization' key with a Bearer JWT.
    """
    return {
        'Authorization': f'Bearer {get_token()}'
    }


def authorized_request(method: str, url: str, **kwargs) -> requests.Response:
    """
    Make an authorized request, refreshing the token once on a 401 response.

    Args:
        method: HTTP method, e.g. 'GET' or 'POST'.
        url: Fully-qualified request URL.
        **kwargs: Passed through to ``requests.request`` (json, files, params, ...).

    Returns:
        requests.Response: The response from the API.
    """
    response = requests.request(method, url, headers=headers(), **kwargs)
    if response.status_code == 401:
        # token likely expired -> refresh and retry once
        get_token(force_refresh=True)
        response = requests.request(method, url, headers=headers(), **kwargs)
    return response
