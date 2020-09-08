def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """

    for i in range(0, len(lst)):
        try:
         if i == (len(lst)-1):
              print(lst[i])
        except:
            print('None')


print(last_element([1,2,3]))
print(last_element([]))