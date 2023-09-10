import time
import random
while True:
    Rod_Wait = random.randint(3,20)
    Can_Catch = False
    Start = input('Press Enter To Start')
    Item_List = ['Duck Toy','Pirates Booty','Cell Phone','Suspision Doll','Silver Coin',' Old Boot','Rusty Can','Tarpon','Tarpon','Redfish','Trout','Cobia','Mahi-mahi','Grouper','Snapper','Kingfish','Tuna','Sailfish','Marlin','Amberjack','Barracuda','Permit','Bonefish','Sheepshead','Pompano','Jack Crevalle','Flounder']
    Fish_RNG = random.choice(Item_List)
    if Start == "":
        time.sleep(Rod_Wait)
        Can_Catch = True
        print('Press enter to pull back your rod!')
        ST = time.time()
        Pull_Back = input('')
        ET = time.time()
        if ET-ST > 3:
            print('You were',ET-ST-3,'seconds late')
            Can_Catch = False
        if Pull_Back == "" and Can_Catch == True:
            print('You caught a '+ Fish_RNG )
        Can_Catch = False
        
