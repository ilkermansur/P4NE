"""

COMMON DATA TYPE IN PYTHON

# 01 - STRINGS
# 02 - INTEGERS,FLOAT
# 03 - BOOLEANS
# 04 - LISTS
# 05 - TUPLES
# 06 - DICTIONARIES
# 07 - FILES

"""






"""
***********************************************************************************************************************
   01 - STRINGS
*********************************************************************************************************************** 
"""

# String can use single, double quotes

ip_1 = '10.0.0.1'
print (ip_1)                        # --> 10.0.0.1

ip_2 = "10.0.0.2"
print (ip_2)                        # --> 10.0.0.2

# or both

Einstein = "If you can't explain it simply, you don't understand it well enough"
print (Einstein)                    # --> If you can't explain it simply, you don't understand it well enough

#   STRING OPERATIONS

# You can add strings together to concatenate them

ipaddr = ip_1 + ip_2
print (ipaddr)                      # --> 10.0.0.110.0.0.2

# You can use whitespace between strings

ipaddr = ip_1 + ' ' +ip_2
print (ipaddr)                      # --> 10.0.0.1 10.0.0.2

# Easy way to add more whitespace between strings another words strings can be multiply

ipaddr = ip_1 + ' '*10 +ip_2
print(ipaddr)                       # --> 10.0.0.1          10.0.0.2

# You can't add strings and numbers

age = 40
print("You are " + age)             # --> TypeError: can only concatenate str (not "int") to str

# But you can if you turn the number into a string first:
age = 40
age_as_string = str(40)
print("You are " + age_as_string)

#   SOME ESCAPE CHARACTERS '\n' '\t' '\'

Einstein = "If you can't explain it simply,\n you don't understand it well enough"
print (Einstein)

# --> If you can't explain it simply,
#      you don't understand it well enough

Einstein = "If you can't explain it simply,\n\n you don't understand it well enough"
print (Einstein)

# --> If you can't explain it simply,

#      you don't understand it well enough

nameandsurname = 'ilker\tmansur'    # --> ilker     mansur
print (nameandsurname)



Einstein = 'If you can\'t explain it simply, you don\'t understand it well enough'
print (Einstein)

# You can use index for specific character  of  the string

adsoyad = 'ilker mansur'
print(adsoyad[0])                   # —> i
print(adsoyad[1])                   # —> l
print(adsoyad[2])                   # —> k
print(adsoyad[3])                   # —> e
print(adsoyad[4])                   # —> r
print ('\n')

# or specific part of string

print (adsoyad[0:])                 # —> ilker mansur
print (adsoyad[6:])                 # —> mansur
print (adsoyad[:6])                 # —> ilker
print(adsoyad[2:4])                 # —> ke

# Actually data types ,that we use, are classes at the same time<class 'str'>

print (type (adsoyad))              # —>  <class 'str'>

# Some method of 'str' class

adsoyad = "ilkermansur"

print(adsoyad.startswith("i"))      # --> True (this is 'boolean' type)

print(adsoyad.startswith("l"))      # --> False (this is 'boolean' type)

adsoyad = "     ilkerm       "

print(adsoyad)                      # --> '      ilkerm     '
print(adsoyad.strip())              # --> 'ilkerm'
print(adsoyad.lstrip())             # --> 'ilkerm    '
print(adsoyad.rstrip())             # --> '    ilkerm'

ipaddr = "10.0.0.1"
print(ipaddr.replace("0","11"))     # --> '111.11.11.1'
print(ipaddr.count("0"))            # --> '3'

print(ipaddr.replace('0','11',2))   # --> '111.11.0.1'

ipaddr = '10.0.0.1 255.255.255.0'
print(ipaddr.split())               # --> ['10.0.0.1', '255.255.255.0']

print(ipaddr.split(sep='.'))        # --> ['10', '0', '0', '1 255', '255', '255', '0']

"""
***********************************************************************************************************************
   02 - INTEGERS and FLOAT
***********************************************************************************************************************
"""

