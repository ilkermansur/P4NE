
"""

######                                      #######                  
#     # #   # ##### #    #  ####  #    #    #        ####  #####     
#     #  # #    #   #    # #    # ##   #    #       #    # #    #    
######    #     #   ###### #    # # #  #    #####   #    # #    #    
#         #     #   #    # #    # #  # #    #       #    # #####     
#         #     #   #    # #    # #   ##    #       #    # #   #     
#         #     #   #    #  ####  #    #    #        ####  #    #    

#     #                                             #######                                             
##    # ###### ##### #    #  ####  #####  #    #    #       #    #  ####  # #    # ###### ###### #####  
# #   # #        #   #    # #    # #    # #   #     #       ##   # #    # # ##   # #      #      #    # 
#  #  # #####    #   #    # #    # #    # ####      #####   # #  # #      # # #  # #####  #####  #    # 
#   # # #        #   # ## # #    # #####  #  #      #       #  # # #  ### # #  # # #      #      #####  
#    ## #        #   ##  ## #    # #   #  #   #     #       #   ## #    # # #   ## #      #      #   #  
#     # ######   #   #    #  ####  #    # #    #    ####### #    #  ####  # #    # ###### ###### #    # 



COMMON DATA TYPE IN PYTHON

01 - STRINGS
02 - INTEGERS,FLOAT
03 - BOOLEANS
04 - LISTS
05 - TUPLE
06 - SET
07 - DICTIONARY
08 - FILES

"""



*********************************************************************************************************************** 
	01 - STRING
*********************************************************************************************************************** 

# String can use single, double quotes

  ip_1 = '10.0.0.1'
  print (ip_1)
  print (len(ip_1))
  
		# --> 10.0.0.1
		# --> 8

  ip_2 = "10.0.0.2"
  print (ip_2) 

		# --> 10.0.0.2

# or both

  Einstein = "If you can't explain it simply, you don't understand it well enough"
  print (Einstein)
  print (len(Einstein))

		# --> If you can't explain it simply, you don't understand it well enough
		# --> 67


*********************************************************************************************************************** 
	STRING OPERATIONS
*********************************************************************************************************************** 
 
# You can add strings together to concatenate them

  ipaddr = ip_1 + ip_2
  print (ipaddr)                      

		# --> 10.0.0.110.0.0.2

# You can use whitespace between strings

  ipaddr = ip_1 + ' ' +ip_2
  print (ipaddr)                      

		# --> 10.0.0.1 10.0.0.2

# Easy way to add more whitespace between strings another words strings can be multiply

  ipaddr = ip_1 + ' '*10 +ip_2
  print(ipaddr)                      

		# --> 10.0.0.1          10.0.0.2

# You can't add strings and numbers

  age=40
  print("You are " + age)           

		# --> TypeError: can only concatenate str (not "int") to str

# But you can if you turn the number into a string first:
  
  age=40
  age_as_string = str(40)
  print("You are " + age_as_string) 
   
		# --> You are 40

****************************************************************************************************************************
	SOME ESCAPE CHARACTERS
****************************************************************************************************************************
 
  Einstein = "If you can't explain it simply,\n you don't understand it well enough"
  print (Einstein)

		# --> If you can't explain it simply,
		#     you don't understand it well enough

  Einstein = "If you can't explain it simply,\n\n you don't understand it well enough"
  print (Einstein)

		# --> If you can't explain it simply,
		
		#      you don't understand it well enough

  nameandsurname = 'ilker\tmansur'
  print (nameandsurname)
  
		# --> ilker    mansur

  Einstein = 'If you can\'t explain it simply, you don\'t understand it well enough'
  print (Einstein)
  
	   # --> 'If you can\'t explain it simply, you don\'t understand it well enough'

****************************************************************************************************************************   
	INDEX of STRING
****************************************************************************************************************************
 
  adsoyad = 'ilker mansur'
  print(adsoyad[0])
  
		# --> i
		
  print(adsoyad[1])
  
		# --> l
		
  print(adsoyad[2])

		# --> k
		
  print(adsoyad[3])

		# --> e
		
  print(adsoyad[4])

		# --> r

# or specific part of string

  print (adsoyad[0:])
  
		# --> ilker mansur
		
  print (adsoyad[6:])
  
		# --> mansur
		
  print (adsoyad[:6])
  
		# --> ilker
		
  print(adsoyad[2:4])
  
		# --> ke

# Actually data types ,that we use, are classes at the same time<class 'str'>
		
  print (type (adsoyad))
  
		# --> <class 'str'>

****************************************************************************************************************************
	SOME METHOD of STR CLASS
