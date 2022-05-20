import os
import googleapiclient.discovery
from google_drive.service import get_service
from googleapiclient.http import MediaFileUpload
from typing import Optional


def upload_file_to_drive(service_obj: googleapiclient.discovery.Resource,
                         file: str, file_name: str = None, folder_name: str = None) -> str:
    """
    :param file_name:
    :param service_obj:
    :param file:
    :param folder_name:
    :return:
    """
    file_metadata = {'name': file,
                     'parents': []}
    if file_name:
        file_metadata['name'] = file_name
    if folder_name:
        file_metadata['parents'].append(create_folder(service_obj, folder_name))

    media = MediaFileUpload(file)
    status = service_obj.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    return status.get('id')


def find_folder(service_obj: googleapiclient.discovery.Resource,
                folder_name: str) -> Optional[str]:
    """
    Finds a certain folder on a Google Drive
    :param service_obj: googleapi service obj
    :param folder_name: name of the folder
    :return: folder id or None if not exists
    """
    folders = service_obj.files().list().execute().get('files', [])
    for folder in folders:
        if folder['name'] == folder_name:
            return folder['id']
    return None


def create_folder(service_obj: googleapiclient.discovery.Resource,
                  name: str) -> str:
    """
    Creates an empty folder on a Google Drive
    :param service_obj: googleapi service obj
    :param name: name of the folder
    :return: id
    """
    folder_id = find_folder(service_obj, name)
    if folder_id:
        return folder_id
    file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    file = service_obj.files().create(body=file_metadata,
                                      fields='id').execute()
    print(f'folder {name} created')
    return file.get('id')


def upload_test_file():
    file = '../rak.pdf'
    if os.path.exists(file):
        service_obj = get_service('../token.json')
        print(upload_file_to_drive(service_obj, file, file))
    else:
        print('test file path is not valid')


if __name__ == '__main__':
    upload_test_file()
