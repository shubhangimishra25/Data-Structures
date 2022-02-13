# Author : Shubhangi Mishra
# Best case time complexity O(n2)
# Worst case time complexity O(n2)

# This is feasible to use in the small lists

# EXAMPLE dry run
# [4, 5, 1, 2, 3]
# [4, 3, 1, 2, 5] after swapping  5 3 where 5  is the maximum  and is being placed at the last position
# [4, 3, 1, 2, 5]
# [2, 3, 1, 4, 5] after swapping  4 2 where 4  is the maximum  and is being placed at the last position
# [2, 3, 1, 4, 5]
# [2, 1, 3, 4, 5] after swapping  3 1 where 3  is the maximum  and is being placed at the last position
# [2, 1, 3, 4, 5]
# [1, 2, 3, 4, 5] after swapping  2 1 where 2  is the maximum  and is being placed at the last position
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5] after swapping  1 1 where 1  is the maximum  and is being placed at the last position
# [1, 2, 3, 4, 5]


def selection_sort(a):

    n=len(a)

    # this will iterate thoughout the array sorting the element in the last
    for i in range(0,n):

        # finding the max in the given range of array
        max=0
        print(a)

        for j in range(0,n-i):

            if a[max]<a[j]:
                max=j

        #  swapping the largest element with the correct position that is the last element
        a[n-i-1],a[max]=a[max],a[n-i-1]

        print(a,'after swapping ',a[n-i-1],a[max],'where',a[n-i-1],' is the maximum  and is being placed at the last position')
    return a

# calling the selection sort 
a=[4,5,1,2,3]
print(selection_sort(a))