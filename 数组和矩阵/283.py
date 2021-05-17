lens = len(nums)
        for i in range(lens):
            for j in range(0,lens-i-1):
                if nums[j] == 0:
                    nums[j] , nums[j+1] = nums[j+1] , nums[j]
