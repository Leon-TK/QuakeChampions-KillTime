from abc import ABC, abstractmethod

import characterClass
import items
import logs

class ICharater(ABC):
	pass

class CharacterBase():
	def __init__(self, charClass: characterClass.CharacterClassBase, bStartingStack: bool):
		self.charClass = charClass
		self.currentHP = 0
		self.currentArmor = 0

		if bStartingStack:
			self.currentHP = self.charClass.startHP
			self.currentArmor = self.charClass.startArmor
		else:
			self.currentHP = self.charClass.maxHP
			self.currentArmor = self.charClass.maxArmor
		logs.simpleLog("Character initiated: HP " + str(self.currentHP) + " Armor " + str(self.currentArmor))

	def ApplyItem(self, item: items.ItemBase):
		if type(item) is items.Mega:
			if self.currentHP == self.charClass.maxHP:
				self.currentHP += 75
			elif self.currentHP < self.charClass.maxHP:
				self.currentHP += 100
			elif self.currentHP > self.charClass.maxHP:
				self.currentHP = self.charClass.maxHP + 75
			logs.simpleLog("Apply Mega is complete: HP " + str(self.currentHP))
			
		if type(item) is items.Red:
			if self.currentArmor == self.charClass.maxArmor:
				self.currentArmor += 75
			elif self.currentArmor < self.charClass.maxArmor:
				self.currentArmor += 100
			elif self.currentArmor > self.charClass.maxArmor:
				self.currentArmor = self.charClass.maxArmor + 75
			logs.simpleLog("Apply Red is complete: HP " + str(self.currentArmor))
	#def GetOverHeal()
	
class Slash(CharacterBase, ICharater):
	def __init__(self, bStartingStack: bool):
		CharacterBase.__init__(self, characterClass.LightClass(), bStartingStack)
class Ranger(CharacterBase, ICharater):
	def __init__(self, bStartingStack: bool):
		CharacterBase.__init__(self, characterClass.MediumClass(), bStartingStack)
class Scalebearer(CharacterBase, ICharater):
	def __init__(self, bStartingStack: bool):
		CharacterBase.__init__(self,characterClass.HeavyClass(), bStartingStack)
class DeathKnight(CharacterBase, ICharater):
	def __init__(self, bStartingStack: bool):
		CharacterBase.__init__(self, characterClass.MediumClass(), bStartingStack)
class Doom(CharacterBase, ICharater):
	def __init__(self, bStartingStack: bool):
		CharacterBase.__init__(self, characterClass.MediumClass(), bStartingStack)
class Eisen(CharacterBase, ICharater):
	def __init__(self, bStartingStack: bool):
		CharacterBase.__init__(self, characterClass.MediumClass(), bStartingStack)
class Nyx(CharacterBase, ICharater):
	def __init__(self, bStartingStack: bool):
		CharacterBase.__init__(self, characterClass.LightClass(), bStartingStack)
class Keel(CharacterBase, ICharater):
	def __init__(self, bStartingStack: bool):
		CharacterBase.__init__(self, characterClass.HeavyClass(), bStartingStack)
class Clutch(CharacterBase, ICharater):
	def __init__(self, bStartingStack: bool):
		CharacterBase.__init__(self, characterClass.HeavyClass(), bStartingStack)
class Galena(CharacterBase, ICharater):
	def __init__(self, bStartingStack: bool):
		CharacterBase.__init__(self, characterClass.MediumClass(), bStartingStack)
class Anarki(CharacterBase, ICharater):
	def __init__(self, bStartingStack: bool):
		CharacterBase.__init__(self, characterClass.LightClass(), bStartingStack)
class Athena(CharacterBase, ICharater):
	def __init__(self, bStartingStack: bool):
		CharacterBase.__init__(self, characterClass.LightClass(), bStartingStack)
class Visor(CharacterBase, ICharater):
	def __init__(self, bStartingStack: bool):
		CharacterBase.__init__(self, characterClass.MediumClass(), bStartingStack)
class Blazhkovitch(CharacterBase, ICharater):
	def __init__(self, bStartingStack: bool):
		CharacterBase.__init__(self, characterClass.MediumClass(), bStartingStack)
class Strogg(CharacterBase, ICharater):
	def __init__(self, bStartingStack: bool):
		CharacterBase.__init__(self, characterClass.MediumClass(), bStartingStack)
class Sorlag(CharacterBase, ICharater):
	def __init__(self, bStartingStack: bool):
		CharacterBase.__init__(self, characterClass.HeavyClass(), bStartingStack)