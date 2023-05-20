import mysql.connector

mydb = mysql.connector.connect(
    host='localhost', 
    user='amir', 
    passwd='khoury25.7',
    database='vocabularydb'
)

mycursor = mydb.cursor()
#text = "SUI"
#definition = "SUI"
#arOutput = "SUI"

#sqlformula = "INSERT INTO vocabulary (word, definition, arabicDefinition) VALUES (%s, %s, %s)"
#word1 = (text, definition, arOutput)

mycursor.execute("DELETE FROM ImageAndWord")
#mycursor.execute("ALTER TABLE ImageAndWord MODIFY COLUMN File LONGBLOB")
mydb.commit()


