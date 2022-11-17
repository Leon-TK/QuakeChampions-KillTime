from abc import ABC, abstractmethod
import weaponAttributes

class IWeapon(ABC):
	pass
class WeaponBase():
	def __init__(self):
		self.Attributes: weaponAttributes.AttributeBase = []

class Gauntlet(WeaponBase, IWeapon):
	def __init__(self):
		WeaponBase.__init__(self)
		self.Attributes.append(weaponAttributes.Damage(75))
		self.Attributes.append(weaponAttributes.DamageRate(0.57))

class NailGun(WeaponBase, IWeapon):
	def __init__(self):
		WeaponBase.__init__(self)
		self.Attributes.append(weaponAttributes.Damage(12))
		self.Attributes.append(weaponAttributes.DamageRate(0.1))

class MachineGun(WeaponBase, IWeapon):
	def __init__(self):
		WeaponBase.__init__(self)
		self.Attributes.append(weaponAttributes.Damage(8))
		self.Attributes.append(weaponAttributes.DamageRate(0.1))

class ShotGun(WeaponBase, IWeapon):
	def __init__(self):
		WeaponBase.__init__(self)
		self.Attributes.append(weaponAttributes.Damage(80))
		self.Attributes.append(weaponAttributes.DamageRate(1.0))

class SuperMachineGun(WeaponBase, IWeapon):
	def __init__(self):
		WeaponBase.__init__(self)
		self.Attributes.append(weaponAttributes.Damage(10))
		self.Attributes.append(weaponAttributes.DamageRate(0.1))

class SuperMachineGun_Zoomed(WeaponBase, IWeapon):
	def __init__(self):
		WeaponBase.__init__(self)
		self.Attributes.append(weaponAttributes.Damage(15))
		self.Attributes.append(weaponAttributes.DamageRate(0.1))	

class SuperNailGun(WeaponBase, IWeapon):
	def __init__(self):
		WeaponBase.__init__(self)
		self.Attributes.append(weaponAttributes.Damage(20))
		self.Attributes.append(weaponAttributes.DamageRate(0.1))

class SuperShotGun(WeaponBase, IWeapon):
	def __init__(self):
		WeaponBase.__init__(self)
		self.Attributes.append(weaponAttributes.Damage(120))
		self.Attributes.append(weaponAttributes.DamageRate(1.0))

class RailGun(WeaponBase, IWeapon):
	def __init__(self):
		WeaponBase.__init__(self)
		self.Attributes.append(weaponAttributes.Damage(90))
		self.Attributes.append(weaponAttributes.DamageRate(1.5))

class RocketLauncher(WeaponBase, IWeapon):
	def __init__(self):
		WeaponBase.__init__(self)
		self.Attributes.append(weaponAttributes.Damage(100))
		self.Attributes.append(weaponAttributes.DamageRate(0.8))

class LightningGun(WeaponBase, IWeapon):
	def __init__(self):
		WeaponBase.__init__(self)
		self.Attributes.append(weaponAttributes.Damage(6))
		self.Attributes.append(weaponAttributes.DamageRate(0.048))

class Tribolt(WeaponBase, IWeapon):
	def __init__(self):
		WeaponBase.__init__(self)
		self.Attributes.append(weaponAttributes.Damage(105))
		self.Attributes.append(weaponAttributes.DamageRate(1.31))

