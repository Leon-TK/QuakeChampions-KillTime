from abc import ABC, abstractmethod

import weaponAttributes
import character
import weapon
import math
import characterClass
import items
import logs

class IAlgoResult(ABC):
    @abstractmethod
    def printConsole(self) -> None:
        pass
    @abstractmethod
    def compare(self, other) -> None:
        pass
    @abstractmethod
    def getValue(self):
        pass

class IAlgo(ABC):
    @abstractmethod
    def getResult(self) -> IAlgoResult:
        pass
    @abstractmethod
    def run(self):
        pass

class AlgoBase():
    pass

class KillTimeResult(IAlgoResult):
    def __init__(self, time) -> None:
        self.time = time
    def printConsole(self) -> None:
        print(self.time)
    def compare(self, other) -> None:
        other.__class__ = KillTimeResult
        if self.time < other.time:
            diff = other.time - self.time
            print("This kill time is faster than other by ", diff)
        elif self.time > other.time:
            diff = self.time - other.time
            print("This kill time is slower than other by ", diff)
        else: 
            print("Kill times are equal")    
    def getValue(self):
        return self.time

class CalcKillTime(IAlgo, AlgoBase):
    def __init__(self, weapon: weapon.WeaponBase,
                 bFirstShotAtZero: bool = False, bUseMega: bool = False, bUseRed: bool = False) -> None:
        AlgoBase.__init__(self)
        # use this by calling setCharacter
        self.character = None
        # or this by calling setCharacterClass
        self.characterClass = None
        self.weapon = weapon
        # if true calculate kill time with shot at zero(0) time
        self.bFirstShotAtZero = bFirstShotAtZero
        self.bUseMega = bUseMega
        self.bUseRed = bUseRed
        # use default starting stack at round begining. Being use only with charClass case
        self.bStartingStack = False
        self.result: IAlgoResult = None

    def setCharacter(self, character: character.CharacterBase):
        self.character = character
        self.characterClass = None
    def setCharacterClass(self, characterClass: characterClass.CharacterClassBase, bStartingStack):
        self.characterClass = characterClass
        self.bStartingStack = bStartingStack
        self.character = None

    def processCharacter(self):
        if self.bUseMega:
            self.character.ApplyItem(items.Mega())
        if self.bUseRed:
            self.character.ApplyItem(items.Red())
        
        sum = self.character.currentHP + self.character.currentArmor
        logs.simpleLog("Stack: " + str(sum))
        damage = self.findDamageAttribute().damage
        rate = self.findDamageRateAttribute().ratePerSecond
        shots = self.CalcTotalShots(sum, damage)
        self.CalcKillTime(rate, shots, self.bFirstShotAtZero)

    def processCharacterClass(self):

        sum = 0
        hp = 0
        armor = 0

        # calculate mega and red usage
        if self.bStartingStack:
            if self.bUseMega:
                if self.characterClass.startHP == self.characterClass.maxHP:
                    hp = self.characterClass.startHP + 75
                elif self.characterClass.startHP < self.characterClass.maxHP:
                    hp = self.characterClass.startHP + 100
                elif self.characterClass.startHP > self.characterClass.maxHP:
                    hp = self.characterClass.maxHP + 75
                logs.simpleLog("Use mega: " + str(hp))
            if self.bUseRed:
                if self.characterClass.startArmor == self.characterClass.maxArmor:
                    armor = self.characterClass.startArmor + 75
                elif self.characterClass.startArmor < self.characterClass.maxArmor:
                    armor = self.characterClass.startArmor + 100
                elif self.characterClass.startArmor > self.characterClass.maxArmor:
                    armor = self.characterClass.maxArmor + 75
                logs.simpleLog("Use red: " + str(armor))
        else:
            if self.bUseMega:
                hp = self.characterClass.maxHP + 75
                logs.simpleLog("Use mega: " + str(hp))
            if self.bUseRed:
                armor = self.characterClass.maxArmor + 75
                logs.simpleLog("Use red: " + str(armor))
            
        sum = hp + armor
        logs.simpleLog("Stack: " + str(sum))
        damage = self.findDamageAttribute().damage
        rate = self.findDamageRateAttribute().ratePerSecond
        shots = self.CalcTotalShots(sum, damage)
        self.CalcKillTime(rate, shots, self.bFirstShotAtZero)

    def findDamageAttribute(self) -> weaponAttributes.Damage:
        for attr in self.weapon.Attributes:
            if type(attr) is weaponAttributes.Damage:
                return attr

    def findDamageRateAttribute(self) -> weaponAttributes.DamageRate:
        for attr in self.weapon.Attributes:
            if type(attr) is weaponAttributes.DamageRate:
                return attr

    def CalcTotalShots(self, stack, damage) -> int:
        return math.ceil(stack / damage)

    def CalcKillTime(self, rate, shots, bFirstAtZero):
        if bFirstAtZero:
            self.result = KillTimeResult((rate * shots) - rate)
        else:
            self.result = KillTimeResult(rate * shots)

    def run(self):
        if self.character is not None and self.characterClass is None:
            self.processCharacter()
        elif self.characterClass is not None and self.character is None:
            self.processCharacterClass()
        else: 
            return
        
    def getResult(self) -> IAlgoResult:
        return self.result