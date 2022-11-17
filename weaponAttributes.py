from abc import ABC, abstractmethod

class IAttribute(ABC):
	pass

class AttributeBase():
	pass

class Damage(AttributeBase, IAttribute):
	def __init__(self, damage):
		AttributeBase.__init__(self)
		self.damage = damage

class DamageRate(AttributeBase, IAttribute):
	def __init__(self, ratePerSecond):
		AttributeBase.__init__(self)
		self.ratePerSecond = ratePerSecond

class Splash(AttributeBase, IAttribute):
	def __init__(self, range):
		AttributeBase.__init__(self)
		self.range = range
		
class Range(AttributeBase, IAttribute):
	def __init__(self, range):
		AttributeBase.__init__(self)
		self.range = range