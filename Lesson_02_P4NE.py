'''

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



CONDITIONS and LOOPS in PYTHON

01 - IF-ELIF-ELSE
02 - LOOPS in PYTHON

'''

****************************************************************************************************************************
	IF / ELSE / ELIF
****************************************************************************************************************************

'''

   There are two things to take note of with regard to syntax when you’re working with an if statement. First, all if statements
   end with a colon (:).  Second, the code that  gets  executed if your  condition  is true is part of an indented block of code

'''

  # EXP-1
  
  a = 5
  b = 4
  c = a + b

  if c == 10:
	  print ('c is equal "10" ')
  else:
	  print ('c is not equal 10')
	  
		# --> c is not equal "10" 

  if c != 10:
	  print ('c is not equal "10" ')
  else:
	  print ('c is equal "10" ')
	  
		# --> c is not equal "10" 
		
  # EXP-2
  
  number = input('Enter a number: ')
  number = int(number)
  
  if 50 <= number <= 100:
	  print (" your number is between 50 and 100")
  elif number <= 50:
	  print (" Your number is smaller then 50")
  else:
	  print (" Your number is bigger then 100")
  
  # EXP-3
  
  our_staff_list = ['ahmet', 'ayla', 'bilal', 'berrin']
  staff = input ('Lütfen isminizi giriniz :')

  if staff in our_staff_list:
  print ('Merhaba '+staff+ ' hoşgendin')
  else :
  print ('ya ismini bilmiyorsun ya da personelimiz değilsin, iki koşulda da burada işin yok malesef')
  
  # EXP-5
  
  version = "CSR1000V Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.3.1, RELEASE"
  if '16.3' in version:
  print ('Your device is up to date')

		# --> Your device is up to date
		
****************************************************************************************************************************
	LOOPS in PYTHON
****************************************************************************************************************************
  
  '''
  
  The general premise behind a while loop is that some set of code  is executed while  some condition is true. The syntax required 
  is similar to what we used when creating if-elif-else statements. The while statement is completed with a colon (:) and the code 
  to be executed is also indented four spaces.
  
  '''
  
  # EXP-1
  
  counter = 1
  
  while counter <= 5:
	  print (counter)
	  counter += 1
  print ('End of loop')
  
		# --> 1
		# --> 2
		# --> 3
		# --> 4
		# --> 5
		# --> End of loop
		
  # EXP-2
  
  counter = 1
  
  while counter <= 5:
	  if counter % 2 == 0:
		  print (counter, ' is even number')
		  counter += 1 
	  else:
		  print (counter, ' is odd number')
		  counter += 1 
  print ('End of loop')
  
		# --> 1 is odd number
		# --> 2 is even number
		# --> 3 is odd number
		# --> 4 is even number
		# --> 5 is odd number
		# --> End of loop
  
  # EXP-3
  
  vendor_list = ['cisco', 'juniper', 'dell']
  for vendor in vendor_list:
	  print (vendor)
  
		# --> cisco
		# --> juniper
		# --> dell
   
  # EXP-4
  # Find prime numbers between 2 numbers
  
  num_1 = 1
  num_2 = 15

  for num in range (int(num_1),int(num_2)+1):
	  if num > 1:
		  for i in range (2,num):
			  if num % i ==0:
				  break
		  else:
			  print (str(num)+ ' is prime number')
  

		# --> 2 is prime number
		# --> 3 is prime number
		# --> 5 is prime number
		# --> 7 is prime number
		# --> 11 is prime number
		# --> 13 is prime number
		
