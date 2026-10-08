from course.andres.designpattern.singleton.database_connection_singleton import DatabaseConnectionSingleton

for i in range(10):
    con = DatabaseConnectionSingleton()
    print(con)

conn1 = DatabaseConnectionSingleton()
# conn1.connect()

conn2 = DatabaseConnectionSingleton()
# conn2.connect()

print(f"¿Son el mismo objeto? {conn1 is conn2}")

# conn1.disconnect()
# conn2.disconnect()