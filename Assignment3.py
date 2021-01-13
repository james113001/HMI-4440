# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 15:32:57 2020

@author: james
"""
import tkinter as tk

def main():                                                                              
    output.delete("1.0", tk.END)
    number = num.get("1.0", tk.END)
    for i in range(10):
        i = str(i)
        count = 0
        text = ""
        for j in str(number):
            if i == j:
                count += 1
        if count != 0:
            if count ==1:
                text = text + f"Number {i} appears {count} time.\n"
            else:
                text = text + f"Number {i} appears {count} times.\n"
        output.insert(tk.END, text)
        

window = tk.Tk()
tk.Label(window, 
         text="Please enter a number.").pack()#grid(row=0, column=0, padx=5, pady=4)

num = tk.Text(window, width=40, height=1, wrap=tk.WORD)
num.pack()#grid(row=0, column=1)
ol = tk.Label(window, text="Instances of each number from 0-9:").pack()#grid(row=4, column=0, padx=5, sticky=tk.W)
output = tk.Text(window, width=40, height=10, wrap=tk.WORD)
output.pack()#grid(row=5, column=0, columnspan=2, padx=5, pady=(0,10))



tk.Button(window, 
          text='Quit', 
          command=window.destroy).pack( side = tk.LEFT )#grid(row=3, 
                                    # column=0, 
                                    # sticky=tk.W, 
                                    # padx=5, pady=4)
bt = tk.Button(window, 
          text='Show', command= main)
bt.pack( side = tk.RIGHT )#grid(row=3, 
                                    # column=1, 
                                    # sticky=tk.W, 
                                    # padx=5, pady=4)
         

tk.mainloop()