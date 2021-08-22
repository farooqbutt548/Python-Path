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

# --simple while_loops
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
