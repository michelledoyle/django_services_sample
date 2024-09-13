from google.cloud.spanner_dbapi import connect

connection = connect('the-poc1', 'rthe-poc1')
cursor = connection.cursor()

cursor.execute(
    "SELECT *"
    "FROM Encounter"
)

results = cursor.fetchall()

# Print each row in the results
for row in results:
    print(row)
