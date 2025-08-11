# q2
my_list = [2,4,6,8,10]
while True:
    try:
        val1 = int(input("Enter first integer value: "))
        break
    except ValueError:
        print("ERROR!!! Please Enter Only Interger Value")
while True:
    try:
        val2 = int(input("Enter second integer value: "))
        break
    except ValueError:
        print("ERROR!!! Please Enter Only Interger Value")

print("First value: ",val1)
print("Second value: ", val2)

# Assignment ans arithmetic operation(=, += , + , - , * , /)
print()
print("==========assignment and arithmatic operation==========")
print()

first = val1
print("using '=' assignment operator: ",first)

temp = 2
temp += val2
print("using '+=' assignment operator: ", temp)

result_add = val1 + val2
print("using '+' assignment operator: ", result_add)

result_sub = val1 - val2
print("using '-' assignment operator: ",result_sub)

result_mul = val1 * val2
print("using '*' assignment operator: ", result_mul)

result_div = val1 / val2
print("using '/' assignment operator: ",result_div)


# comparison(==, != , < , >)
print()
print("==========comparison operation==========")
print()

# == operator
if val1 == val2:
    print("using '==' value1 and value2 Both are same")
else:
    print("using '==' value1 and value2 Both are different")

#!= operator
if val1 != val2:
    print("using '!=' value1 and value2 Both are different")
else:
    print("using '!=' value1 and value2 Both are same")

# > operator

if val1 > val2:
    print("using '>' value1 is big ")
elif(val1 == val2):
    print("value1 and value2 both are same ")
else: 
    print(" using '>' value2 is big ")

# < operator

if val2 < val1 :
    print("using '<'  value1 is big ")
elif val1 == val2:
    print("value1 and value2 both are same ")
else:
    print("using '<'  value2 is big ")

#logical check(and , or , not)
print()
print("==========logical operation==========")
print()

if(val1 > 0 and val2 > 0):
    print("using 'and': Both values are positive")

if(val1 == 0 or val2 == 0):
    print("using 'or': at least one value is zero.")

if not(val1 == val2):
    print("using 'not': both vaues are different")
else:
    print(" using 'not': both vaues are same")

#bitwise operations(&, | , ^)
print()
print("==========bitwise operation==========")
print()


if(val1 > 0 & val2 > 0):
    print("Using '&' bitwise AND operator: Both values are positive")

if(val1 == 0 | val2 == 0):
    print("Using '|' bitwise OR operator: at least one value is zero.")

xor_result = val1 ^ val2
print("Using '^' bitwise XOR operator: ", xor_result)

# query

# membership test(check if number are in a predefined list (in, not in))
print()
print("=========membership test(check uf number are ina predefined list (in, not in))==========")
print()

if val1 in my_list:
    print(f"using 'in': value {val1} in my list predefined")
else:
    print(f"using 'in': value {val1} is not in my list predefined")

if val1 not in my_list:
    print(f"using 'not in': value {val1} is not in my list predefined")
else:
    print(f"using 'not in': value {val1} in my list predefined")



# identity test (check if both variable reference the same object(is,is not))
print()
print("=======identity test (check if both variable reference the same object(is,is not))===")
print()

if val1 is val2:
    print("using 'is': value 1 and value 2 reference the same object memory")
else:
    print("using 'is': value 1 and value 2 DIFFERENT reference object memory")

if val1 is not val2:
    print("using 'is not':  value 1 and value 2 DIFFERENT reference object memory")
else:
    print("using 'is not':  value 1 and value 2 reference the same object memory")



