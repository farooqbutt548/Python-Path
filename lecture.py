'''# ----String
numbers = (1,2,3)
name1 = ['abc', 'bcd','cde', 'def']

# ----numbers
integer = [1,2,3,4,5]
floate = [1.2, 2.33,4.0]
complexe = (10+2-j)
esj'''
# input("\n\nPress the enter key to exit."); input("\n\nPress the enter key to exit."); input("\n\nPress the enter key to exit.")
#<button></button> successfully
# ----operators
    # -- Addition
'''a = 5 ; b = 11
print(a+b)
    # --Subtraction
print(b-a)
    # --Multiplication
print(a*b)
    # --Division
print(b/a); print(b//a)
    # --Modulus
print(b%a) 
    # --Exponent(power)
print(2**3)

print(a!=b)

    # ---in
name =[1,2,3,4,5,6]
if 2 in name:
    print('it\'s is present')
if 7 not in name:
    #123
    print("it's true statement") '''


                # ---Loops
#  we can get output of while_loop with for_loop and vise versa

                        # -- while_loops
'''num = int(input('enter a n_num to their sum : '))
total = 0
i = 0
while i <= num:
    total += i
    i += 1
print(f"the total sum is : {total}") '''

# while_loop with slicing      1234 = 1+2+3+4
'''number = input('enter numbers : ')
total = 0
i = 0
while i < len(number):
    total += int(number[i])
    i += 1
print(total)'''
# name letter count with while loof
'''name = input('enter your name : ')
temp_cell = ''
i = 0
while i < len(name):
    if name[i] not in temp_cell:
        temp_cell += name[i]
        print(f'the char {name[i]} is {name.count(name[i])} times in {name}')
    i +=1'''
                # ---for_loop

# sum via slicing
'''total = 0
number = input('plz enter a num to addition : ')
for i in range(0, len(number)):
    total += int(number[i])
print(total)'''
# sum of n_num with For_loop
'''num = int(input('plz enter a n_num to addition : '))
total = 0
for i in range(0,num+1):
    total+= i
print(total)'''
# letter_count with for loop
'''name = input('enter name to letter count : ')
cell = ''
for i in range(len(name)):
    if name[i] not in cell:
        cell += name[i]
        print(f'the "{name[i]}" in "{name} : {name.count(name[i])}" timkes.')'''
        # Exercise if with In-keyword
'''name = input('enter some text : ')
letter = input('enter desired letter : ')
if letter in name:
    print(f"Yup! your letter '{letter}' is present in '{name}' ")
else:
    print(f"Nop! your letter '{letter}' is not present in '{name}' ")'''
                                #Numbers 
#integer Numbers
'''int_nums =50
float_nums = 3.1428
complex_nums = 2+3j
print(type(int_nums)) # interger
print(type(float_nums)) # float 
print(type(complex_nums)) # complex
print(2+2)  #integer
print(type(2+2.33))  #flout
print(f"we can type int, float here {2+2}, .... ")
new_float = int_nums+float_nums
print(new_float)
print(type(new_float))  #  float'''
                            #  Strings

# Simple String
'''string1 = ' this is 1st string,  '
string2 = "this is 2nd string"
print(type(string1))
connect_string = string1+ " "+string2
print(connect_string)
# print("errer"+3)  erreor
print('this is not error'+' ' + str(3))
print('this will print 3 times'*3 )'''
# f-string, string-formatting
'''f_name = 'farooq'
l_name = 'butt'
print(f'hello {f_name} {l_name} how are you.')
# string input via split method()
name, age,degree = input('enter your name, age & degree comma separated : ').split(',')
print(f'hello {name} your age is {age} & degree is {degree}.')
# string indexing 
name_index = 'farooq butt'
print(name_index[1])  #2nd number char will print from left
print(name_index[-1]) #last char will print
print(name_index[2:6:1])   #  string slicing [start:ending:step]
print(name_index[ : :-1])  #    reverse string'''

# string exercice 
#  name in reversed order 
'''name = input('enter your naem : ') ; print(name[::-1])'''
#  string methods
'''word = 'abCdefgHijKlmnOpqRsTuvwXyz'
print(len(word))    # leangth of word
print(word.lower())  # for lower letters
print(word.upper())  # for upper letters
print(word.count('b'))  # for count a letter in word
print(word.title())  # for first letter capital
print(word.center(80)) # for aligning text '''
                    
                    # -----List 
