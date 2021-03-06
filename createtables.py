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

    print("PostgreSQL connection is open")

    cursor = connection.cursor()

    my_query = (
        """
        CREATE TABLE IF NOT EXISTS patient(
        patientid INTEGER PRIMARY KEY,
        patientfname VARCHAR,
        patientlname VARCHAR,
        patientsuburb VARCHAR);
        """,
        """
        CREATE TABLE IF NOT EXISTS Doctor(
            DoctorId INTEGER PRIMARY KEY,
            DoctorFName VARCHAR,
            DoctorLName VARCHAR,
            DoctorSuburb VARCHAR
            );
        """,
        """
        INSERT INTO Patient VALUES
        (201901, 'Jack', 'D', 'Rhodes'),
        (201902, 'Dan', 'J', 'Ryde'),
        (201903, 'Rachel', 'K', 'Medowbank'),
        (201904, 'Karen', 'L', 'Rhodes') ON CONFLICT DO NOTHING;
        """,
        """
        INSERT INTO Doctor VALUES
        (201, 'SAM', 'K', 'Medowbank'),
        (202, 'Mac', 'B', 'Rhodes'),
        (303, 'Randy', 'L', 'Ryde'),
        (404, 'Hans', 'L', 'Silverwater'),
        (406, 'Dan', 'K', 'Medowbank'),
        (413, 'Mars', 'B', 'Rhodes'),
        (423, 'Roshan', 'L', 'Rhodes'),
        (408, 'Brian', 'N', 'Silverwater') ON CONFLICT DO NOTHING;
        """
    )

    for query in my_query:
        cursor.execute(query)

    print("PostgreSQL queries executed")

    connection.commit()


except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

else:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
