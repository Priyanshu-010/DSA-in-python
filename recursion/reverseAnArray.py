nums= [2,212,4,4,1,123,5,2,1]
def swap(nums, l, r):
    if(l > r):
        return
    nums[l], nums[r] = nums[r], nums[l]
    swap(nums,l+1,r-1)

swap(nums,0,len(nums)-1)
print(nums)