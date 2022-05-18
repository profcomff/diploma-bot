import requests
import configparser
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from google_drive.google_drive_utils import upload_file_to_drive, get_service
from google_drive.token import get_token_file

config = configparser.ConfigParser()
config.read('auth.ini')

GROUP_ID = config['auth_vk']['group_id']
GROUP_TOKEN = config['auth_vk']['group_token']
DOWNLOAD_TAG = config['tags']['test_tag']
API_VERSION = '5.131'

vk_session = VkApi(token=GROUP_TOKEN, api_version=API_VERSION)  # Auth with community token
longpoll = VkBotLongPoll(vk_session, group_id=GROUP_ID)
vk_api = vk_session.get_api()
drive_service = get_service('token.json')


def process_event(event, cache=True):
    if event.type == VkBotEventType.MESSAGE_NEW and event.from_user:
        if DOWNLOAD_TAG in (event.message['text']).lower().split() and event.message.attachments:
            title = event.message.attachments[0]['doc']['title']
            url = event.message.attachments[0]['doc']['url']
            content = requests.get(url).content
            if cache:
                fmt = title.split('.')[1]
                file = f'cache.{fmt}'
                with open(file, 'wb') as cachefile:
                    cachefile.write(content)
                print(f'File: {title} uploaded to cache')
                upload_file_to_drive(drive_service, file=file, name=title)
            else:
                with open(title, 'wb') as file:
                    file.write(content)
                print(f'File: {title} uploaded to server')
                upload_file_to_drive(drive_service, title)


def chat_loop():
    while True:
        try:
            for event in longpoll.listen():
                process_event(event)
        except BaseException as e:
            raise e


if __name__ == '__main__':
    chat_loop()
