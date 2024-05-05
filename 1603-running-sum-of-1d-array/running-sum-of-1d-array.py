class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        run_list = []

        current_sum = 0 

        for num in nums:
            current_sum += num
            run_list.append(current_sum)
        return run_list