#from objects import *
from database import *

player = Player(1, "Novice")
player.playerinfo()
print('')
monster1 = Monster(1, "Normal", pseudoslimestat_n)
monster1.monsterinfo()

battlepve = BattlePVE(player, monster1)
if battlepve.battle():
    print("Player wins.")
else:
    print("Monster wins.")
