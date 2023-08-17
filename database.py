from objects import *

# monsters stat_n
pseudoslimestat_n = stat_n(hp = 10.0, atk = 2, def_ = 0, hitrate = 100.0, dodgerate = 0.0,
                  critrate = 0.0, critres = 0.0, critdmg = 150.0, guardrate = 0.0, guarddmgdec = 30.0, brkthr = 0.0, speed = 1)

# monsters stat_s


# monsters rewards
#pseudoslimereward = Reward(random.randint(1, 5), random.randint(1, 3))


# Equipment
# weapons
baseballbatstat_n = stat_n(hp = 0.0, atk = 3, def_ = 0, hitrate = 0.0, dodgerate = 0.0,
                  critrate = 5.0, critres = 0.0, critdmg = 0.0, guardrate = 0.0, guarddmgdec = 0.0, brkthr = 0.0, speed = 0)
baseballbat = Weapon(name = "야구배트", type_= "전설의 무기", element = "None", stat_n = baseballbatstat_n, stat_s = stat_s())
# armors
# accesories

# Field

