import json
import requests


def post_reports_to_slack():
    slack_url = "https://hooks.slack.com/services/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"

    # To generate report file add "> test.log" at end of pytest command for e.g. pytest -v > test.log
    test_report_file = 'test.log'  # Add report file name and address here
    # Open report file and read data
    with open(test_report_file, "r") as in_file:
        testdata = ""
        write = 0
        for line in in_file:
            if "short test summary info" in line:
                write = 1
            if write == 1:
                testdata = testdata + line

    # Set Slack Pass Fail bar indicator color according to test results
    if 'FAILED' in testdata:
        bar_color = "#ff0000"
        data = {"color": bar_color,
                "title": "Test Report",
                "text": testdata}
        res = requests.post(url=slack_url, data=json.dumps(data), headers={"Content-type": "application/json"})
        print(res)
    else:
        bar_color = "#ff0000"
        data = {"color": bar_color,
                "title": "Test Report",
                "text": testdata}
        res = requests.post(url=slack_url, data=json.dumps(data), headers={"Content-type": "application/json"})
        print(res)


if __name__ == '__main__':
    post_reports_to_slack()