# List basic 

'''list_data = [1,2,3,4,5,'faroooq', 'butt', 'zaheer','irshad', 2.33,55.9]
print(list_data[4])    # 5th position 
print(list_data[ : 4])   # first 5 
print(list_data[:7:2])   # among first 8 with 2 step
list_data[2]='three'       # change 3rd index value (mutable)
print(list_data)
print(type(list_data))'''
# list add values 
'''name = [ 'farooq', 'zaheer', 'touseef']
degree = ['BS-IT', 'BS-SE', 'BS-CS']
name.append('butt')   # add at last index
print(name)
name.insert(1, 'engineer')  # add at desired index (i like this method not append)
print(name)
print(name+degree)      # concatination two lists
name.extend(degree)  # joined both lists, name & degree
print(name)     # now name has all values'''
# list remove data 
'''uni = ['UOS', 'NUST', 'MY-UNI', 'NUT', 'UOS','LUMS', 'NFC', 'UET', 'UOJ']
print(uni.pop())  # last element poped 'UOJ'
print(uni)   # UOJ is popped
del (uni[2])
print(uni)   # 3rd my-uni is deleted
uni.remove('NFC')  # remove via name if available
print(uni)'''
# other methods in list 
'''print(uni.count('UOS'))         # count the element in list
nums =[2 ,3 ,8.44 , 6 ,5.32 , 8 ,1 ,4 ]
nums.sort()          # sorted by numbers
print(nums)
new_copy_list = nums.copy()         # copy all daya and past in new list
alphabits = ['b','d','g','s','e','c','a','f']
print(sorted(alphabits))   # sorted for this line not change list value
alphabits.sort()           # sorts alphabitically 
print(alphabits)
alphabits.clear()
print(alphabits)            # clear all data '''
# == , is difference in list
'''name1 = ['python', 'java','kotlin', 'ruby', 'c++']
name2 = ['python', 'java','kotlin', 'ruby', 'c++']
print(name1 == name2)   # values are equal  (True)
print(name1 is name2)   # values are same but not same memory location (False)'''
# convertion of lists to string and to list
'''name = input('enter your name :').split()  # string to list
print(name)         # will make list seperated by spaces
name1, name2, name3 = 'farooq butt kashmiri'.split()
print(name1, name2, name3)
# list to string 
cities = ['faisalabad ' ,'lahore ', 'islamabad ', 'rawalpindi ']
print(','.join(cities))        # convert list to string '''
# Loops in list 
'''laptops = ['dell', 'hp','lenavo', 'apple mac', 'l.g']
for i in laptops:
    print(i)'''
# nested loop in list
'''datam = [['a','b', 'c'],['d','e', 'f'],['g', 'h','i']]
for data in datam:
    for i in data:
        print(i)
print(datam[1][1])   # indext 2 of 2nd element (e)'''
 # to make list first 15 naturel nums
'''make_list =list(range(1,16))
print(make_list)'''

                        # ----- Tuple 

'''tup1 = (1,2,3,4,5,6.0)
for i in tup1:              # we can use while loop too
    print(i, end=' ')

uni_tuple = (1,)          # is tuple not int
print(type(uni_tuple))
also_tuple = tuple (range(1,11))
print(type(also_tuple))

unies = 'UOS', 'NUST', 'UET', 'FAST', 'MYU', 'AIOU'
print(type(unies))          # tuples without bracess
# List in Tuple (Tuple is immutable but list in it is mutable)
list_tuple = (1,5, 'butt', ['first', 'second', 'last'])
list_tuple[3].pop()
print(list_tuple)       # 'last' will be removed
list_tuple[3].append('new last')
print(list_tuple)
print(min(tup1))
print(max(tup1))
print(tup1+tup1)'''

                                              # ---- Dictionary

