"""
CONDITIONS and LOOPS in PYTHON

# 01 - IF-ELIF-ELSE
# 02 - LOOPS in PYTHON

"""



""""
***********************************************************************************************************************
   01 - IF-ELIF-ELSE
*********************************************************************************************************************** 
"""

# There are two things to take note of with regard to syntax when you’re working with an if statement. First, all if
# statements end with a colon (:). Second, the code that gets executed if your condition is true is part of an indented
# block of code

# EXAMPLE-01

a = 5
b = 4
c = a + b

if c == 10:
    print ('c equals 10')
elif c == 9:
    print ('c equals 9')                        # c equals 9
else:
    print("i don't know anything about'c'" )

# EXAMPLE-02

hostname = 'Router01'

if hostname == 'router01':
    print('Same Device')
else:
    print ('Different Device')                  # Different Device

# EXAMPLE-03

vendors = ['CISCO', 'HP', 'DELL', 'JUNIPER']

if 'CISCO' in vendors:
    print ('CISCO is deployed')                 # CISCO is deployed

# EXAMPLE-04

version = "CSR1000V Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.3.1, RELEASE"
if '16.3' in version:
    print ('Your device is up to date')

"""
***********************************************************************************************************************
   02 - LOOPS in PYTHON
*********************************************************************************************************************** 
"""
# The general premise behind a while loop is that some set of code is executed while some condition is true.
# The syntax required is similar to what we used when creating if-elif-else statements. The while statement is
# completed with a colon (:) and the code to be exe‐ cuted is also indented four spaces.

# EXAMPLE-01
counter = 1

while counter < 5:
    print (counter)
    counter += 1
print ('end of loop')                           # 1
                                                # 2
                                                # 3
                                                # 4
                                                # end of loop

# For loops in Python are awesome because when you use them you are usually loop‐ ing, or iterating, over a set of
# objects, like those found in a list, string, or dictionary. for loops in other programming languages require an
# index and increment value to always be specified, which is not the case in Python.

# EXAMPLE-02

vendors = ['CISCO', 'HP', 'DELL', 'JUNIPER']

for vendor in vendors:
    print ('VENDOR: ' + vendor)                 # VENDOR: CISCO
                                                # VENDOR: HP
                                                # VENDOR: DELL
                                                # VENDOR: JUNIPER


# EXAMPLE-03

Legendary_Player = ['metin', 'ali', 'feyyaz', 'metin oktay', 'lefter']

player_list = ['melo', 'burak yilmaz', 'lefter']

for player in player_list:
    if player not in Legendary_Player:
        print ('Hadi oradan ' + player)         # Hadi oradan melo
                                                # Hadi oradan burak yilmaz
    else:
        print ('Saygilar '+ player)             # Saygilar lefter

# EXAMPLE-04

# To prepare for the next example, let’s build a dictionary that stores CLI commands to configure certain features
# on a network device. We see that we have a dictionary that has three items (key-value pairs). Each item’s key is a
# network feature to configure, and each item’s value is the start of a command string that’ll configure that respective
# feature. These features include speed, duplex, and description. The values of the dictionary each have curly braces
# ({}) because we’ll be using the format() method of strings to insert variables.

COMMANDS = {
    'description': 'description {}',
    'speed': 'speed {}',
    'duplex': 'duplex {}'
}

# Now that the COMMANDS dictionary is created, let’s create a second dictionary called CONFIG_PARAMS that will be used
# to dictate which commands will be executed and which value will be used for each command string defined in COMMANDS.

CONFIG_PARAM = {'description': 'auto description by python', 'speed': '10000', 'duplex': 'auto'}

command_list = []

for feature, value in CONFIG_PARAM.items():
    command = COMMANDS.get(feature).format(value)
    command_list.append(command)

command_list.insert(0,'interface ETH1/1')
print (command_list)                    # ['interface ETH1/1', 'description auto description by python', 'speed 10000',
                                        # 'duplex auto']

# enumerate() is used to enumerate the list and give an index value, and is often handy to determine the exact position
# of a given element. The next example shows how to use enumerate() within a for loop. You’ll notice that the beginning
# part of the for loop looks like the dictionary examples, only unlike items(), which returns a key and value, enumerate()
# returns an index, starting at 0, and the object from the list that you are enumerating.

vendors = ['CISCO', 'HP', 'DELL', 'HUAWEI', 'JUNIPER']

for index, each in enumerate(vendors):
    print (str(index) + ' '+ each)      # 0 CISCO
                                        # 1 HP
                                        # 2 DELL
                                        # 3 HUAWEI
                                        # 4 JUNIPER





