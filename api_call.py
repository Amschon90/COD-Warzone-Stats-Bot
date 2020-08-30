import requests, json, os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('ACT_SSO_COOKIE')

def makecall(bnid):
    url = f'https://my.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/battle/gamer/{bnid}/matches/wz/start/0/end/0/details/'
    response = requests.get(url,headers={'Cookie': f'ACT_SSO_COOKIE={TOKEN};'})
    print(response)
    return json.loads(response.text)