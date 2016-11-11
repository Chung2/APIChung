import datetime
import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='marvelgamescore')

cursor = connection.cursor()

def Gegevensuithalen() :
    sql = 'SELECT * FROM score'

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            naam = row[0]
            datum = row[1]
            score = row[2]
            print('naam= %s,datum= %s,score= %d' % \
                  (naam, datum, score))

    except:
        print('haha het werkt niet')
    connection.close()

def Gegevensinvoeren(naam,datumVandaag,punten):

    sql ='INSERT INTO score(gebruiker, ' \
         'datum, score)VALUES("%s","%s","%d")' % \
         (naam,datumVandaag,punten)

    try:
        cursor.execute(sql)
        connection.commit()
    except  pymysql.Error as e:
        connection.rollback()
        print('Error Mysql')
    connection.close()
