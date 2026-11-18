def get_stats(seq):
    counts = {}
    for i in zip(seq, seq[1:]):
        counts[i] = counts.get(i, 0) + 1
    
    return counts


def merge(seq, pair, idx):
    newseq = []
    
    i = 0
    while i < len(seq):
        if i < len(seq)-1 and seq[i] == pair[0] and seq[i+1] == pair[1]:
            newseq.append(idx)
            i += 2
        else:
            newseq.append(seq[i])
            i += 1
        
    return newseq
