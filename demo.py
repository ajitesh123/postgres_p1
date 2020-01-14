import psycopg2

connection = psycopg2.connect('dbname=persondb user=ajitesh')

cur = connection.cursor()

cur.execute("drop table if exists users;")

cur.execute("""
    create table users(
        id integer primary key,
        description varchar not null
    );
""")

cur.execute('insert into users(id, description) values(%s, %s);', (1, 'Yay this runs'))

connection.commit()
connection.close()
cur.close()
