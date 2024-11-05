import psycopg2

# Connect to chinook database
# connection = psycopg2.connect(database="chinook")
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database
# cursor = connection.cursor()
cursor = connection.cursor()

# Query 1 - select all artists from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')
cursor.execute('SELECT * FROM "Artist"')

# Fetch the results (multiple)
# results = cursor.fetchall()
results = cursor.fetchall()

# Fetch the results (single)
# results = cursor.fetchone()

# Close the connection
# connection.close()
connection.close()

# Print the results
# for result in results:
#     print(result)
for result in results:
    print(result)    