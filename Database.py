
def main():
    import sqlite3
    import os.path
    import pandas as pd


    # import file and load it to sql
    data = pd.read_csv("diamonds_table.csv")
    data_lines = data['SHAPE']

    # Create a sqlite table
    isExist = os.path.isfile('diamond.db')
    conn = sqlite3.connect('diamond.db')
    c = conn.cursor()

    if isExist:
        conn.executescript("""DROP  TABLE diamonds""")

    c.execute("""CREATE TABLE diamonds (
                       shape nchar,
                       size nchar,
                       color nchar,
                       clarity nchar,
                       cut integer,
                       florecent integer,
                       price integer
                   )""")
    conn.commit()

    # Insert diamonds to the table
    for i in range(0, data_lines.size):
        row = data.iloc[i]
        print(row[4])
        print(row[6])
        c.execute("INSERT INTO diamonds (shape,size,color,clarity,cut,florecent,price) VALUES (?,?,?,?,?,?,?)",
                      (row[0], row[1], row[2], row[3], int(row[4]), int(row[5]), int(row[6])))
    conn.commit()


main()
