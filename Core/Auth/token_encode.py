import base64

def encode(api_key: str, api_secret):
    token = f"{api_key}:{api_secret}"
    encoded_token = base64.encode(token)
    auth_string = f"Basic {encoded_token}"
    return auth_string