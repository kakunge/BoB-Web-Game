#from objects import *
from database import *

player = Player(1, "Novice")
player.playerinfo()
playerp = player
player.Equip(baseballbat)
player.playerinfo()
playerp.playerinfo()

#"""
print('----------------')
monster1 = Monster(name = "pseudoslime", lv = 1, type_ = "Normal", element = "None", reward = Reward(random.randint(1, 5), random.randint(1, 3)), stat_n = pseudoslimestat_n)
monster1.monsterinfo()

battlepve = BattlePVE(player, monster1)
battlepve.battle()
#"""
playerp.playerinfo()

monster1 = Monster(name = "pseudoslime", lv = 1, type_ = "Normal", element = "None", reward = Reward(random.randint(1, 5), random.randint(1, 3)), stat_n = pseudoslimestat_n)
battlepve = BattlePVE(player, monster1)
battlepve.battle()
playerp.playerinfo()