import keyboard
import random

#this program in no way interacts with the game, to avoid being a cheat, it simply prints names to the console
MainGuns = ['SR 7.62','tactical shotgun','M4','Ballitsic shield','Oppresor','ES36','UMP','Rattler','HB82','Mark 12','Mac-10','Kyanite','AKU','Sawed off','Bizon','Valkyrie','FAL','SKS']
Sidearms = ['Mock 17','P10C','Falcon','SW11','FN57']
Tools1 = ['Frag grenade','Flash grenade','C2 Charge','Night vision']
Tools2 = ['Frag grenade','Flash grenade','UDC','Smoke grenade']
Tools3 = ['Door rammer','Medkit']

while True:
    keyboard.wait('e')
    print('--------------')
    print(random.choice(MainGuns))
    print(random.choice(Sidearms))
    print(random.choice(Tools1))
    print(random.choice(Tools2))
    print(random.choice(Tools3))
