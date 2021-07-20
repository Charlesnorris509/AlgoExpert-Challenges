#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#This the implementation of an AlgoXpert Challenge
# Linked List - Shift Link list

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    tail = head
    length = 1
    while tail.next:
        tail = tail.next
        length += 1

    offset = abs(k) % length
    if offset == 0:
        return head

    newtailPos = length - offset if k > 0 else offset
    newTail = head
    
    for i in range(1, newtailPos):
        newTail = newTail.next

    newHead = newTail.next
    newTail.next = None
    tail.next = head

    return newHead