'''designation = {'farooq':'c.e.o', 'zaheer':'cfo', 'waqas': 'accountant'}     # dictionary (key:value)
print(designation)
print (type(designation))
marks = dict (ict = 97, dld= 88, algebra = 87, ai = 55)     # dict method is used (i like this method)
print(marks)
print(type(marks))

print(designation['zaheer'])
# simple dictionary
bio = dict(name = 'farooq',
 age= 25,
  degree = 'BS-IT',
   roll_num = 660,
    City = 'Faisalabad',
     Phon = 923015902110)
print(bio['degree'])
                    # dictionary in dictionary
phon_num = dict(
    farooq = dict(jazz = 923015902110, zong = 923179600604),
    afzal = dict(jazz =  923004049286, zong = 923184049286),
    zaheer = 923007663624
)
print(phon_num)
print(phon_num['farooq']['zong'])       # access dictionary in dictionary value

                    # Add in Dictionary 
empty = {}
empty['sargodha'] = 'UOS'
empty['lahore'] = 'UET'
empty['islamabad'] = 'AIOU'
empty['faisalabad'] = 'GCUF'
print(empty)
del empty['faisalabad']     # delete the (key :value)
print(empty)

alphabet = dict(a='b', c='d', e='f')
alphabet.clear()           # will delete all entire entries
print(alphabet)

city = input('input city : ')
if city in empty:                           # for finding key. for integer we will make it int form
    print('Yup! here in dictionary.')       
else:
    print('Nope! not in dictionary.')

uni = input('input uni : ')
if uni in empty.values():                           # for finding value 
    print('Yup! here in dictionary.')       
else:
    print('Nope! not in dictionary.')

empty = {}
empty['sargodha'] = 'UOS'
empty['lahore'] = 'UET'
empty['islamabad'] = 'AIOU'
empty['faisalabad'] = 'GCUF'
print(empty.values())               # -------- all values will print
for i in empty.values():    
    print(i)                        # -------- all values will print

for i in empty.keys():                     # -------- all keys will print.... (either use key method or not)
    print (i)

                                        # ---------- items method
empty = {}
empty['sargodha'] = 'UOS'
empty['lahore'] = 'UET'
empty['islamabad'] = 'AIOU'
empty['faisalabad'] = 'GCUF'
item_method = empty.items()         # make a list of tuples of key, values
print(item_method)
print(type(item_method))
# Example of item method
for city, uni in empty.items():
    print(f'the {city} has {uni} populer university')      # looping with item method

new_empty = empty.pop('faisalabad')         # popped item stored in new_empty
print(new_empty)
print(type(new_empty))
print(empty)                    # faisalabad is popped 

news_empty = empty.popitem()    # randomply pop and save in variable
print(news_empty)
print(type(news_empty))
                                    # -------- update method
student = dict(name = 'farooq', 
                    caste = 'kashmiri',
                    roll_num = 660,
                    uni = 'UOS',
                    degree = 'BSIT')

more_info = dict( home_town = 'faisalabad',
                    adress = 'orchards home',
                    name = 'Muhammad Farooq',
                    cell_num = 923015902110)
print(student)
print(more_info)
student.update(more_info)
print(student)                  # merge both info and 'name' will update as of more_info
student.update({})
print(student)                  # nothing will update same previos information
            # ------- get method
print(more_info.get('adress'))          # value of adress
print(more_info.get('adresses'))        # give 'none' not error
# copy method 

a = dict(name = 'farooq', caste = 'butt', age = 25)
b= a.copy()             # two same but different dictionary , a! = B
a.pop('age')
print(a)
print(b)

# EXERCISE No. 1     (key, key*3)
def cube_finder(n):
    cubes = {}
    for i in range(1,n+1):
        cubes[i] = i**3
    return cubes
print(cube_finder(10))

# EXERCISE No. 2    (key, key*2) 
def twice(n):
    twice_dict = {}
    for i in range(1,n+1):
        twice_dict[i] = i*2
    return(twice_dict)

print(twice(10)) 
# EXERCISE No. 3
def info (data):
    info_dict = {}
    a = input('enter name : ')
    b = input('enter age :')
    c = input('enter degree :')
    d = input('enter uni :')
    e = input('enter number :')
    info_dict['name'] = a
    info_dict['age'] = b
    info_dict['degree'] = c
    info_dict['uni'] = d
    info_dict['number'] = e
    return(info_dict)

data = {}
print(info(data).items())  '''

                            # -------------   Date & Time 

