
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

01 - STRINGS
02 - INTEGERS,FLOAT
03 - BOOLEANS

'''
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
		
