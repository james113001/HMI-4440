# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 16:25:30 2020

@author: james
"""
import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as st 
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
import string

class Scrollable(tk.Frame):
    """
       Make a frame scrollable with scrollbar on the right.
       After adding or removing widgets to the scrollable frame, 
       call the update() method to refresh the scrollable area.
    """

    def __init__(self, frame, width=16):

        scrollbar = tk.Scrollbar(frame, width=width)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)

        self.canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.canvas.yview)

        self.canvas.bind('<Configure>', self.__fill_canvas)

        # base class initialization
        tk.Frame.__init__(self, frame)         

        # assign this obj (the inner frame) to the windows item of the canvas
        self.windows_item = self.canvas.create_window(0,0, window=self, anchor=tk.NW)


    def __fill_canvas(self, event):
        "Enlarge the windows item to the canvas width"

        canvas_width = event.width
        self.canvas.itemconfig(self.windows_item, width = canvas_width)        

    def update(self):
        "Update the canvas and the scrollregion"

        self.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox(self.windows_item))       
        
        
def stem():                                                                              
    output.delete("1.0", tk.END)
    freq.delete("1.0", tk.END)
    lancaster.delete("1.0", tk.END)
    porter.delete("1.0", tk.END)

    abstract = abst.get("1.0", tk.END)
    table = str.maketrans(dict.fromkeys(string.punctuation))
    abstract= abstract.translate(table)
    
    # Tokenize the text using word_tokenize() from NLTK
    words = nltk.word_tokenize(abstract)
    
    words = [word for word in words if not word.isnumeric()]
    words = [word.lower() for word in words]
    # for x in punc:                          #eliminate punctuation
    #     words = [y.replace(x, "") for y in words]
    roots = ", ".join(words)
    
    
    #Compute word frequency using FreqDist(). 
    fdist = nltk.FreqDist(words)
    #What are the most frequent 3 words excluding the stop words. *no stop words
    for word, frequency in fdist.most_common(3): 
        fdist = u'{};{}'.format(word, frequency)
        freq.insert(tk.END, " " + fdist)

    output.insert(tk.END, roots)
    output.configure(state ='disabled') 
    
    #Stem the words from the paragraph using the Lancaster and Porter stemmer
    pstem= PorterStemmer()
    lstem = LancasterStemmer()
    plist = []
    for w_port in words:
        plist.append(pstem.stem(w_port))
    porter.insert(tk.END, ", ".join(plist))    
    
    llist = []    
    for w_lan in words:
        llist.append(lstem.stem(w_lan))
    lancaster.insert(tk.END, ", ".join(llist))
            
    porter.configure(state ='disabled') 
    lancaster.configure(state ='disabled') 
    
    #Compare the above results with the ones produced by your stemmer developed in Assignment 4.
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
    a4.insert(tk.END, newsent)


root = tk.Tk()
body = ttk.Frame(root)
body.pack(fill=tk.BOTH, expand=True) 

scrollable_body = Scrollable(body, width=30)

tk.Label(scrollable_body, text="Please type the abstract.").pack(pady = 10, padx = 10)
abst = st.ScrolledText(scrollable_body, wrap = tk.WORD, width = 80, height = 10, padx = 5)
abst.pack(padx = 10)

tk.Label(scrollable_body, text="Roots of the words in the abstract:").pack(pady = 10, padx = 10)
output = st.ScrolledText(scrollable_body, wrap = tk.WORD, width = 80, height = 8, padx = 5)
output.pack(padx = 10)

tk.Label(scrollable_body, text="Top 3 most frequent words in the abstract:").pack(pady = 10, padx = 10)
freq = tk.Text(scrollable_body, width=60, height=1, wrap=tk.WORD, padx = 5)
freq.pack(padx = 10)

tk.Label(scrollable_body, text="Results of Lancaster stemming:").pack(pady = 10, padx = 10)
lancaster = st.ScrolledText(scrollable_body, wrap = tk.WORD, width = 80, height = 8, padx = 5)
lancaster.pack(padx = 10)

tk.Label(scrollable_body, text="Results of Porter stemming:").pack(pady = 10, padx = 10)
porter = st.ScrolledText(scrollable_body, wrap = tk.WORD, width = 80, height = 8, padx = 5)
porter.pack(padx = 10)

tk.Label(scrollable_body, text="Results of Assignment 4 stemming:").pack(pady = 10, padx = 10)
a4 = st.ScrolledText(scrollable_body, wrap = tk.WORD, width = 80, height = 8, padx = 5)
a4.pack(pady = 10, padx = 10)


footer = ttk.Frame(root)
footer.pack(pady = 10, padx = 10)

tk.Button(footer, text='Quit', command=root.destroy).pack(side=tk.LEFT, pady = 10, padx = 10)

tk.Button(footer, text='Enter', command= stem).pack(side=tk.RIGHT, pady = 10, padx = 10)

scrollable_body.update()

root.mainloop()
