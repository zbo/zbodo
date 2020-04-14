# class Solution2(object):
#     def numSubarrayProductLessThanK(self, nums, k):
#         if len(nums) == 1:
#             if nums[0] < k:
#                 return 1
#             else:
#                 return 0

#         tmp = 1
#         i = 0
#         while i < len(nums):
#             tmp = tmp * nums[i]
#             if tmp >= k:
#                 break
#             i = i + 1
#         print i, nums[1:]
#         return i + self.numSubarrayProductLessThanK(nums[1:], k)

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        sum = 0
        while len(nums)!=0:
            if len(nums) == 1:
                if nums[0] < k:
                    return sum+1
                else:
                    return sum
            tmp = 1
            i = 0
            while i < len(nums):
                tmp = tmp * nums[i]
                if tmp >= k:
                    break
                i = i + 1
            nums = nums[1:]
            sum = sum + i
        return sum

if __name__=="__main__":
    s = Solution()
    print(s.numSubarrayProductLessThanK([10,5,2,6],100))