import os
import re
import requests
from requests.auth import HTTPBasicAuth

def sync_app():
    _android_app = requests.get("https://api.appcenter.ms/v0.1/apps/sms.sekuritas/SimInvest/releases/latest",
                                headers={"X-Api-Token": "9363f95eb552d33054cd59db6f24e559778a08c0"})
    _ios_app = requests.get("https://api.appcenter.ms/v0.1/apps/sms.sekuritas/SimInvest-1/releases/latest",
                            headers={"X-Api-Token": "9363f95eb552d33054cd59db6f24e559778a08c0"})
    print(_android_app.json())
    print(_ios_app.json())

    ios_app = _ios_app.json()
    android_app = _android_app.json()
    _bs_ios = requests.post("https://api-cloud.browserstack.com/app-automate/upload",
                            auth=HTTPBasicAuth('manish_dxNy3J', 'VD3gsZgUhKyYYmvgiz7b'),
                            data={"url": ios_app["download_url"]})
    _bs_android = requests.post("https://api-cloud.browserstack.com/app-automate/upload",
                                auth=HTTPBasicAuth('manish_dxNy3J', 'VD3gsZgUhKyYYmvgiz7b'),
                                data={"url": android_app["download_url"]})

    bs_ios = _bs_ios.json()
    ios_app_url = bs_ios['app_url']
    bs_android = _bs_android.json()
    android_app_url = bs_android['app_url']
    return ios_app_url, android_app_url

def update_app_url_cap(url,path):
    file_path = os.path.abspath(path)
    with open(file_path , 'r+') as f:
        content = f.read()
        match = re.sub(r'"app":.*',url , content)
        f.seek(0)
        f.truncate()
        f.write(match)
        f.close()

def update_url_in_cap_file():
    ios_app_url, android_app_url = sync_app()

    # update url in android cap file
    final_app_url_android = f'"app": "{android_app_url}",'
    print(final_app_url_android)
    path_android = '..\\cap_files\\bs_android_cap.py'
    update_app_url_cap(final_app_url_android, path_android)

    #update url in ios cap file
    final_app_url_ios = f'"app": "{ios_app_url}",'
    print(final_app_url_ios)
    path_ios = '..\\cap_files\\bs_ios_cap.py'
    update_app_url_cap(final_app_url_ios, path_ios)

update_url_in_cap_file()