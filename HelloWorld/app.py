import os
def avg_len_words(test):
    #avg = 0
    avg = len(x.replace(" ","")) / 4.0
    return avg
  
x = "the quick brown fox"
avg_x = avg_len_words(x)
print(x)
print('see me', avg_x)
assert(avg_x == 4.0)