number = 10

print(type(number))                 # --> <class 'int'>

number = 10.0

print(type(number))                 # --> <class 'float'>

# In network automation scripts, use str for expressing ip address instead of integer because of syntax

ipaddr_int = 10.0.0.1
ipaddr_str = '10.0.0.1'

# MATH with operator ('+' '-' '*' '/' '//' '%')

a = 9
b = 2

c = a + b
print (c)                           # --> 11

c = a - b
print (c)                           # --> 7

c = a * b
print (c)                           # --> 18

c = a ** b
print (c)                           # --> 81

c = a / b
print (c)                           # --> 4.5

c = a // b
print (c)                           # --> 4

c = a % b
print (c)                           # --> 1

"""
***********************************************************************************************************************
   03 - BOOLEANS
*********************************************************************************************************************** 
"""

# Booleans returns only 'True' or 'False'

a = 3
b = 5

print (a == b)                      # --> False
print (a != b)                      # --> True

a = 'Router01'
b = 'router01'

print (a == b)                      # --> False

A = True
B = False

print (A or B)                      # --> True
print (A and B)                     # --> False
print (A or A)                      # --> True
print (B or B)                      # --> False
print (A and A)                     # --> True
print (B and B)                     # --> False

"""
***********************************************************************************************************************
   04 - LISTS
*********************************************************************************************************************** 
"""

# Lists are the object type called list, and at their most basic level are an ordered sequence of objects.

hostnames = ['r1' , 'r2' , 'r3' , 'r4' , 'r5']
commands = ['conf t' , 'interface Ethernet1/1' , 'no shutdown']

# Each object can be different data type

list = ['router1' , False , 3]

# Can be use each element from list

voiceinterfaces = ['Eth1/1' , 'Eth1/2' , 'Eth1/3' , 'Eth1/4']

print(voiceinterfaces[0])           # --> Eth1/1
print(voiceinterfaces[1])           # --> Eth1/12

datainterfaces = ['Eth1/5' , 'Eth1/6']

print (datainterfaces[0])           # --> Eth1/5

print (voiceinterfaces)             # --> ['Eth1/1', 'Eth1/2', 'Eth1/3', 'Eth1/4']
print (datainterfaces)              # --> ['Eth1/5', 'Eth1/6']

# You can see that using append() adds the element to the last position in the list.

voiceinterfaces.append('Eth1/5')
print (voiceinterfaces)             # --> ['Eth1/1', 'Eth1/2', 'Eth1/3', 'Eth1/4', 'Eth1/5']

# To use insert(), you need to pass it two arguments. The first argument is the position, or index, where the new
# element gets stored, and the second argument is the actual object getting inserted into the list.

voiceinterfaces.insert(0 , datainterfaces)
print (voiceinterfaces)             # --> [['Eth1/5', 'Eth1/6'], 'Eth1/1', 'Eth1/2', 'Eth1/3', 'Eth1/4', 'Eth1/5']

# Extend is different from insert. Need only one argument and add value as an element NOT list

voiceinterfaces.extend(datainterfaces)

print (voiceinterfaces)             # --> ['Eth1/5', 'Eth1/6', 'Eth1/1', 'Eth1/2', 'Eth1/3', 'Eth1/4', 'Eth1/5']

# You can count how many instances of a given object are found by using the count() method.

p_s = ['connected' , 'notconnected', 'notconnected', 'notconnected' , 'connected']
print(p_s.count('notconnected'))    # --> 3
print(p_s.count('connected'))       # --> 2

# Pop and index usage is so simple for discard element from end of list or specific index.

voiceint = ['Eth1/1' , 'Eth1/2' , 'Eth1/3' , 'Eth1/4']

voiceint.pop()
print (voiceint)                    # --> ['Eth1/1' , 'Eth1/2' , 'Eth1/3']

voiceint.pop(1)                     # --> ['Eth1/1', 'Eth1/3']
print(voiceint.index('Eth1/3'))     # --> 1




