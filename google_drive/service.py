import googleapiclient.discovery
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build, Resource


def get_service(token_file: str) -> googleapiclient.discovery.Resource:
    creds = Credentials.from_authorized_user_file(token_file)
    return build('drive', 'v3', credentials=creds)


if __name__ == '__main__':
    print(get_service('../token.json'))
