def swap(a, i, j):
    temp = a[i]
    a[i]=a[j]
    a[j] = temp

def mergeSort(a, left, right):
    if left>= right:
        return

    if(right == (left+1)):
        if(a[left]> a[right]):
            swap(a, left, right)
        return
    else:
        middle = (left +right)//2
        mergeSort(a, left, middle)
        mergeSort(a, middle+1, right)
        merge(a, left, middle, right)

def merge(a, left, middle, right):
    i = left
    j = middle+1

    tmp_stored = []

    while( i<=middle and j<=right ):
        if(a[i]  <a[j]):
            tmp_stored.append(a[i])
            i+=1

        else:
            tmp_stored.append(a[j])
            j+=1

    if i<=middle:
        tmp_stored+=a[i:middle+1]

    if j<=right:
        tmp_stored+=a[j:right+1]

    a[left:right+1] = tmp_stored






A= [5,12,6,3,1, 55, 8, 56, 23, 8, 17, 16]
mergeSort(A, 0,len(A)-1)
print(A)