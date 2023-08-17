from objects import *

# monsters stat_n
pseudoslimestat_n = stat_n(hp = 10.0, atk = 2, def_ = 0, hitrate = 100.0, dodgerate = 0.0,
                  critrate = 0.0, critres = 0.0, critdmg = 150.0, guardrate = 0.0, guarddmgdec = 30.0, brkthr = 0.0, speed = 1)

redslimestat_n = stat_n(hp = 25.0, atk = 4, def_ = 1, hitrate = 100.0, dodgerate = 0.0,
                  critrate = 5.0, critres = 0.0, critdmg = 180.0, guardrate = 0.0, guarddmgdec = 30.0, brkthr = 0.0, speed = 4)
"""
blueslimestat_n = stat_n(hp = 25.0, atk = 4, def_ = 1, hitrate = 100.0, dodgerate = 0.0,
                  critrate = 7.0, critres = 0.0, critdmg = 150.0, guardrate = 0.0, guarddmgdec = 30.0, brkthr = 0.0, speed = 4)
greenslimestat_n = stat_n(hp = 25.0, atk = 3, def_ = 2, hitrate = 100.0, dodgerate = 0.0,
                  critrate = 3.0, critres = 0.0, critdmg = 150.0, guardrate = 5.0, guarddmgdec = 30.0, brkthr = 0.0, speed = 3)
"""



# monsters stat_s


# monsters rewards
#pseudoslimereward = Reward(random.randint(1, 5), random.randint(1, 3))


# Equipment
# weapons
baseballbatstat_n = stat_n(hp = 0.0, atk = 3, def_ = 0, hitrate = 0.0, dodgerate = 0.0,
                  critrate = 5.0, critres = 0.0, critdmg = 0.0, guardrate = 0.0, guarddmgdec = 0.0, brkthr = 0.0, speed = 0)
baseballbatexplain = "전설의 대장장이 HK가 만들었다고 전해지는? 야구배트이다. 몬스터를 팰 때 매우 유용하다. 그 단단함은 이루 말할 수 없다. 다만, 본래 용도와 다르게 사용하면 무슨 일이 일어날지도 모른다.."
baseballbat = Weapon(name = "야구배트", type_= "전설의 무기", explanation = baseballbatexplain, element = "None", stat_n = baseballbatstat_n, stat_s = stat_s())

excaliburstat_n = stat_n(hp = 1000.0, atk = 500, def_ = 0, hitrate = 30.0, dodgerate = 0.0,
                  critrate = 20.0, critres = 0.0, critdmg = 50.0, guardrate = 0.0, guarddmgdec = 0.0, brkthr = 30.0, speed = 100)
excaliburstat_s = stat_s(1000, 20.0, 10.0)
excaliburexplain = "원탁의 아서왕이 사용했다고 전해지는 전설의 검이다. 앞을 가로막는 모든 것들을 벨 수 있다. 다만, 어떤 사정에 의하여 다량으로 배포되었다는 소문이 있다.. 설마 이것도 복제품?"
excalibur = Weapon(name = "엑스칼리버", type_= "검", explanation = excaliburexplain, element = "Light", stat_n = excaliburstat_n, stat_s = excaliburstat_s)
# armors
# accesories

# Field

