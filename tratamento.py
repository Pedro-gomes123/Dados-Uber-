import duckdb as db 

con = db.connect()


con.execute("""  
    CREATE OR REPLACE  TABLE rice AS 
    SELECT  * FROM 'ncr_ride_bookings.csv';

""")

df =  con.execute(" SELECT * FROM  rice limit 10;").fetchdf()

print(df)