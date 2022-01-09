# dict={}
# def count_common(list1,list2):
#     for num in list1:
#         dict[num]=True
#     for num in list2:
#         if num in dict:
#             print(num)
#         else:
#             print('nothing common')
# list1=[1,3,3,5]
# list2=[3,8,9]
# count_common(list1,list2)
# print(dict)

# listans=[]
# def count_zero(list):
#     for i,num in enumerate(list):
#         sum=num
#         listans=num
#         for j in range(i+1,len(list)):
#             sum=sum+list[j]
#             listans=list[j]
#             if sum==0:
#                 print(listans)
#             j+=1
#             listans.clear()
#         listans.clear()
# count_zero([3, 4, -7, 3, 1, 3, 1, -4, -2, -2])


# def binary_search(a, key,left,right):
#   #TODO: Write - Your - Code
#   mid=left+right//2
#   if left>right:
#     return -1
#   if a[key]==mid:
#     return mid
#   if a[key]<mid:
#     binary_search(a,key,left,mid-1)
#   if a[key]>mid:
#     binary_search(a,key,mid+1,right) 


# a=[1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162, 176, 188, 199, 200, 210, 222]
# key=10
# print(binary_search(a,key,0,len(a)))


# Definition for singly-linked list.
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

# class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     print(head)
class LinkedList:
    def __init__(self):
        self.head=None
    def print_list(self):
        curreNode=self.head
        while curreNode:
            print( curreNode.data,'->',)
            curreNode=curreNode.next 
    def insert_list(self,data):
        new_node=ListNode(data)
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
    


linklist=LinkedList()
linklist.insert_list('1')
linklist.insert_list('2')
linklist.print_list()
