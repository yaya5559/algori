def maxProduct(nums):
    
    maxEndingHere = nums[0]
    minEndingHere = nums[0]

    globalMax = maxEndingHere

    for i in range(1, len(nums)):
        prevMax = maxEndingHere
        prevMin = minEndingHere

        newMax = max(nums[i], max(prevMin * nums[i], prevMax * nums[i]))
        newMin = min(nums[i], min(prevMin * nums[i], prevMax * nums[i]))

        maxEndingHere = newMax
        minEndingHere = newMin

        globalMax = max(globalMax, maxEndingHere)

    return globalMax