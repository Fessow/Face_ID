nums = [1,2,3,4,3,2,1,2]

def count_nums(lst):
    dict_nums = dict()
    for num in lst:
        dict_nums[num]=dict_nums.get(num, 0)+1
    return dict_nums


print(count_nums(nums))
