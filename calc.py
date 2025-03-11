a = float(input("Enter first value: "))
b = float(input("Enter second value: "))
sign = input("Enter sign: ")

def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b

if sign == "+":
	result = add(a,b)
	print(f"{a} + {b} = {result}")
elif sign == "-":
	result = sub(a,b)
	print(f"{a} - {b} = {result}")
elif sign == "*":
	result = mul(a,b)
	print(f"{a} * {b} = {result}")
elif sign == "/":
	result = div(a,b)
	print(f"{a} / {b} = {result}")
else:
	print("invalid sign!")
