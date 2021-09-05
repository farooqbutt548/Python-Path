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

tup1 = (1,2,3,4,5,6.0)
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
