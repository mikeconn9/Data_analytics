a = (lambda x: x*(x+1))(6)
print(a)

nums = [1, 2, 8, 3, 7]
res = list(filter(lambda x: x%2==0, nums))
print(res)

# Fibonacci problem:
# Approach:
# Write psedo code 
# 1. Test 0, 1, 2, 3: Fi_func(0, 1, 2, 3) -> Figureed Core function: Fi_func(x-1) + Fi_func(x-2)
# 2. Figure out the Base Case: Should be two x == 0 and x == 1
# 3. Figure out the range, output
input_num = int(input())
Fi_list = []
def Fi_func(x):
    if x == 1:
        return 1
    else:
        if x == 0:
            return 0
        else:
            return Fi_func(x-1) + Fi_func(x-2)
    
for i in range(input_num):
    Fi_list.append(Fi_func(i))

print(Fi_list)