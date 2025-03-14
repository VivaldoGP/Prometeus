from requests import post, HTTPError, ConnectionError, Timeout


def get_access_token(username: str,
                     password: str,
                     token_url: str = "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token") -> str:
    creds = {
        'client_id': 'cdse-public',
        'username': username,
        'password': password,
        'grant_type': 'password'
    }

    try:
        response = post(token_url, data=creds, timeout=10)
        response.raise_for_status()

    except HTTPError as e:
        if response.status_code == 401:
            raise Exception("Invalid credentials")
        raise Exception(f"Error HTTP {response.status_code}: {e}")

    except (ConnectionError, Timeout):
        raise Exception("Connection error")

    except Exception as e:
        raise Exception(f"Failed to get access token: {e}")

    return response.json()['access_token']