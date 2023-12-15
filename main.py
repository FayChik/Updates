from pyupdater.client import Client
from client_config import ClientConfig

APP_NAME = 'Super App'
APP_VERSION = '1.2.0'

ASSET_NAME = 'ffmpeg'
ASSET_VERSION = '2.3.2'


def print_status_info(info):
    total = info.get(u'total')
    downloaded = info.get(u'downloaded')
    status = info.get(u'status')
    print(downloaded, total, status)


client = Client(ClientConfig())
client.refresh()

client.add_progress_hook(print_status_info)

app_update = client.update_check(APP_NAME, APP_VERSION)

if app_update is not None:
    app_update.download()
if app_update.is_downloaded():
    app_update.extract_overwrite()
