import csv
import psycopg2

with open('chemists.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        db = psycopg2.connect(database="new_pharm", host="localhost",
                              port="5432", user="new_pharm",
                              password="new_pharm")
        cursor = db.cursor()
        sql = """
        INSERT INTO pharmacies_pharmacy(
            NO,NAME,TOWN,STREET,COUNTY)\
             VALUES ('{}','{}','{}','{}','{}')""".format(row[0],\
                row[1].replace("'", ""), row[2].replace("'", ""), row[3].replace("'", ""), row[4].replace("'", ""))

        print(sql)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except Exception as e:
            print(e.message)
            # Rollback in case there is any error

db.close()
