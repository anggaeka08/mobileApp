import json
import requests


def post_reports_link_to_slack():
    slack_url = "https://hooks.slack.com/services/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"

    # To generate report file add "> test.log" at end of pytest command for e.g. pytest -v > test.log
    report_url ='APP UI Automation Report : https://smssekuritas.bitbucket.io/siminvest-app-qa/allure-report/'

    bar_color = "#ff0000"
    data = {"color": bar_color,
            "title": "Test Report Url",
            "text": report_url}
    res = requests.post(url=slack_url, data=json.dumps(data), headers={"Content-type": "application/json"})
    print(res.text)


if __name__ == '__main__':
    post_reports_link_to_slack()
