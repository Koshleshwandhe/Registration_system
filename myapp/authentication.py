import base64
def generate_auth_token(id, password):
    credentials = f"{id}:{password}"
    token = base64.b64encode(credentials.encode()).decode()
    return token