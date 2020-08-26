import requests, json
import credentials

url = 'https://my.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/battle/gamer/Zigon%231491/matches/wz/start/0/end/0/details/'
response = requests.get(url,headers={'Cookie': f'ACT_SSO_COOKIE={credentials.ACT_SSO_COOKIE};'})
print(response)
gameData = json.loads(response.text)