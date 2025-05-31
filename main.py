num = input("What number do you want to power?")
if("." in num):
    num = float(num)
else:
    num = int(num)

n = int(input("What is the power?"))

print(f"The result is: {num**n}")