****************************************************************************************************************************
		
  adsoyad = "    İlker Mansur    "

  print(adsoyad.count('r'))

		# --> 2
		
  print(adsoyad.endswith('r'))

		# --> False
		
  print(adsoyad.endswith(' '))

		# --> True
		
  print(adsoyad.startwith('İ'))

		# --> True
		
  print(adsoyad.lower())

		# -->     ilker mansur
		  
  print(adsoyad.upper())

		# -->     İLKER MANSUR
		
  print(adsoyad.strip())

		# --> İlker Mansur
		
  print(adsoyad.rstrip())

		# -->     İlker Mansur
		
  print(adsoyad.lstrip())

		# --> İlker Mansur
		

  ip_address = "10.0.0.1 255.255.255.0"

  print(ip_address.split(' '))

		# --> ['10.0.0.1', '255.255.255.0']
  
  print (ip_address.split('.'))

		# --> ['10', '0', '0', '1 255', '255', '255', '0']

  new_ip_address = ip_address.replace('10','20')
  print(new_ip_address)

		# --> 20.0.0.1 255.255.255.0

  new_ip_address = ip_address[::-1]

		# --> 0.552.552.552 1.0.0.01
		
****************************************************************************************************************************
	02 - INTEGER & FLOAT
****************************************************************************************************************************

  number = 10
  print(type(number))

		# --> <class 'int'>
		
  number = 10.0
  print(type(number))

		# --> <class 'float'>
	
# In network automation scripts, use str for expressing ip address instead of integer because of syntax

ipaddr_int = 10.0.0.1
ipaddr_str = '10.0.0.1'

# MATH with operator ('+' '-' '*' '/' '//' '%')

  a = 9
  b = 2
  
  c = a + b
  print (c)

		# --> 11
  
  c = a - b
  print (c)

		# --> 7
  
  c = a / b
  print (c)

		# --> 4.5
  
  c = a // b
  print (c)

		# --> 4
  
  c = a % b
  print (c)

		# --> 1

# It is possibble to convert int <-> float
	
  a = 9
  b = float(a)
  print(b)

		# --> 9.0

  c = 7.0
  d = int(c)
  print (d)

		# --> 7

  e = 5.9
  f = int(e)
  print (f)

		# --> 5
		
****************************************************************************************************************************
	03 - BOOLEAN
****************************************************************************************************************************
  
# Booleans returns only 'True' or 'False'

  a = 9
  b = 6
  print (a == b)
  print (a != b)

		# --> False
		# --> True

  a = 'Router01'
  b = 'router_02'
  print (a == b)
  
		# --> False

  x = True
  y = False
  
  print (a or b)
  print (a and b)
  print (a or a)
  print (a and a)
  print (b and b)

		# --> True
		# --> False
		# --> True
		# --> True
		# --> False
		
****************************************************************************************************************************
	04 - LIST
****************************************************************************************************************************
  
# Lists are the object type called list, and at their most basic level are an ordered sequence of objects.

  hostnames = ['r1' , 'r2' , 'r3' , 'r4' , 'r5']
  commands = ['conf t' , 'interface Ethernet1/1' , 'no shutdown']

# Each object can be different data type

  my_list = ['router1' , False , 3]
  
# Can be use each element from list

  voiceinterfaces = ['Eth1/1' , 'Eth1/2' , 'Eth1/3' , 'Eth1/4']

  print(voiceinterfaces[0])           
  
		# --> Eth1/1
		
  print(voiceinterfaces[1])           

		# --> Eth1/2
  
****************************************************************************************************************************
	SOME METHOD of LIST CLASS
****************************************************************************************************************************
  
  voice_interfaces = ['Eth1/1' , 'Eth1/2']
  data_interfaces = ['Eth1/1' , 'Eth1/2' , 'Eth1/3' , 'Eth1/4']

  voice_interfaces.append('Eth1/3')
  print(voice_interfaces)

		# --> ['Eth1/1', 'Eth1/2', 'Eth1/3']

  voice_interfaces.clear()
  print(voice_interfaces)

		# --> []

  print (data_interfaces.index('Eth1/4'))

		# --> 3

  data_interfaces.insert(3, 'Eth1/5')
  print (data_interfaces)

		# --> ['Eth1/1', 'Eth1/2', 'Eth1/3', 'Eth1/5', 'Eth1/4']

  data_interfaces.append('Eth1/6')
  print(data_interfaces)

		# --> ['Eth1/1', 'Eth1/2', 'Eth1/3', 'Eth1/5', 'Eth1/4', 'Eth1/6']

  data_interfaces.remove('Eth1/2')
  print (data_interfaces)

		# --> ['Eth1/1', 'Eth1/3', 'Eth1/5', 'Eth1/4', 'Eth1/6']

  data_interfaces.pop()
  print(data_interfaces)

		# --> ['Eth1/1', 'Eth1/3', 'Eth1/5', 'Eth1/4']
		
  data_interfaces.pop(1)
  print(data_interfaces)

		# --> ['Eth1/1', 'Eth1/5', 'Eth1/4']

  data_interfaces.sort()
  print(data_interfaces)
  
		# --> ['Eth1/1', 'Eth1/4', 'Eth1/5']

  port_status = ['connected' , 'notconnected', 'notconnected', 'notconnected' , 'connected']

  print (port_status.count('connected'))
  print (port_status.count('notconnected'))

		# --> 2
		# --> 3

****************************************************************************************************************************
	05 - TUPLE
****************************************************************************************************************************
  
