# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:18:51 2020

@author: james
"""

import mysql.connector

try:
    cnx = mysql.connector.connect(user='root', password='root123',
                              host='localhost',
                              database='assignment9',
                              use_pure=True)

except mysql.connector.Error as err:        
    print(err.msg)
else:
    print('connected...')
    cursor= cnx.cursor()
    city=input('search for a city: ')      
    
    query = "SELECT CompanyName FROM customers WHERE City LIKE '%"+city+"%' UNION SELECT CompanyName AS 'Supplier' FROM suppliers WHERE City LIKE '%"+city+"%'"
    
    
    try:   
        cursor.execute(query)
        
    except mysql.connector.Error as err:        
        print(err.msg)
    else:
        for (CompanyName) in cursor:
            print(CompanyName)

cursor.close()
cnx.close()