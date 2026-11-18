import os, json, random
from .tokenizer_v2 import *


folder = "DATA/SYMBA - Test Data/SYMBA - Test Data"
files = os.listdir(folder)

pats = ["i", "_u", "m_[a-z]+", r"s_\d+", "reg_prop", r"g\^\d+", r"\^", r"\s*\+\s*", "-", "/", r"\*", r"\(-\d+\)", r"\(\d+\)", r"\(", r"\)", r"\d+"]
reg_pat = "|".join(pats)







# -----------------(building vocab from train split)
with open("tokenizer/data/splits.txt", "r") as f:
    data = json.load(f)["val"]


for t in data:
    vocab  = encode(t[-1])

# print(vocab)






# -----------------(dedup and split!)

# data = []

# for file in files:
#     txt = []
    
#     with open(folder+ "/" + file, "r", encoding ="utf-8") as f:
#         txt = f.read()
    
#     lines = txt.strip("\n").split("\n")
#     print(f"going through lines, total lines in this file: {len(lines)}")
#     for l in lines:
#         elems = l.rstrip("\n").split(" : ")
#         sqamp = elems[-1]
#         amp = elems[-2]
#         data.append((amp, sqamp))


# for i in range(len(data) - 1):
#     if data[i] == data[i+1]:
#         print(f"duplicate found: {data[i]} instances found: {data.count(data[i])}")
        
# data = list(set(data))
# print(data[-1][-1], data[-1][-2], len(data) )

# with open("tokenizer/data/amps_sqamps.txt", "w") as f:
#     json.dump(data, f)


# with open("tokenizer/data/amps_sqamps.txt", "r") as f:
#     data = json.load(f)

# #shuffling it!
# rng = random.Random(45)
# rng.shuffle(data) #inplace shuffle

# #making splits
# idx1 = int(len(data) * 0.8)
# idx2 = idx1 + int(len(data) * 0.1)

# print(idx1, idx2)

# train = data[:idx1]
# val = data[idx1:idx2]
# test = data[idx2:]

# with open("tokenizer/data/splits.txt", "r") as f: #loading the data from the file itself
#     obj =  json.load(f)

# train, val, test = obj["train"], obj["val"], obj["test"]
# print("\n\n")
# print(len(train), len(val), len(test))
# print(type(train), type(val), type(test))

# train_set, val_set, test_set = {tuple(x) for x in train}, {tuple(x) for x in val}, {tuple(x) for x in test}

# assert not (train_set & val_set)
# assert not (train_set & test_set)
# assert not (val_set & test_set)



#------------------------- (build vocab)


# def fvocab():
#     for file in files:
#         txt = ""
#         with open(folder + "/" + file, "r") as f:
#             txt = f.read()
            
#         lines = txt.strip("\n").split("\n")
#         for l in lines:
#             sqamp = l.split(" : ")[-1]
#             build_vocab(sqamp)

#     return vocab

# vocab = fvocab()
# print(vocab)

# with open("tokenizer/data/vocab.txt", "w") as f:
#     f.write(f"{vocab}")





# #-------------------------------------------
# # pats = ["i", "_u", "m_[a-z]+", r"s_\d+", "reg_prop", r"g\^\d+", r"\^2",  r"\^4", r"\^", r"\+", "-", "/", r"\*", r"\(-\d+\)", r"\(\d+\)", r"\d*"]

# # pats = 


# # s = """-1/144*g^4*((-16)*m_d^2*m_u^2 + (-8)*m_d^2*s_12 + (-8)*s_14*s_23 + (-8)*s_13*s_24 + (-8)*m_u^2*s_34)*(m_u^2 + s_12 + 1/2*reg_prop)^(-2) + 1/16*i*g^2*(i*g^2*((-16)*m_d^2*m_u^2 + (-8)*m_d^2*s_12 + (-8)*s_14*s_23 + (-8)*s_13*s_24 + (-8)*m_u^2*s_34)/(m_u^2 + s_12 + 1/2*reg_prop) + 32/9*i*g^2*(m_d^2*m_u^2 + 1/2*m_d^2*s_12 + 1/2*s_14*s_23 + 1/2*s_13*s_24 + 1/2*m_u^2*s_34)/(m_u^2 + s_12 + 1/2*reg_prop))/(m_u^2 + s_12 + 1/2*reg_prop)"""


# # PAT = r""""""






# #------------------------------------
# # txt = ""

# # with open(folder + "/" + file, "r", encoding="utf-8") as f:
# #     txt = f.read()

# # lines = txt.strip("\n").split("\n")

# # sqamp = []
# # for l in lines:
# #     elems = l.split(" : ")
# #     sqamp.append(elems[-1])


# # print(sqamp)



# #-------------------------------------
# # for file in files:
# #     txt = []
    
# #     with open(folder+ "/" + file, "r", encoding ="utf-8") as f:
# #         txt = f.read()
    
# #     lines = txt.strip("\n").split("\n")
# #     data = {file: len(lines)}

# #     for l in lines:
# #         elems = l.rstrip("\n").split(" : ")
# #         if len(elems) != 4:
# #            data |= { "No 4 fields": lines.index(l) } 


# #     info.append(data)
    
# # # print(info)
# # for i in info:
# #     if len(i) > 1:
# #         print(i)



# #----------
# # file = "QCD-2-to-2-diag-TreeLevel-0.txt"
# # with open(folder+ "/" + file, "r", encoding ="utf-8") as f:
# #     txt = f.read()
    
# # lines = txt.strip("\n").split("\n")
# # a = []

# # for l in lines:
# #     line = l.strip("\n").split(" : ")
# #     a.append(len(line))
    
# # print(min(a))

# import json

# with open("tokenizer/data/vocab.txt", "w") as f:
#     obj ={'<BOS>': 1, '<EOS>': 2, '<PAD>': 0, '<UNK>': 3, 'g': 4, 'i': 5, 'reg_prop': 6, '\\+': 7, '-': 8, '\\*': 9, '/': 10, '^': 11, '\\(': 12, '\\)': 13, '1': 15, '144': 16, '*': 17, 'g^4': 18, '(': 19, '(-16)': 20, 'm_d': 21, '2': 22, 'm_u': 23, ' + ': 24, '(-8)': 25, 's_12': 26, 's_14': 27, 's_23': 28, 's_13': 29, 's_24': 30, 's_34': 31, ')': 32, '(-2)': 33, '16': 34, 'g^2': 35, '32': 36, '9': 37, 'm_s': 38, 'm_t': 39, 'm_c': 40, 'm_b': 41, '27': 42, '1728': 43, '128': 44, '64': 45, '960': 46, '864': 47, '(-128)': 48, '(-4)': 49, '(-2048)': 50, '1024': 51, '512': 52, '480': 53, '(-1024)': 54, '(-64)': 55, '8': 56, '2304': 57, '(-224)': 58, '576': 59, '4': 60, '7': 61, '18': 62, '448': 63, '112': 64, '224': 65, '17': 66, '896': 67, '288': 68, '3': 69, '256': 70, '6': 71, '12': 72, '96': 73, '48': 74, '192': 75, '5': 76, '24': 77, '640': 78}
#     json.dump(obj, f)