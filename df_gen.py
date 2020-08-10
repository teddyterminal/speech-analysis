import pandas as pd
import os
import string
import numpy as np

def punct(string): 
  
    # punctuation marks 
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~—'''
  
    # traverse the given string and if any punctuation 
    # marks occur replace it with null 
    for x in string.lower(): 
        if x in punctuations: 
            string = string.replace(x, "") 
  
    # Print string without punctuation 
    return string.lower()

s = pd.read_csv("data.txt", "\t")
s.columns = ["word", "+/-", "score"]


q1 = list(s["word"])
q2 = list(s["score"])
d = {}
for i in range(len(q1)): 
    d[q1[i]] = q2[i]


spd = {}
for file in os.listdir("./docs"): 
    try: 
        f = open("./docs/" + file, "r")
        sr = f.read()
    except Exception as e: 
        print(e)
        continue
    
    sr = punct(sr.replace('\n',' '))
    sr = punct(sr.replace('  ',' '))
    sr = sr.split(" ")
    #print(file)
    
    for k in [5, 4, 3, 2]: 
        for i in range(len(sr)-k): 
            pot_word = sr[i]
            for q in range(1, k):
                pot_word = pot_word + "_" + sr[i+q]

            if pot_word in d and k > 2: 
                #print(pot_word, d[pot_word])

                sr[i] = pot_word

                for q in range(1, k):
                    sr[i+q] = ""   
    
    c = []
    cc = []
    score = 0
    count = 0
    for word in sr: 
        #if word in ["laughter", "applause", "cheers"]: 
        #    print(file)
        if word in d and word not in ["laughter", "applause", "cheers"]: 
            score += d[word]
        count += 1
        c.append(score)
        cc.append((score/len(sr) - 0.0505*count/len(sr))*len(sr))
    
    a = c[-1]/len(sr)

    ccc = []
    score = 0
    count = 0
    for word in sr: 
        if word in d and word not in ["laughter", "applause", "cheers"]: 
            score += d[word]
        count += 1
        #print(a, score, count, len(sr))
        ccc.append((score/len(sr) - a*count/len(sr))*1000)   

    spd[file] = (len(sr), c, cc, ccc, a*100, np.std(ccc))

df = pd.DataFrame(spd).T
df.columns = ["length", "sent1", "sent_norm", "sent_var", "final_sent", "var_sent"]

df.to_csv("sentiments.csv")

