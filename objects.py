import random
import math
import time

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
    
    def __add__(self, stat):
        # element는 따로 바꿔주자.
        self.hp_ += stat.hp_
        self.atk_ += stat.atk_
        self.def_ += stat.def_
        self.hr_ += stat.hr_
        self.dr_ += stat.dr_
        self.cr_ += stat.cr_
        self.crr_ += stat.crr_
        self.crd_ += stat.crd_
        self.gr_ += stat.gr_
        self.gdd_ += stat.gdd_
        self.brk_ += stat.brk_
        self.speed_ += stat.speed_
    
    def __sub__(self, stat):
        # element는 따로 바꿔주자.
        self.hp_ -= stat.hp_
        self.atk_ -= stat.atk_
        self.def_ -= stat.def_
        self.hr_ -= stat.hr_
        self.dr_ -= stat.dr_
        self.cr_ -= stat.cr_
        self.crr_ -= stat.crr_
        self.crd_ -= stat.crd_
        self.gr_ -= stat.gr_
        self.gdd_ -= stat.gdd_
        self.brk_ -= stat.brk_
        self.speed_ -= stat.speed_

class stat_s:
    def __init__(self, elemforce = 0, givedmginc = 0.0, getdmgdec = 0.0): # base stats
        self.eforce_ = elemforce
        self.givedmginc_ = givedmginc
        self.getdmgdec_ = getdmgdec
    
    def __add__(self, stat):
        # element는 따로 바꿔주자.
        self.eforce_ += stat.eforce_
        self.givedmginc_ += stat.givedmginc_
        self.getdmgdec_ += stat.getdmgdec_
    
    def __sub__(self, stat):
        # element는 따로 바꿔주자.
        self.eforce_ -= stat.eforce_
        self.givedmginc_ -= stat.givedmginc_
        self.getdmgdec_ -= stat.getdmgdec_

class Monster():
    def __init__(self, lv, type_: str, stat_n: stat_n, stat_s = stat_s()):
        self.lv_ = lv
        self.type_ = type_ # Normal, Elite, BOSS
        self.curhp_ = stat_n.hp_
        self.stat_n_ = stat_n
        self.stat_s_ = stat_s
    
    def monsterinfo(self):
        print("type: " + str(self.type_))
        print("level: " + str(self.lv_))
        print("hp: " + str(self.stat_n_.hp_))
        print("atk: " + str(self.stat_n_.atk_))
        print("def: " + str(self.stat_n_.def_))
        print("element: " + self.stat_n_.atkelement_)

class Weapon:
    def __init__(self, type_: str, stat_n: stat_n, stat_s = stat_s()) -> None:
        self.type_ = type_ # Sword, etc..
        

class Player:
    weapon = "None"

    def __init__(self, lv, class_: str, stat_n = stat_n(), stat_s = stat_s()):
        self.lv_ = lv
        self.class_ = class_ # Warrior, etc.
        self.curhp_ = stat_n.hp_
        self.stat_n_ = stat_n
        self.stat_s_ = stat_s
    
    def playerinfo(self):
        print("class: " + str(self.class_))
        print("level: " + str(self.lv_))
        print("hp: " + str(self.curhp_) + "/" + str(self.stat_n_.hp_))
        print("atk: " + str(self.stat_n_.atk_))
        print("def: " + str(self.stat_n_.def_))
        print("element: " + self.stat_n_.atkelement_)
    
    def changestat(self):
        return
    
    def levelup(self):
        return
    
    def takeoffWeapon(self):
        if self.weapon == "None":
            print("You can't do it.")
            return
        
    
    def changeWeapon(self): # 장비 교체
        if self.weapon != "None":
            print("")
            return
        return
        
