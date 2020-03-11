def flatten(l,a=[]):
    for elem in l:
        if type(elem) == list:
            flatten(elem,a)
        else:
            a.append(elem)
    return a

    
l =  [1,2,[3,4,5],[6,[7,8]]]
print(flatten(l,[]))