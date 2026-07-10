class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        #create a loop to cycle through the positiosn
        for i in range(len(nums)):
            product = 1
        

            for j in range(len(nums)):
                #check wether j is differnet drom i
                if j != i:
                    product *= nums[j]
        
            output.append(product)

        return output