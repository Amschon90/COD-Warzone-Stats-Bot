import api_call

gameData = api_call.gameData

# Format for message return:
  # Player Name, Last Five Games Summary
  # Kills:        Deaths: 
  # Avg Dmg:      Total Dmg:
  # Gulag Record: 
  # Survival Time: 

class GameStats:
  def __init__(self, pname, reqtype, kills, deaths, dmg, gk, gd, surtime):
    self.pname = pname
    self.reqtype = reqtype
    self.kills = kills
    self.deaths = deaths
    self.dmg = dmg
    self.gk = gk
    self.gd = gd
    self.surtime = surtime

g = gameData['data']
print(g['matches'][0])

stats = GameStats('Zigon','Last Game','10','14','1422','0','0','12:34')

statsprintout = (f'{stats.pname} - {stats.reqtype}\nKills: {stats.kills}     Deaths: {stats.deaths}\nDamage: {stats.dmg}  Gulag Score: {stats.gk}-{stats.gd}\nTotal Survival Time: {stats.surtime}')
