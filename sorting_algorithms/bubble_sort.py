# Author : Shubhangi Mishra
#  best case time complexity O(n)
#  worst case time complexity O(n2)

# 0(indicates value of ith iteration)
# [1, 3, 5, 4, 2] 1 3 (elements that are compared and swapped  here 1 and 3 
#                       is compared and if 1 is not smaller than 3 then not
#                        swapped else it is swapped)
# [1, 3, 5, 4, 2] 3 5
# [1, 3, 4, 5, 2] 4 5
# [1, 3, 4, 2, 5] 2 5
# 1
# [1, 3, 4, 2, 5] 1 3
# [1, 3, 4, 2, 5] 3 4
# [1, 3, 2, 4, 5] 2 4
# 2
# [1, 3, 2, 4, 5] 1 3
# [1, 2, 3, 4, 5] 2 3
# 3
# [1, 2, 3, 4, 5] 1 2










def bubble_sort(a):
    n=len(a)

    #  for every iteration maximum element will come at the last place
    for i in range(0,n):

        # variable taken to stop sorting if array has already become sorted
        swapped=False

        for j in range(1 , n-i):

            if a[j-1]>a[j]:
                # swapping if the initila place element is largere than the coming element
                a[j-1],a[j]=a[j],a[j-1]
                swapped=True

        # loop will break as the array is already overall sorted
        if not swapped:
            break
    return a

a=[3,1,5,4,2]

print(bubble_sort(a))
