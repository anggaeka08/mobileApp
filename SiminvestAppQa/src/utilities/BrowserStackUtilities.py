import requests
from requests.auth import HTTPBasicAuth


def sync_app():
    _android_app = requests.get("https://api.appcenter.ms/v0.1/apps/sms.sekuritas/SimInvest/releases/latest",
                                headers={"X-Api-Token": "9363f95eb552d33054cd59db6f24e559778a08c0"})
    _ios_app = requests.get("https://api.appcenter.ms/v0.1/apps/sms.sekuritas/SimInvest-1/releases/latest",
                            headers={"X-Api-Token": "9363f95eb552d33054cd59db6f24e559778a08c0"})

    ios_app = _ios_app.json()
    android_app = _android_app.json()
    _bs_ios = requests.post("https://api-cloud.browserstack.com/app-automate/upload",
                            auth=HTTPBasicAuth('manish_dxNy3J', 'VD3gsZgUhKyYYmvgiz7b'),
                            data={"url": ios_app["download_url"]})
    _bs_android = requests.post("https://api-cloud.browserstack.com/app-automate/upload",
                                auth=HTTPBasicAuth('manish_dxNy3J', 'VD3gsZgUhKyYYmvgiz7b'),
                                data={"url": android_app["download_url"]})

    bs_ios = _bs_ios.json()
    bs_android = _bs_android.json()
    