''' 

  The tuple is an interesting  data type and also best understood when compared to a list. It is like a list, but cannot be
  modified. We saw that lists are  mutable, meaning that it is  possible to update, extend, and modify them. Tuples, on the 
  other hand, are immutable, and it is not possible to modify them once they’re created. Also, like lists, it’s possible to
  access individual elements of tuples.
 
''' 
  
  deviceslist = ['cisco', 'juniper', 'HP', 'Dell', 'Huawei', 'cisco']
  print(type(devicelist))

		# --> <class 'list'>

  devicetuple = tuple(deviceslist)
  print (devicetuple)
  print(type(devicetuple))

		# --> ('cisco', 'juniper', 'HP', 'Dell', 'Huawei', 'cisco')
		# --> <class 'tuple'>

  print (devicetuple.count('cisco'))

		# --> 2

  print (devicetuple.index ('cisco'))

		# --> 0

  print (devicetuple[1])

		# --> juniper

  print (devicetuple[1:3])

		# --> ('juniper', 'HP')

  device_short_list = devicetuple[0:2]
  print (device_short_list)
  print (type(device_short_list))

		# --> ('cisco', 'juniper')
		# --> class 'tuple'>
		
****************************************************************************************************************************
	06 - SET
****************************************************************************************************************************
		

'''

  If you understand lists, you’ll understand sets. Sets are a list of elements, but there can only be one of a given element
  in a set, and additionally elements cannot be indexed.
		
'''

  deviceslist = ['cisco', 'juniper', 'HP', 'Dell', 'Huawei', 'cisco']

  device_set = set (deviceslist)
  print (device_set)

		# --> {'Huawei', 'HP', 'Dell', 'juniper', 'cisco'}
		
  device_set.pop()
  print (device_set)

		# --> {'Dell', 'Huawei', 'cisco', 'juniper'}
		# The pop() method removes a random item from the set. This method returns the removed item.

  device_set.pop(0)
  print (device_set)

		# --> TypeError: pop() takes no arguments (1 given)

  device_set.remove('Dell')
  print (device_set)
		
		# --> {'Huawei', 'cisco', 'juniper'}

****************************************************************************************************************************
	ADD \OR UPDATE USING SET
****************************************************************************************************************************

  deviceset_1 = {'Huawei', 'Cisco', 'Juniper'}
  deviceset_2 = {'Arista', 'Dell'}

  deviceset_1.update(deviceset_2)
  print (deviceset_1)

		# --> {'Arista', 'Juniper', 'Cisco', 'Dell', 'Huawei'}

  deviceset_1.add('Apple')
  print (deviceset_1)

		# --> {'Arista', 'Juniper', 'Cisco', 'Apple', 'Dell', 'Huawei'}

  deviceset_1.update('Meraki')
  print (deviceset_1)

		# --> {'r', 'Dell', 'Huawei', 'e', 'a', 'Arista', 'M', 'i', 'k', 'Juniper', 'Cisco', 'Apple'}
		
****************************************************************************************************************************
	07 - DICTIONARY
****************************************************************************************************************************
	
'''

   We’ve now reviewed  some of the most common data types, including strings, integers, booleans, and lists, which exist across
  all programming languages. In this section we take a look at  the dictionary, which is a  Python-specific data type. In other 
  languages, they  are known  as associative arrays, maps, or hash  maps. Dictionaries are unordered lists and their values are 
  accessed  by names, otherwise known as keys, instead of by index (integer). Dictionaries are simply a collection of unordered
  key-value pairs called items.
		
'''

  devices = {'vendor': 'cisco', 'hostname': 'router01', 'OS': 'IOS-XE'}
  print(type(devices))

		# --> <class 'dict'>

  print(devices.keys())

		# --> dict_keys(['vendor', 'hostname', 'OS'])

  print(devices.values())

		# --> dict_values(['cisco', 'router01', 'IOS-XE'])

  print (devices.items())

		# --> dict_items([('vendor', 'cisco'), ('hostname', 'router01'), ('OS', 'IOS-XE')])

  print(devices['vendor'])

		# --> cisco
		
  copy_devices = devices.copy()
  print (copy_devices)
  
		# --> {'vendor': 'cisco', 'hostname': 'router01', 'OS': 'IOS-XE'}

****************************************************************************************************************************
	08 - FILE
****************************************************************************************************************************

'''

  The key function for working with files in Python is the open() function. The open() function takes two parameters; filename
  and mode.

	"r" - Read - Default value. Opens a file for reading, error if the file does not exist
	"a" - Append - Opens a file for appending, creates the file if it does not exist
	"w" - Write - Opens a file for writing, creates the file if it does not exist
	"x" - Create - Creates the specified file, returns an error if the file exists
	
'''
  #EXP-1
  test_file = open("testfile.txt", "w")
  test_file.write("Bu bir deneme yazısıdır")
  test_file.close()

  x = open('testfile.txt')
  print(x.read())

  #EXP-2
  dosya = open('RT_01.txt', 'x')
  dosya.write('conf t\ninterface gigabitethernet0/1\nno shutdown\n')
  dosya.close()

  x = open('RT_01.txt')
  print(x.read())
		
		