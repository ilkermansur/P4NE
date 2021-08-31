

'''
                         *******        *******         ****     **       ********
                        /**////**      /**////**       /**/**   /**      /**///// 
                        /**   /**      /**   /**       /**//**  /**      /**      
                        /*******       /*******        /** //** /**      /******* 
                        /**////        /**///**        /**  //**/**      /**////  
                        /**            /**  //**       /**   //****      /**      
                        /**            /**   //**      /**    //***      /********
                        //             //     //       //      ///       //////// 
                        
COMMON DATA TYPE IN PYTHON

04 - LISTS
05 - TUPLE
06 - SET
07 - DICTIONARY

'''

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
