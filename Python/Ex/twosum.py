nums = [3,2,4]
target = 6
index = []
new_target = 0



for i in range(len(nums)):
    for j in range(len(nums)):
        new_target = nums[i]+nums[j]
        if new_target == target and i != j and not index.__contains__(i):
            index.append(i)
            index.append(j)
            print(index)
            





    


