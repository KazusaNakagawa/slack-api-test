import json
import logging
import os
import pathlib
import requests

from dotenv import load_dotenv

load_dotenv()

LOG_DIR = './log'
USER_ID = os.environ.get("USER_ID")

"""
ref: https://api.slack.com/apps/<APP ID>/incoming-webhooks?
naming rule: SLACK_Webhook_URL_<channel name>
"""
# SLACK_Webhook_URL_RANDOM = os.environ.get("SLACK_Webhook_URL_RANDOM")
# SLACK_Webhook_URL_SAMPLE_MSG_APP = os.environ.get("SLACK_Webhook_URL_SAMPLE_MSG_APP")
SLACK_Webhook_URL_ERROR_TEST = os.environ.get("SLACK_Webhook_URL_ERROR_TEST")

if not pathlib.Path(LOG_DIR).exists():
    pathlib.Path(LOG_DIR).mkdir()

logger = logging.getLogger(os.path.basename(__file__))
logging.basicConfig(
    level='INFO',
    filename=f"{LOG_DIR}/app.log",
    filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


def message(text='test message'):
    payload = {'text': f"{text}"}
    url = SLACK_Webhook_URL_ERROR_TEST

    try:
        if 'Alert' in text:
            r = requests.post(url=url, data=json.dumps(payload))
            logger.info({
                'status': r.status_code,
                'msg': payload,
            })
        else:
            logger.info({'msg': 'Done'})

    except Exception as ex:
        logger.error({'ex': ex})


if __name__ == '__main__':
    message('⚠️ <!channel> Error: test Alert')
    message('⚠️ <!here> Error: test Alert')
    message(f"⚠️ :frowning: <@{USER_ID}> Error: test Alert")
    message()
