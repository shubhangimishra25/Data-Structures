# Author : Shubhangi Mishra
# Worst case time complexity O(n2)
# Best case time complexity is O(n)
# Usecase is when the array is partially sorted
# It is a stable sorting algorithm  and takes part in hybrid sorting algorithm
# It is adaptive and takes less number of steps as compared 
#  to bubble sort because it breaks if number is not swapping as remaining LHS would definitely be sorted otherwise




# EXAMPLE dry run
# pass 0
# here 3 is being compared
# [5, 3, 4, 1, 2]
# [3, 5, 4, 1, 2]

# pass 1
# here 4 is being compared
# [3, 5, 4, 1, 2]
# [3, 4, 5, 1, 2]

# pass 2
# here 1 is being compared
# [3, 4, 5, 1, 2]
# [3, 4, 1, 5, 2]
# [3, 1, 4, 5, 2]
# [1, 3, 4, 5, 2]

# pass 3
# here 2 is being compared
# [1, 3, 4, 5, 2]
# [1, 3, 4, 2, 5]
# [1, 3, 2, 4, 5]
# [1, 2, 3, 4, 5]


def insertion_sort(a):

    n=len(a)

# this iteration runs from 0 to n-2 because last element will be automatically sorted
# and for j we have to use i+1 so that it does not go out of range
    for i in range(0,n-1):
        print('pass',i)
        # internal loop that takes a number and put it in correct LHS index
        for j in range(i+1,0,-1):
            print(j)
            print(a)
            # swapping logic
            if a[j]<a[j-1]:
                a[j],a[j-1]=a[j-1],a[j]

            # breaks the loop as remaining LHS is already sorted
            else:
                break
    return a

a=[5,3,4,1,2]
print(insertion_sort(a))

