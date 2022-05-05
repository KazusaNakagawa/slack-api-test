import json
import logging
import os
import requests

from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(os.path.basename(__file__))
logging.basicConfig(
    level='INFO',
    filename='log/app.log',
    filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


def message(text='test message'):
    payload = {"text": f"{text}"}
    url = os.environ.get("SLACK_SAMPLE_MSG_APP")

    try:
        if 'Error' in text:
            raise Exception
        else:
            logger.info({'msg': 'Done'})

    except Exception as ex:
        r = requests.post(url=url, data=json.dumps(payload))
        logger.error({
            'ex': ex,
            'status': r.status_code,
            'msg': payload,
        })


if __name__ == '__main__':
    message('⚠️ Error: test Alert')
    message()
