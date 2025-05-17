def run():
    from myconnection import connect_to_mysql

    with open("opsql.txt") as f:
        query=f.read()

    config = {
        "host": "127.0.0.1",
        "user": "root",
        "password": "arnab11286",
        "database": "Bank",
    }

    cnx = connect_to_mysql(config, attempts=3)

    if cnx and cnx.is_connected():

        with cnx.cursor() as cursor:

            result = cursor.execute(query)

            rows = cursor.fetchall()

            for rows in rows:

                print(rows)

        cnx.close()

    else:

        print("Could not connect")