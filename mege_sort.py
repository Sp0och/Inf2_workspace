
import numpy as np

# def merge(list1, list2):
#     merged_list = []
#     for i in range(len(list1) + len(list2)):
#         if(len(list1) > 0 and len(list2) > 0):
#             if(list1[0] < list2[0]):
#                 merged_list.append(list1.pop(0))
#             else:
#                  merged_list.append(list2.pop(0))
#         elif(len(list1) > 0):
#             merged_list.append(list1.pop(0))
#         else:
#             merged_list.append(list2.pop(0))
#     return merged_list
            
# def mergesort(List):
#     if(len(List) <= 1):
#         return List
#     else:
#         left_index = int(len(List)/2)
#         right_index = left_index + 1
#         list_left = mergesort(List[0:left_index+1])
#         list_right = mergesort(List[right_index,-1])
#         return merge(list_left,list_right)
Liste = [1,2,3,4,5]
try:
    print(Liste[6])
except ZeroDivisionError:
    print('''Don'tdevidebyzero''')
except IndexError:
    print("Index not in list")          