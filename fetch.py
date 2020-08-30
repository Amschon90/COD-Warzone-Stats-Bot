import api_call
import user

def summaryStats(n, bnid):
    gameData = api_call.makecall(bnid)
    avgkd = gameData['data']['summary']['all']['kdRatio']
    sstats = SummaryClass(0,0,avgkd,0,0,0,0)
    for i in range(n):
        ps = gameData['data']['matches'][i]['playerStats']
        sstats.k += ps['kills']
        sstats.d += ps['deaths']
        sstats.gk += ps['gulagKills']
        sstats.gd += ps['gulagDeaths']
        sstats.dd += ps['damageDone']
        sstats.dt += ps['damageTaken']
    return sstats


class SummaryClass:
  def __init__(self, k, d, akd, gk, gd, dd, dt):
    self.k = k
    self.d = d
    self.akd = akd
    self.gk = gk
    self.gd = gd
    self.dd = dd
    self.dt = dt