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
	print(add(a,b))
elif sign == "-":
	print(sub(a,b))
elif sign == "*":
	print(mul(a,b))
elif sign == "/":
	print(div(a,b))
else:
	print("invalid sign!")
