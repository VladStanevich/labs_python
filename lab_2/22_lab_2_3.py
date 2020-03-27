from memory_profiler import profile


def merge(A: list, B: list):
    C = [0]*(len(A)+len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C
    
def merge_sort(A):
    if len(A) <= 1:
        return 
    middle = len(A) // 2
    L = [A[i] for i in range(middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L,R)
    for i in range(len(A)):
        A[i] = C[i]

@profile
def main():
    f = open('lab_2/output.txt','r')
    lines = f.read().split('\n')
    f.close()
    s = open('lab_2/sort.txt','w')
    merge_sort(lines)
    for stroka in lines:
        stroka = stroka.split()
        merge_sort(stroka)
        for word in stroka: 
            s.write(word + ' ')
        s.write('\n')
    s.close()

if __name__ == "__main__":
    main()