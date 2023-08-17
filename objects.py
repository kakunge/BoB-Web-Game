import random
import math
import time

class stat_n:
    def __init__(self, hp = 20.0, atk = 2, def_ = 1, hitrate = 100.0, dodgerate = 5.0,
                  critrate = 5.0, critres = 0.0, critdmg = 150.0, guardrate = 3.0, guarddmgdec = 30.0, brkthr = 0.0, speed = 10): # player's base stats
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

class Reward:
    def __init__(self, gold, exp, items = None):
        self.gold = gold
        self.exp = exp
        self.items = items # list of Item

class Monster:
    def __init__(self, name: str, lv, type_: str, element: str, reward: Reward, stat_n: stat_n, stat_s = stat_s()):
        self.name = name
        self.lv_ = lv
        self.type_ = type_ # Normal, Elite, BOSS
        self.curhp_ = stat_n.hp_
        self.atkelement_ = element
        self.defelement_ = element
        self.reward = reward
        self.stat_n_ = stat_n
        self.stat_s_ = stat_s
    
    def monsterinfo(self):
        print("type: " + str(self.type_))
        print("level: " + str(self.lv_))
        print("hp: " + str(self.stat_n_.hp_))
        print("atk: " + str(self.stat_n_.atk_))
        print("def: " + str(self.stat_n_.def_))
        print("element: " + self.atkelement_)

class Item:
    def __init__(self, class_, explanation: str, nums = 1):
        self.class_ = class_ # 소비, 기타 ...
        self.explanation = explanation
        self.nums = nums

class Equipment(Item):
    class_ = "Equipment"
    def __init__(self, type_: str):
        self.type_ = type_ # ...

class Weapon(Equipment):
    #class_ = super().class_
    slot = 1
    def __init__(self, name: str, type_: str, explanation: str, element: str, stat_n: stat_n, stat_s = stat_s()):
        super().__init__(type_)
        self.name = name
        self.type_ = type_ # Sword, etc..
        self.explanation = explanation
        self.element_ = element
        self.stat_n_ = stat_n
        self.stat_s_ = stat_s
        self.class_ = super().class_

class Armor(Equipment):
    def __init__(self, name: str, slot: int, type_: str, explanation: str, element: str, stat_n: stat_n, stat_s = stat_s()):
        super().__init__(type_)
        self.name = name
        self.slot = slot # 2, 3, 4
        self.type_ = type_ # Cloth, etc..
        self.explanation = explanation
        self.element_ = element # 방어속성은 갑옷에 의해 결정된다. 나머지는 무속성.
        self.stat_n_ = stat_n
        self.stat_s_ = stat_s
        self.class_ = super().class_

class Accessory(Equipment):
    def __init__(self, name: str, slot: int, type_: str, explanation: str, stat_n: stat_n, stat_s = stat_s()):
        super().__init__(type_)
        self.name = name
        self.slot = slot
        self.type_ = type_ # 목걸이, 반지
        self.explanation = explanation
        self.stat_n_ = stat_n
        self.stat_s_ = stat_s
        self.class_ = super().class_

#class Rune: #나중에..

class Player:
    equipments = [None, None, None, None, None, None]
    atkelement_ = "None"
    defelement_ = "None"
    maxexp = 10
    curexp = 0
    gold = 0
    inventory = None # list of Item
    reststat = 0
    #title #칭호, 나중에..

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
        print("element: " + self.atkelement_)
        if self.equipments[0] == None:
            print("weapon: None")
        else:
            print("weapon: " + self.equipments[0].name)

    
    def changestat(self):
        return
    
    def levelup(self):
        while self.curexp < self.maxexp:
            self.curexp -= self.maxexp
            self.lv_ += 1
            self.stat_n_.hp_ += 10
            self.curhp_ = self.stat_n_.hp_
            self.reststat += 5
            if self.lv_ < 10:
                self.maxexp += self.lv_ * 10
            elif self.lv_ == 10:
                self.maxexp += self.lv_ * 10
                self.maxexp *= 2
            elif (10 < self.lv_) and (self.lv_ < 30):
                self.maxexp += self.lv_ * 20
            elif self.lv_ == 30:
                self.maxexp += self.lv_ * 20
                self.maxexp *= 2
            elif (30 < self.lv_) and (self.lv_ < 60):
                self.maxexp += self.lv_ * 40
            elif self.lv_ == 60:
                self.maxexp += self.lv_ * 40
                self.maxexp *= 3
            elif (60 < self.lv_) and (self.lv_ < 100):
                self.maxexp += self.lv_ * 120
            else:
                self.maxexp = 10000000000000
        
        return
    
    def unequip(self, slot: int):
        if self.equipments[slot - 1] == None:
            return
        
        self.stat_n_ - self.equipments[slot - 1].stat_n_
        self.stat_s_ - self.equipments[slot - 1].stat_s_
        if self.curhp_ > self.stat_n_.hp_:
            self.curhp_ = self.stat_n_.hp_
        self.equipments[slot - 1] = None
        return
    
    def Equip(self, equipment): # 장비 교체
        self.unequip(equipment.slot)
        self.equipments[equipment.slot - 1] = equipment
        self.stat_n_ + equipment.stat_n_
        self.stat_s_ + equipment.stat_s_
        return

        
