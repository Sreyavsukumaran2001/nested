lst=[
    [10,11],
    [13,45],
    [50,15],
    [60,16],
    [70,60]
]
fltn_list=[num for slist in lst for num in slist]

maped_list=[num+1 if num>25 else num-1 for num in fltn_list]
print(maped_list)

# print(fltn_list)
#
# num_gt_sixt=[num for num in fltn_list if num>16]
# print(num_gt_sixt)
#
#
#
# odd_num=[ num for num in fltn_list if num%2!=0]
# print(odd_num)
#
# even_sum = sum([ num for num in fltn_list if num%2==0])
# print(even_sum)


# for sub_list in lst:
#     for num in sub_list:
#         if num>16:
#             print(num)

# print(max(lst)[1])
#
# print(lst)
# flatten_list=[]
# for sub_list in lst:
#     for num in sub_list:
#         flatten_list.append(num)
# print(max(flatten_list))