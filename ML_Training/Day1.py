# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

lstnew=[1,5,'hey']
lstnew.append('new val')
print(lstnew)
lstnew.insert(2,'i am here')



if len(lstnew)>0:
    print(lstnew)
    
test1='Hey\tMan'.expandtabs()
print(test1)

temp='This is a temporary script file'
temp1=temp.partition('a')
print(temp1)
print(type(temp1))


#list compression
listCompression={x:x**2 for x in range(10)}
print(listCompression)


def sum_list(list1):
        sum1=0
        val1=50000
        for val in list1:
            sum1=sum1+val
        return sum1, val1

sum_list1=(1,5,3,7,8)
sumval,val1=sum_list(sum_list1)
print(sumval)
print(val1)



# map function
temp=[3,7,34,98]
mapoutput=list(map(lambda x:(x+8),temp))
print(mapoutput)


# reduce function
from functools import reduce
temp1=[3,7,34,98]
output=reduce(lambda x,y:x+y,temp1)
print(output)


# filter function



numbers = {5: '5, heythis is', 4: '4, heythis is', 8: '8, heythis is'}

sort_nmbers=sorted(numbers)
print(sort_nmbers)
for keys in sort_nmbers:
    print(numbers[keys])
    

import csv

zegamiDictionary={}
zegamiDictionary['1']="'ID':'1' , 'Treatment':'1 key, 1 value'"
zegamiDictionary['5']="'ID':'5' , 'Treatment':'5 key, 5 value'"
zegamiDictionary['2']="'ID':'2' , 'Treatment':'2 key, 2 value'"

sort_zegami=sorted(zegamiDictionary)


'''	
with open('C:\PSTL\Purdue_PSTL\SMS\Purdue_Audit\zegami.csv', mode='w') as csv_file:
    fieldnames = ['ID', 'Treatment']

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)	
    writer.writeheader()
    
    print(sort_zegami)
    
    for keys in sort_zegami:
        print(zegamiDictionary[keys])
        print(writer.writerow({zegamiDictionary[keys]}))
    
    
    #writer.writerow({'ID':'1' , 'Treatment':'1 key, 1 value'})
    #writer.writerow({'ID':'5' , 'Treatment':'5 key, 5 value'})
    #writer.writerow({'ID':'2' , 'Treatment':'2 key, 2 value'})
    
    
    
    
    print('CSV Saved At :','C:\PSTL\Purdue_PSTL\SMS\Purdue_Audit\zegami.csv')
'''

with open('C:\PSTL\Purdue_PSTL\SMS\Purdue_Audit\zegami.csv', mode='w') as csv_file:
    fieldnames = ['ID', 'Treatment']

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)	
    writer.writeheader()
  
    
    writer.writerow({'ID':'1' , 'Treatment':'1 key, 1 value'})
    writer.writerow({'ID':'5' , 'Treatment':'5 key, 5 value'})
    writer.writerow({'ID':'3' , 'Treatment':'3 key, 3 value'})
    



import csv

myData0 = [['ID','Treatment','misc']]

myData = [['1', 'Good Evening', 'Good Afternoon']] 
myData1 = [['2', 'Good Evening dfsd', 'Good Afternoon']] 

print(type(myData1))

 
myFile = open('C:\PSTL\Purdue_PSTL\SMS\Purdue_Audit\csvexample3.csv', 'w')
  
with myFile:  
   writer = csv.writer(myFile)
   
   writer.writerows(myData0)   
   writer.writerows(myData)
   writer.writerows(myData1)
   
   listMydata = ['3', 'Good Evening dfsd', 'Good Afternoon']
   listMynew=[listMydata]
   writer.writerows(listMynew)
   
   print(type(listMydata))
   