'''import datetime as dt

date1 = dt.date.today()      # today date complete
print(date1)

print('years are ',date1.year)       # individual year
print('months are ',date1.month)      # individual month
print('days are ', date1.day)         # individual day


date2= dt.time(8, 36,33, 122212)
print('time is : ', date2)

print('houres are  : ', date2.hour)
print('minutes are : ', date2.minute)
print('seconds are : ', date2.second)
print('microseconds are : ', date2.microsecond)
                # --date & time combine
datetime_obj = dt.datetime(2021, 8,31, 23,59,59,999999)
print(datetime_obj)

print('the only date is : ',datetime_obj.date())
print('the only time is : ',datetime_obj.time())
print('the only years is : ',datetime_obj.year)
print('the only hours is : ',datetime_obj.hour)
        # -- current date time & datetime differences
current_dt = dt.datetime.now()        # today() or now()
print('current date & time is : ', current_dt)

birth_date = dt.datetime(1995, 4, 20, 8,37,12)      # selective datetime
print('your birth date is : ',birth_date)

my_age = current_dt-birth_date                  # date time difference
print('my actual age is : ', my_age)

print(type(current_dt))     # datetime type
print(type(birth_date))
print(type(my_age))         # difference two dates is timedelta obj

                            # Month of the year
import calendar as cal
mon = cal.month(1947, 8, 3)
print(mon)'''


#                               --------also can be used
'''import datetime
import calendar      

dt = datetime.datetime.now()            # current time and date
print (dt)

# print('years are: ',dt.year)            # individual time and date
# print('months are: ',dt.month)
# print('days are: ',dt.day)
# print('hour are: ',dt.hour)
# print('minutes are: ',dt.minute)
# print('seconds are: ',dt.second)
# print('microseconds are: ',dt.microsecond)

# all_cal = calendar.calendar(2021)          # all months of the year
# print(all_cal)

# cal = calendar.month(2022,4)            # specific month calendar
# print(cal)

# print('an other way to print month: ', datetime.datetime.now().month, 'mean September')
#           format of time and date

print(dt.strftime('the date is: %a, %dth %b, %Y'))  # %a,%A = day, %d=date, %b=month, %y,%Y=year'''
'''import time
t = time.localtime()
print(t)            # all type of time and date

print('years : ',t.tm_year)         # individual time or date
print('months : ',t.tm_mon)
print('days : ',t.tm_mday)
print(' hours :',t.tm_hour)
print(' minutes :',t.tm_min)
print(' seconds :',t.tm_sec)'''

                           # -------------------    Modules 
#          ---------type(1)

# addition and subtraction simple module add(), sub()
'''import module1              # simple module name
print(module1.add(3,4))
print(module1.sub(8,4))

# Febonacci Sequance n-number module    febonacci()
n_num = int(input('enter a digit for n-number febunacci: '))
febu_cell = module1.febonacci(n_num)
print(febu_cell)

# nth addition number n_add()
addition_cell = module1.n_add(10)
print(addition_cell)'''

#          ---------type(2)

'''import module1 as m         # alias name as you like to use

# nth-addition 
addition_cell = m.n_add(10)         # here we use m instead of module1
print(addition_cell)

# Febunacci 
febu_num = m.febonacci(10)
print(febu_num)

# addition and subtraction
print(m.add(7,2))
print(m.sub(7,2))'''

        # -------- type(3)

'''from module1 import add, febonacci, n_add

print(n_add(6))
print(febonacci(10))
print(add(10,8))            # sub is not mentioned so it will not work (when we put some function it auto imported)'''

        # --------type(4)

'''from module1 import n_add as n, febonacci as f

print(n(10))        # now n is equal to n_add in module1
print(f(10))        # now f is equal to febunacci in module1'''

        # ------type(5)
'''from module1 import *

print(add(2,7))
print(sub(2,7))
print(febonacci(12))
print(n_add(50))'''

        #------type(6)

'''from module1 import ab, cd
print(cd(8,2))      # here module1 will execute bcz it does know that module2 is coming next
from module2 import ab, cd
#  if 2 different modules have same variablr, functio or method then last mention module has most periority

print (ab)  
print (ab)
print(cd(8,2))      # here most recent module(module2) will execute'''

        # ------type(6) with classes

'''import module1
from module2 import department, university

print(department().IT())
print(module1.house().beaconites())

b = module1.house().beaconites()        # now all path save in 'b', b = beaconites()
print(b)    '''

        # ---------type(7)

'''from module2 import university, department
from module1 import university

print(university().UOS())       # most recent class obj calls '''

