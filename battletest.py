#from objects import *
from database import *

player = Player(1, "Novice")
player.playerinfo()
player.Equip(baseballbat)
player.playerinfo()
print('')
monster1 = Monster(name = "pseudoslime", lv = 1, type = "Normal", element = "None", reward = Reward(random.randint(1, 5), random.randint(1, 3)), stat_n = pseudoslimestat_n)
monster1.monsterinfo()

battlepve = BattlePVE(player, monster1)
battlepve.battle()

#player.playerinfo()