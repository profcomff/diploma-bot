import os.path
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/drive']


def get_token_file():
    if os.path.exists('../token.json'):
        print('Account token already exsists. Overwriting....')
    flow = InstalledAppFlow.from_client_secrets_file(
        'google_drive/credentials.json', SCOPES)
    creds = flow.run_local_server(port=8000)
    with open('/token.json', 'w') as token:
        token.write(creds.to_json())


if __name__ == '__main__':
    get_token_file()
