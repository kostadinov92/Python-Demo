import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='dbuser',
                             password='dbpassword',
                             db='phonebook',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `city` (`name`) VALUES (%s)"
        cursor.execute(sql, ('Pernik',))  # tuple!!

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `contact`"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
