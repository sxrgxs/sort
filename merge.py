def merge_sort(seq : list) -> None:
    if len(seq) < 2:
        return

    mid = len(seq) // 2
    a = seq[:mid]
    b = seq[mid:]

    merge_sort(a)
    merge_sort(b)

    merge(a, b, seq)

def merge(a : list, b : list, seq : list) -> None:
    i = j = 0
    while i + j < len(seq):
        if j == len(b) or (i < len(a) and a[i] < b[j]):
            seq[i + j] = a[i]
            i+=1
        else:
            seq[i + j] = b[j]
            j+=1
