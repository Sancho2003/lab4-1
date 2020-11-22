from entities import player, enemy
from items import weapon

player1 = player.Player("Klotske", 200)
zenith = weapon.Zenith()
player1.equip(zenith)
print(player1)
player1.heal()
print(player1)

player2 = player.Player("Gathes", 300)
print(player2)
terra_blade = weapon.TerraBlade()
player2.equip(terra_blade)
print(player2)

demon_eye = enemy.DemonEye()
demon_eye.attack(player1)
print(player1)
print(demon_eye)
player1.attack(demon_eye)
print(demon_eye)

zombie = enemy.Zombie()
wooden_sword = weapon.WoodenSword()
zombie.equip(wooden_sword)
print(zombie)
print(player2)
zombie.attack(player2)
zombie.attack(player2)
zombie.attack(player2)
zombie.attack(player2)
print(player2)
player2.attack(zombie)
print(zombie)