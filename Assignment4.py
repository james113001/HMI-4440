# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:40:24 2020

@author: james
"""
import tkinter as tk

def main():                                                                              
    output.delete("1.0", tk.END)
    sentence = sent.get("1.0", tk.END)
    words = [y.strip() for y in sentence.split()]
    punc = [",", ".", ":", ";", "!", "?", "'"]
    for x in punc:                          #eliminate punctuation
        words = [y.replace(x, "") for y in words]
    vowels = ["a", "e", "i", "o", "u"]
    for i in words:
        j= words.index(i)
        words[j] = i.lower()
        if i.endswith("ing"):
            if i[-4] == i[-5]:  #double consonant
                if i[-4] not in vowels: #^
                    words[j]= i[:-4]   
                    print(words[j]) 
                elif i[-4] in vowels:    #double vowel 
                    words[j] = i[:-3]
            elif i[-5] in vowels: #verbs ending with e
                words[j]= i.replace("ing", 'e')
            elif i[-4] == 'y':
                words[j] = i.replace("ying", 'ie')   #-ie to -ying
            elif i[-4] not in vowels and i[-5] not in vowels and i[-6] not in vowels:
                words[j] = i
            else:
                words[j] = i[:-3]
        elif i.endswith("s"):
            if i.endswith("es"):
                special = ["s", "ss", "sh", "ch", "x", "z"]
                if i[-3] in special or i[-4:-2] in special:
                    words[j] = i.replace("es", '')
                elif i[-3] == "i":
                    words [j] = i.replace("ies", 'y')
            elif i == "was" or i == "is":
                words[j] = "is"
            elif i[-2] == "s":
                words[j] = i
            
            else:
                words[j] = i[:-1] 
    newsent = ", ".join(words)
    output.insert(tk.END, newsent)

window = tk.Tk()
tk.Label(window, 
         text="Please type a sentence.").pack()

sent = tk.Text(window, width=40, height=2, wrap=tk.WORD)
sent.pack()


ol = tk.Label(window, text="Roots of the words in the sentence:").pack()
output = tk.Text(window, width=40, height=10, wrap=tk.WORD)
output.pack()



tk.Button(window, 
          text='Quit', 
          command=window.destroy).pack( side = tk.LEFT )

bt = tk.Button(window, 
          text='Enter', command= main)
bt.pack( side = tk.RIGHT )
         

tk.mainloop()