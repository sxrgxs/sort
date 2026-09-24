def selection_sort(seq : list) -> None:
    for i in range(len(seq) - 1):
        num = i
        for j in range(i + 1, len(seq)):
            if seq[j] < num:
                num = j
        seq[i], seq[num] = seq[num], seq[i]