def compareElement(attacker, defender):
        if attacker.atkelement_ == defender.defelement_:
            return 0 # "Equal"
        elif (defender.defelement_ == "None") or (attacker.atkelement_ == "Blaze" and defender.defelement_ == "Earth") or (attacker.atkelement_ == "Cold" and defender.defelement_ == "Blaze") or (attacker.atkelement_ == "Earth" and defender.defelement_ == "Cold"):
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
        print("Monster's hp: " + str(self.monster.curhp_) + "/" + str(self.monster.stat_n_.hp_))
        time.sleep(0.5) #텍스트 출력 후 1초 슬립

        if self.monster.curhp_ <= 0:
            return True # death
        return False
    
    def passedturn(self):
        print("Total Passed turn: " + str(self.turn))
        return

    def defeat(self):
        # lose exp. + 상태이상: 부상. 숙소 등에서 회복 가능.
        self.player.curexp = math.ceil(self.player.curexp * 3 / 4)
        return
    
    def win(self, monster: Monster):
        # get rewards.
        self.player.gold += monster.reward.gold
        self.player.curexp += monster.reward.exp
        if self.player.curexp > self.player.maxexp:
            self.player.levelup()
        return

    def battle(self):
        if self.player.stat_n_.speed_ < self.monster.stat_n_.speed_:
            if self.attacktop():
                self.passedturn()
                print("Monster wins.")
                self.defeat()
                return False # Monster win.
            self.turn += 0.5
        
        while True:
            if self.attacktom():
                self.passedturn()
                print("You win.")
                self.win(self.monster)
                return True
            self.turn += 0.5
            if self.attacktop():
                self.passedturn()
                print("Monster wins.")
                self.defeat()
                return False
            self.turn += 0.5
            
class Field:
    player = None
    dangerlevel = 1 # 위협도. max: 100
    area = 1 # 1, 2. 2에서 보스 도전 가능.
    battlepve = None
    recovercount = 5

    def __init__(self, name: str, fieldlevel: int):
        self.name = name
        self.flevel = fieldlevel # 추천레벨: (fieldlevel - 1)*10 ~ fieldlevel*10 이며 area별로 5, 5를 담당한다.

    def enter(self, player: Player):
        self.player = player
        return
    
    def leave(self, player: Player):
        self.player = None
        return
    
    def changearea(self, areanum: int):
        self.area = areanum
        return
    
    def incdanger(self):
        self.dangerlevel += random.randint(10, 20)
        if self.dangerlevel > 100:
            self.dangerlevel = 100
        return
    
    def initializedanger(self):
        self.dangerlevel = 0
        return

    def recover(self):
        return

    def encounter(self):
        # DB랑 연동 후 적정레벨과 배틀. 종료 후 None으로 바꾼다.
        return
    
    def boss_challenge(self):
        # 최종목표는 DB랑 연동. 그 전에는 하드코딩.
        return

    def explore(self):
        if self.dangerlevel - random.randint(1, 100) >= 0:
            self.encounter()
        
        probabilitylv = random.randint(1, 100)
        reclv = (self.fieldlevel - 1)*10 + self.area*5 # 적정레벨
        if probabilitylv <= 40:
            self.incdanger()
            self.player.curexp += random.randint(reclv*5 - 24, math.floor((reclv**2) * 3 / 5))
            self.player.gold += random.randint(reclv, reclv*4)
        elif (40 < probabilitylv) and (probabilitylv <= 50):
            self.player.gold += random.randint(reclv*20, reclv*80)
        elif (50 < probabilitylv) and (probabilitylv <= 70):
            self.player.curhp_ -= (math.ceil(self.player.stat_n_.hp_ / 5) + reclv - self.player.stat_n_.def_)
        elif (70 < probabilitylv) and (probabilitylv <= 75):
            return
        elif (75 < probabilitylv) and (probabilitylv <= 80):
            return
        else:
            return
        
        return

