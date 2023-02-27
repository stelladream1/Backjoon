cursum, maxsum = 0, nums[0]
for i in range(len(nums)):
    cursum = max(cursum + nums[i], nums[i])
    maxsum = max(cursum, maxsum)
