def twoSum(num,target):
    num_map={} 
    for index, num in enumerate(num):
        complement = target - num
        if complement in num_map:
            return[num_map[complement],index]
        num_map[num] = index
    return[]

num =list(map(int, input("enter the array of numbers (separated by spaces:) ").split()))
target=int(input("enter the target valu]e:"))
#target=9
result =twoSum(num,target)
print(result)