'''
Created on Feb 10, 2018

@author: KRG
'''

a,b,c,d = 1,2.55,"john","Y"

print(a)
print(b)
print(c)
print("Nothing: "+d)

# Numbers


# String
strs = 'Hello World!'
print (strs)       # Prints complete string
print (strs[0])     # Prints first character of the string
print (strs[2:5])    # Prints characters starting from 3rd to 5th
print (strs[6:])      # Prints string starting from 3rd character
print (strs * 2)      # Prints string two times
print (strs + " TEST"+'\n') # Prints concatenated string


# List
lists = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
lists[2] = 1000  
print (lists)          # Prints complete list
print (lists[0])       # Prints first element of the list
print (lists[1:3])     # Prints elements starting from 2nd till 3rd 
print (lists[2:])      # Prints elements starting from 3rd element
#print (tinylist * 2)  # Prints list two times
print (lists + tinylist) # Prints concatenated lists
print('\n')

# Tuple
tuples = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')
#tuples[2] = 1010
print (tuples)           # Prints complete list
print (tuples[0])        # Prints first element of the list
print (tuples[1:3])      # Prints elements starting from 2nd till 3rd 
print (tuples[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints list two times
print (tuples + tinytuple) # Prints concatenated lists
print('\n')

# Dictionary
dicts = {}
dicts['one'] = "This is one"
dicts[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dicts['one'])       # Prints value for 'one' key
print (dicts[2])           # Prints value for 2 key
print (tinydict.get("dept"))          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values