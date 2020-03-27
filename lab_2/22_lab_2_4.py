def flatten(l, a=[]):
    for elem in l:
        if isinstance(elem, list):
            flatten(elem, a)
        else:
            a.append(elem)
    return a

    
l = [[1,[2]], [3, 3], [[3,[[[[[[[[[44,[[[[[[[[[[[[[[[[[333,[[[[[[[[[[[[[[[[[[[[[[[[[55]]]]]]]]]]]]]]]]]]]]]]]]]]]]]],76835]]]]]]]]]]]]]]]]]]]],[6,5,2]]]], [[[6]]]]
print(flatten(l))
