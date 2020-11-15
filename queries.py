import psycopg2
import os

from dotenv import load_dotenv
load_dotenv()

try:
    # local
    # connection = psycopg2.connect(
    #     user=os.getenv("LOCAL_DB_USER"),
    #     password=os.getenv("LOCAL_DB_PASSWORD"),
    #     host=os.getenv("LOCAL_DB_HOST"),
    #     port=os.getenv('LOCAL_DB_PORT'),
    #     database=os.getenv('LOCAL_DB_NAME')
    # )

    # ec2
    # connection = psycopg2.connect(
    #     user=os.getenv("EC2_DB_USER"),
    #     password=os.getenv("EC2_DB_PASSWORD"),
    #     host=os.getenv("EC2_DB_HOST"),
    #     port=os.getenv("EC2_DB_PORT"),
    #     database=os.getenv("EC2_DB_NAME")
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
