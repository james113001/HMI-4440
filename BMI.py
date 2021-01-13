# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 15:36:26 2020

@author: james
"""

#BMI Calculator with GUI

import tkinter as tk

#print entry, BMI, and rating to console

def show_entry_fields():
    global BMI, Rating
    print("Body weight (kg): %s \nHeight (m): %s \nBMI: %d \
          \nRating: %s " % (weight.get(), height.get(), BMI, Rating))
    weight.delete(0, tk.END)
    height.delete(0, tk.END)
    
   
def BMI_calc():
    global BMI, Rating
    #calculate BMI
    BMI = float(weight.get()) / (float(height.get()) ** 2)
    
    #rate BMI
    Rating = "null"
    if BMI<=20:
        Rating = "Underweight"
    elif BMI > 20 and BMI <= 25:
        Rating = "Normal weight"
    elif BMI > 25 and BMI <= 30:
        Rating = "Overweight"
    else:
        Rating = "null"
        

#GUI
window = tk.Tk()
tk.Label(window, 
         text="Weight (kg)").grid(row=0)
tk.Label(window, 
         text="Height (m)").grid(row=1)

weight = tk.Entry(window)
height = tk.Entry(window)

weight.grid(row=0, column=1)
height.grid(row=1, column=1)

tk.Button(window, 
          text='Quit', 
          command=window.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    padx=5, pady=4)
tk.Button(window, 
          text='Show', command= lambda:[BMI_calc(), show_entry_fields()]).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       padx=5, pady=4)

tk.mainloop()