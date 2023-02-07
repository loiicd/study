import psycopg2

try:
  con = psycopg2.connect(user = 'loicdoerr',
                          password = 'password',
                          host = 'localhost',
                          port = '5432',
                          database = 'room')
  cursor = con.cursor()
  query = 'select * from user'

  cursor.execute(query)
  records = cursor.fetchall()

  print(records)

  # print("Print each row and it's columns values")
  # for row in records:
  #   print()
  #   print(f"Id = {row[0]}")
  #   print(f"Firstname = {row[1]}")
  #   print(f"Lastname = {row[2]}")

except (Exception, psycopg2.Error) as error:
  print("Error while fetching data from PorstgreSQL", error)