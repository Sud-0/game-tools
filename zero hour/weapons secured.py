import keyboard

#this was one of my first few scripts, explaining the bad variable naming and such
#this program in no way interacts with the game directly, to avoid being a cheat, its simply a counter with a name behind it
while True:
    weaponcount = 0
    enemynum = input('how many enemies on the map? ')

    try:
        enemynumcnv = int(enemynum)
    except:
        print('please enter a number')

    while True:
        keyboard.wait('`')
        weaponcount = weaponcount + 1
        weaponcountstr = str(weaponcount)
        print(weaponcountstr + '/' + enemynum)
        if weaponcount == enemynumcnv:
            print('all weapons secured')
            break