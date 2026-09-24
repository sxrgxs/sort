def insertion_sort(seq : list) -> None:
    for i in range(1, len(seq)):
        k = i
        while seq[k] < seq[k - 1] and k > 0:
            seq[k], seq[k-1] = seq[k-1], seq[k]
            k-=1
