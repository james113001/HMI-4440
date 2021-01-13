import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='root', password='root123',
                              host='localhost',
                              database='assignment11',
                              use_pure=True)

except mysql.connector.Error as err:      
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:        
        print("Something is wrong with your user name or password")      
    elif err.errno == errorcode.ER_BAD_DB_ERROR:        
        print("Database does not exist")      
    else:        
        print(err.msg)
else:
    print('connected...')
cursor= cnx.cursor()
search=input('search for a ICD Code by description: ')
query = "SELECT Code,Description FROM icd10codes WHERE Description like '%"+search+"%' LIMIT 10"
try:   
    cursor.execute(query)
except mysql.connector.Error as err:        
    print(err.msg)
else:
    print("Top 10 results by Code order")
    for (Code, Description) in cursor:
        print("Code: " + Code+ "    Description: "+ Description)
cursor.close()
cnx.close()