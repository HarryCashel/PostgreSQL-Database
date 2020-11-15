import psycopg2
import os

from dotenv import load_dotenv
load_dotenv()

try:
    # local
    # connection = psycopg2.connect(
    #     user='cashmoney',
    #     password='g3t0ffw0w!1',
    #     host='localhost',
    #     port='5432',
    #     database='mypythondatabase'
    # )
    # ec2
    # connection = psycopg2.connect(
    #     user='postgres',
    #     password="postgres",
    #     host='ec2-3-138-189-186.us-east-2.compute.amazonaws.com',
    #     port='5432',
    #     database='postgres'
    # )

    # database
    connection = psycopg2.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME")
    )

    print("Postgresql connection is open")

    cursor = connection.cursor()

    my_query = (
        """
        SELECT * FROM patient
        """
    )

    cursor.execute(my_query)

    print("\nThe query retrieved", cursor.rowcount, "records\n")

    print("All records are:\n")
    row = cursor.fetchall()
    print(row)

    print("\nThe records are in:\n")
    for r in row:
        print(r)

    connection.commit()

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

else:
    if connection:
        cursor.close()
        connection.close()
        print("\nPostgreSQL connection is closed")
