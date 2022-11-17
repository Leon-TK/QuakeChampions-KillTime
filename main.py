import logs #TODO this is old version and causes exteptions
import algos
import weapon
import character
import characterClass


if __name__ == '__main__':
    logs.baseLog.staticInit("E:\\Source\\SourceCodes\\Quake weapon", "log")

    # for all character class get kill time by every weapon
    characters = [character.Nyx, character.Ranger, character.Scalebearer]
    characterClasses = [characterClass.LightClass, characterClass.MediumClass, characterClass.HeavyClass]

    weapons = [weapon.Gauntlet, weapon.ShotGun, weapon.MachineGun,
               weapon.NailGun, weapon.SuperMachineGun, weapon.SuperMachineGun_Zoomed, weapon.SuperShotGun, 
               weapon.SuperNailGun, weapon.RocketLauncher, weapon.RailGun,
               weapon.LightningGun, weapon.Tribolt]
               
    for weapon in weapons:
        print("Weapon: ", weapon, "\r")
        for character in characterClasses:
            killAlgo = algos.CalcKillTime(weapon(), True, True, True)
            killAlgo.setCharacterClass(character(), False)
            algo: algos.IAlgo = killAlgo
            algo.run()
            print("Class: ", character, ". Kill time: ", algo.getResult().getValue())
            
    
    