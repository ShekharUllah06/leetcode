nums = [1, 1, 2, 3, 4, 5, 4, 5, 3, -1, 2]
total=len(nums)//2
c=0
while True:
    if c==total:
        break
    c=c+1
    tem = nums[1:len(nums)]
    print(nums)
    print("---------------------")
    for i in tem:
        if i==nums[0]:
           print(nums)
           nums.remove(i)
           nums.remove(i)
           break
            
       
print(nums[0])

