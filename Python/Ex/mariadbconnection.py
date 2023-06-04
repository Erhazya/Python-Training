import pymysql

# Connect to the database
connection = pymysql.connect(
    host='192.168.0.240',
    user='admin',
    password='Sublimo86236$@',
    db='ToDoList'
)

# Create a cursor object
cursor = connection.cursor()

# Execute a SQL query
query = "SELECT * FROM Users"
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()