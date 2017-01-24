import pyodbc
conn = pyodbc.connect('DRIVER={HDBODBC};SERVERNODE=107.22.7.180:30115;SERVERDB=DB1;UID=SYSTEM;PWD=Welcome1') #Open connection to SAP HANA  
cur = conn.cursor() #Open a cursor  
file = open('c:/my.html', 'rb') #Open file in read-only and binary   
content = file.read() #Save the content of the file in a variable  
cur.execute("INSERT INTO TA.MYTABLE_BLOB VALUES(?,?,?)", ('3',content,'text/html')) #Save the content to the table  
cur.execute("COMMIT") #Save the content to the table  
file.close() #Close the file  
cur.close() #Close the cursor  
conn.close() #Close the connection  
