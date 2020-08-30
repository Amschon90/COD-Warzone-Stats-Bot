import api_call
import user
import gameModes
import weapons

m = gameModes.gameModes

w = weapons.weapons

def summaryStats(n, bnid):
    gameData = api_call.makecall(bnid)
    avgkd = gameData['data']['summary']['all']['kdRatio']
    sstats = SummaryClass(0,0,0,0,0,0,avgkd,0,0,0,0,0,0,0)
    for i in range(n):
        ps = gameData['data']['matches'][i]['playerStats']
        sstats.k += ps['kills']
        sstats.d += ps['deaths']
        sstats.gk += ps['gulagKills']
        sstats.gd += ps['gulagDeaths']
        sstats.dd += ps['damageDone']
        sstats.dt += ps['damageTaken']
    return sstats

def detailStats(g, bnid):
  gameData = api_call.makecall(bnid)
  dstats = SummaryClass(0,0,0,0,0,0,0,0,0,0,0,0,0,0)
  gd = gameData['data']['matches'][g]
  dstats.gt = m[gd['mode']] #
  dstats.mt = gd['utcStartSeconds'] #
  dstats.sc = gd['playerStats']['score'] #
  dstats.gp = gd['playerStats'].get(str(['teamPlacement'])) #
  dstats.k = gd['playerStats']['kills']
  dstats.d = gd['playerStats']['deaths']
  dstats.gk = bool(gd['playerStats']['gulagKills'])
  dstats.dd = gd['playerStats']['damageDone']
  dstats.dt = gd['playerStats']['damageTaken']
  dstats.pg = w[gd['player']['loadout'][0]['primaryWeapon']['name']] #
  dstats.sg = w[gd['player']['loadout'][0]['secondaryWeapon']['name']] #
  dstats.lo = True #
  return dstats

class SummaryClass:
  def __init__(self, gt, mt, sc, gp, k, d, akd, gk, gd, dd, dt, pg, sg, lo):
    self.gt = gt
    self.mt = mt
    self.sc = sc
    self.gp = gp
    self.k = k
    self.d = d
    self.akd = akd
    self.gk = gk
    self.gd = gd
    self.dd = dd
    self.dt = dt
    self.pg = pg
    self.sg = sg
    self.lo = lo

t = detailStats(4, 'Zigon%231491')
print(t.gt)
print(t.mt)
print(t.sc)
print(t.gp)
print(t.gk)
print(t.pg)
print(t.sg)
print(t.lo)