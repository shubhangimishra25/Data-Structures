# method to heapify down the heap after deletion of root node
def heapify_down_min(i):

    while ((2*i) < (len(Min)-1)):
        if (2*i)+1 == (len(Min)-1) or (Min[((2*i)+1)] <= Min[(2*i)+1+1]):
            j = (2*i)+1
        else:
            j = (2*i)+1+1
        if Min[j] < Min[i]:
            temp = Min[i]
            Min[i] = Min[j]
            Min[j] = temp
            i = j
        else:
            break

# method to heapify up the heap after insertion of node

def heapify_up_min(i):
    while i > 0:
        j = i-1 >> 1
        if Min[i] < Min[j]:
            temp = Min[i]
            Min[i] = Min[j]
            Min[j] = temp
            i = j
        else:
            break

# method for deletion of node from a heap

def extract(Min):
    item = Min[0]
    Min[0] = Min[-1]
    Min.pop()
    return item

# method for insertion of node in a heap

def insert(value):
    Min.append(value)
    heapify_up_min(len(Min)-1)