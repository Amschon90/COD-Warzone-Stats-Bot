import requests, json

url = 'https://my.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/battle/gamer/Zigon%231491/matches/wz/start/0/end/0/details/'
response = requests.get(url,headers={'Cookie': 'ACT_SSO_COOKIE=MjM1ODY0MTMyNTMxODMxNjY0NjoxNTk3OTgxNTU3Mjg0OjQxZjdlZTZjNDRjYjliY2JjMmM5YTk3MDE5MzNhNTVk;'})
print(response)
gameData = json.loads(response.text)

def lastFiveGames(g,gc):
  # Player Name, Last Five Games Summary
  # Kills:        Deaths: 
  # Downs:        Assists: 
  # Avg Dmg:      K/D/A: 
  # Gulag Record: 
  # Survival Time: 
  print(getStats(g,gc))

def lastTwentyGames():
  for i in range(len(g['matches'])):
    print("\n")
    print(f'Match #{i+1} (Time):')
    print('Kills: ' + str(g['matches'][i]['playerStats']['kills']))
    print('Deaths: ')
    print('Enemies Downed: ')
    print('Damage Done: ')

def getStats(g,gc):
  tk = 0
  for i in range(gc-1):
    tk += int(g['matches'][i]['playerStats']['kills'])
  return tk

g = gameData['data']
#print(g['matches'][0])

lastFiveGames(g,1)