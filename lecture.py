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

                                #Numbers 
#integer Numbers
int_nums =50
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
print(type(new_float))  #  float

