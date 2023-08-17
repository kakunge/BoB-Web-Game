import random

class stat_n:
    def __init__(self, element = "None", hp = 20.0, atk = 2, def_ = 1, hitrate = 100.0, dodgerate = 5.0,
                  critrate = 5.0, critres = 0.0, critdmg = 150.0, guardrate = 3.0, guarddmgdec = 30.0, brkthr = 0.0, speed = 10): # player's base stats
        self.atkelement_ = element
        self.defelement_ = element
        self.hp_ = hp
        self.atk_ = atk
        self.def_ = def_
        self.hr_ = hitrate
        self.dr_ = dodgerate
        self.cr_ = critrate
        self.crr_ = critres
        self.crd_ = critdmg
        self.gr_ = guardrate
        self.gdd_ = guarddmgdec
        self.brk_ = brkthr
        self.speed_ = speed

class stat_s:
    def __init__(self, elemforce = 0, givedmginc = 0.0, getdmgdec = 0.0): # base stats
        self.eforce_ = elemforce
        self.givedmginc_ = givedmginc
        self.getdmgdec_ = getdmgdec


class Monster():
    def __init__(self, lv, type_, stat_n: stat_n, stat_s: stat_s):
        self.lv_ = lv
        self.type_ = type_ # normal, elite, boss
        self.stat_n_ = stat_n
        self.stat_s_ = stat_s

class Player:
    def __init__(self, lv, class_, stat_n: stat_n, stat_s: stat_s):
        self.lv_ = lv
        self.class_ = class_ # Warrior, etc.
        self.stat_n_ = stat_n
        self.stat_s_ = stat_s
        

class BattlePVE:
    def __init__(self, player: Player, monster: Monster):
        self.player = player
        self.monster = monster
        self.pstat_n_ = player.stat_n_
        self.pstat_s_ = player.stat_s_
        self.mstat_n_ = monster.stat_n_
        self.mstat_s_ = monster.stat_s_
    
    def attacktop(self):
        dmg = (float)(self.mstat_n_.atk_ - self.pstat_n_.def_)
        if (self.mstat_n_.hr_ - self.pstat_n_.dr_) - random.randint(1, 100) < 0:
            # missed, dmg 0
            return 0.0
        if (self.pstat_n_.gr_ - self.mstat_n_.brk_) - random.randint(1, 100) >= 0:
            #guarded
            dmg = dmg * (1.0 - self.pstat_n_.gdd_ / 100)
        else:
            if (self.mstat_n_.cr_ - self.pstat_n_.crr_) - random.randint(1, 100) >= 0:
                dmg = dmg * (self.mstat_n_.crd_ / 100)

        #텍스트 출력 후 1초 슬립


