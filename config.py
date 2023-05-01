import secrets

SECRET_KEY = secrets.token_hex(16)
STATIC_FOLDER = 'static'
STATIC_URL_PATH = '/static'

print(SECRET_KEY)