import re, json
from typing import Final



pats = ["i", "_u", "m_[a-z]+", r"s_\d+", "reg_prop", r"g\^\d+", r"\^", r"\s*\+\s*", "-", "/", r"\*", r"\(-\d+\)", r"\(\d+\)", r"\(", r"\)", r"\d+", "."]

reg_pat = "|".join(pats)

closed_vocab = {
    "<BOS>": 1,
    "<EOS>": 2,
    "<PAD>" : 0,
    "<UNK>": 3,
    "g": 4,
    "i": 5,
    "reg_prop": 6,
    r"\+": 7,
    "-": 8,
    r"\*": 9,
    "/": 10  ,
    "^": 11,
    r"\(":12,
    r"\)":13
}

open_vocab = {}

vocab = closed_vocab | open_vocab


def build_vocab(seq, file):
    global vocab

    tokens = re.findall(reg_pat, seq)
    for t in tokens:
        if t in vocab:
            pass
        else:
            open_vocab[t] = len(vocab) + 1  # okay leaving len(vocab) as int token
            vocab |= open_vocab

    with open(file, "w") as f:
        json.dump(vocab, f)

    return vocab



#the tragedy i feel about this is that i  hvae to use regex in this too
def encode(seq, fname=None):
    tok_seq = seq #not sure if that's a nicce name
    vocab  = {} 
    
    with open("tokenizer/data/vocab.txt", "r") as f:
        vocab = json.load(f)
    # print(vocab, type(vocab))
    tokens = []
    while True:
        for p in pats:
            match = re.match(p, tok_seq)
            # print(f"match obj: {match}")
            
            if match:
                try:
                    tokens.append(vocab.get(match.group(), vocab["<UNK>"]))
                    tok_seq = tok_seq.replace(match.group(), "", 1)
                    # print(f"tokens made {tokens} remaining tok_seq: {tok_seq}")
                    break
                except Exception as e:
                    raise Exception(f"remaining state of tok_seq: {tok_seq} causing the error: {e} it belongs to file: {fname}")
        
        if len(tok_seq) == 0:
            break
        
    return tokens
        
def decode(seq):
    out = ""
    
    with open("tokenizer/data/vocab.txt", "r") as f:
        vocab = json.load(f)
    
    inv_vocab = {v:k for k,v in vocab.items()}
    
    for t in seq:
        out += inv_vocab[t]
    
    return out