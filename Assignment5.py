"""
Created on Tue Sep 22 22:40:24 2020

@author: james
"""
import tkinter as tk

def main():
    output.delete("1.0", tk.END)
    select = selection.get("1.0")
    car = numandkey[select]
    color = Carscolors[car]
    text = f"The {car}'s color is {color}. Congratulations!"                                                                         
    output.insert(tk.END, text)

numandkey = {"1": "Tesla Model 3", "2": "Bentley Continental GT", "3":"Volkswagon Beetle"}    
Carscolors = {"Tesla Model 3": "Black", "Bentley Continental GT": "White", "Volkswagon Beetle": "Red"}

window = tk.Tk()

tk.Label(window, 
         text=numandkey).pack()
tk.Label(window, 
         text="You won a car! Which color is it?\n\
         Find out by selecting a car model by typing 1, 2, or 3.").pack()

selection = tk.Text(window, width=5, height=1, wrap=tk.WORD)
selection.pack()


olabel = tk.Label(window, text="Color of the car:").pack()
output = tk.Text(window, width=40, height=2, wrap=tk.WORD)
output.pack()



tk.Button(window, 
          text='Quit', 
          command=window.destroy).pack( side = tk.LEFT )

bt = tk.Button(window, 
          text='Enter', command= main)
bt.pack( side = tk.RIGHT )
         

tk.mainloop()