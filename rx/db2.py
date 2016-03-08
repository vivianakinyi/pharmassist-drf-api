import csv
import psycopg2

with open('RxTerms201512.txt') as csvfile:
    reader = csv.reader(csvfile, delimiter='|')
    for row in reader:
        db = psycopg2.connect(database="new_pharm", host="localhost",
                              port="5432", user="new_pharm",
                              password="new_pharm")
        cursor = db.cursor()
        sql = """
        INSERT INTO pharmacies_drugs(
            RXCUI,GENERIC_RXCUI,TTY,FULL_NAME,\
            RXN_DOSE_FORM,FULL_GENERIC_NAME,BRAND_NAME,DISPLAY_NAME,\
            ROUTE,NEW_DOSE_FORM,STRENGTH,SUPPRESS_FOR,DISPLAY_NAME_SYNONYM,\
            IS_RETIRED,SXDG_RXCUI,SXDG_TTY,SXDG_NAME,PSN)\
             VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',\
                '{}','{}','{}','{}','{}','{}','{}','{}')""".format(row[0],\
                row[1].replace("'", ""), row[2].replace("'", ""), row[3].replace("'", ""), row[4].replace("'", ""), row[5].replace("'", ""),
                row[6].replace("'", ""), row[7].replace("'", ""), row[8].replace("'", ""), row[9].replace("'", ""),
                row[10].replace("'", ""), row[11].replace("'", ""),row[12].replace("'", ""),row[13].replace("'", ""), row[14].replace("'", ""),
                row[15].replace("'", ""),row[16].replace("'", ""),row[17].replace("'", ""))
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
