import os
import googleapiclient.discovery
from google_drive.service import get_service
from googleapiclient.http import MediaFileUpload


def upload_file_to_drive(service: googleapiclient.discovery.Resource,
                         file: str, name: str) -> str:
    """
    Generates POST request for one file
    Returns file id on a Google Drive
    """
    file_metadata = {'name': name}
    media = MediaFileUpload(file)
    status = service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
    return status.get('id')


def upload_test_file():
    file = '../rak.pdf'
    if os.path.exists(file):
        service = get_service('../token.json')
        print(upload_file_to_drive(service, file))
    else:
        print('test file path is not valid')


if __name__ == '__main__':
    upload_test_file()

