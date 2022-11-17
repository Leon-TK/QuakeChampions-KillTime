from abc import ABC, abstractmethod

import items
import logs

class ICharacterClass(ABC):
	pass

class CharacterClassBase():
	def __init__(self):
		self.startHP = 0
		self.startArmor = 0
		self.maxHP = 0
		self.maxArmor = 0	
			
class HeavyClass(CharacterClassBase, ICharacterClass):
	def __init__(self):
		CharacterClassBase.__init__(self)
		self.startHP = 125
		self.startArmor = 75
		self.maxHP = 100
		self.maxArmor = 125

class MediumClass(CharacterClassBase, ICharacterClass):
	def __init__(self):
		CharacterClassBase.__init__(self)
		self.startHP = 125
		self.startArmor = 50
		self.maxHP = 100
		self.maxArmor = 100

class LightClass(CharacterClassBase, ICharacterClass):
	def __init__(self):
		CharacterClassBase.__init__(self)
		self.startHP = 125
		self.startArmor = 25
		self.maxHP = 100
		self.maxArmor = 75