def compareElement(attacker, defender):
        if attacker.stat_n_.atkelement_ == defender.stat_n_.defelement_:
            return 0 # "Equal"
        elif (defender.stat_n_.defelement_ == "None") or (attacker.stat_n_.atkelement_ == "Blaze" and defender.stat_n_.defelement_ == "Earth") or (attacker.stat_n_.atkelement_ == "Cold" and defender.stat_n_.defelement_ == "Blaze") or (attacker.stat_n_.atkelement_ == "Earth" and defender.stat_n_.defelement_ == "Cold"):
            return 1 # "Attacker"
        else:
            return 2 # "Defender"
        # 나중에 무속성 뎀추*감은 10%로 변경하기.

class BattlePVE:
    turn = 1

    def __init__(self, player: Player, monster: Monster):
        self.player = player # 원래 스탯
        self.monster = monster
        self.pstat_n_ = player.stat_n_ # 버프 포함 최종 스탯
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
            print("Player guarded.")
            dmg = dmg * (1.0 - self.pstat_n_.gdd_ / 100)
        else:
            if (self.mstat_n_.cr_ - self.pstat_n_.crr_) - random.randint(1, 100) >= 0:
                #critical occured
                print("Critical!!")
                dmg = dmg * (self.mstat_n_.crd_ / 100)
        
        if compareElement(self.monster, self.player) == 1:
            dmg = dmg * (1.5 + self.mstat_s_.eforce_ / 10000)
        elif compareElement(self.monster, self.player) == 2:
            dmg = dmg * (0.7 - self.pstat_s_.eforce_ / 10000)
        else:
            dmg = dmg * 1
        
        dmg = dmg * (1.0 + (self.mstat_s_.givedmginc_ - self.pstat_s_.getdmgdec_) / 100)
        
        self.player.curhp_ -= math.floor(dmg * 10) / 10 # 소수점 한자리 변경
        print("Player's hp: " + str(self.player.curhp_ ) + "/" + str(self.player.stat_n_.hp_))
        time.sleep(1) #텍스트 출력 후 1초 슬립

        if self.player.curhp_  <= 0:
            return True # death
        return False

    def attacktom(self):
        dmg = (float)(self.pstat_n_.atk_ - self.mstat_n_.def_)
        if (self.pstat_n_.hr_ - self.mstat_n_.dr_) - random.randint(1, 100) < 0:
            # missed, dmg 0
            return 0.0
        if (self.mstat_n_.gr_ - self.pstat_n_.brk_) - random.randint(1, 100) >= 0:
            #guarded
            print("Monster guarded.")
            dmg = dmg * (1.0 - self.mstat_n_.gdd_ / 100)
        else:
            if (self.pstat_n_.cr_ - self.mstat_n_.crr_) - random.randint(1, 100) >= 0:
                #critical occured
                print("Critical!!")
                dmg = dmg * (self.pstat_n_.crd_ / 100)
        
        if compareElement(self.player, self.monster) == 1:
            dmg = dmg * (1.5 + self.pstat_s_.eforce_ / 10000)
        elif compareElement(self.player, self.monster) == 2:
            dmg = dmg * (0.7 - self.mstat_s_.eforce_ / 10000)
        else:
            dmg = dmg * 1
        
        dmg = dmg * (1.0 + (self.pstat_s_.givedmginc_ - self.mstat_s_.getdmgdec_) / 100)
        
        self.monster.curhp_ -= math.floor(dmg * 10) / 10 # 소수점 한자리 변경
        print("Monster's hp: " + str(self.monster.curhp_) + "/" + str(self.mosnter.stat_n_.hp_))
        time.sleep(0.5) #텍스트 출력 후 1초 슬립

        if self.monster.curhp_ <= 0:
            return True # death
        return False
    
    def passedturn(self):
        print("Total Passed turn: " + str(self.turn))
        return

    def battle(self):
        if self.player.stat_n_.speed_ < self.monster.stat_n_.speed_:
            if self.attacktop():
                self.passedturn()
                return False # Monster win.
            self.turn += 0.5
        
        while True:
            if self.attacktom():
                self.passedturn()
                return True
            self.turn += 0.5
            if self.attacktop():
                self.passedturn()
                return False
            self.turn += 0.5
            
