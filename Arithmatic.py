def add (num1,num2):
    ans = num1 + num2
    return ans


def sub (num1,num2):
    ans = num1 - num2
    return ans

def mul (num1,num2):
    ans = num1 * num2
    return ans

a = 10
b = 20
ans = add(a,b)
ans = sub(a,b)
ans = mul(a,b)

print(f"Addition of {a} and {b} is {ans}")
print(f"substraction of {a} and {b} is {ans}")
print(f"multiplication of {a} and {b} is {ans}")