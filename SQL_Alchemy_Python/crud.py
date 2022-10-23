from config import DATABASE_URI
from model import Houses, Flats,Residents, Owners, Relatives,Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, scoped_session
from random import choice, randint
from datetime import date

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def set_connect():
    # Устанавливаем соединение с postgres
    connection = psycopg2.connect(user="Shupta_EA", password="20studShEA22")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # Создаем курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    sql_create_database = cursor.execute('create database liv_cooper')
    # Создаем базу данных
    cursor.close()
    connection.close()

def get_session_engine(db_uri):
    engine = create_engine(db_uri, echo=True)
    #session = scoped_session(sessionmaker(bind=engine))
    sess = scoped_session(sessionmaker(bind=engine))
    return sess, engine


def create_database(db_uri):
    ses, engine = get_session_engine(db_uri)
    #engine = create_engine(db_uri)
    #ses = scoped_session(sessionmaker(bind=engine))
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return ses


def fill_db(session):

    def read_csv(name):
        with open(f'./static_data/{name}.csv', 'r', encoding="utf-8") as f:
            result = [line.strip() for line in f]
        return result

    house = read_csv('Houses')
    flats = read_csv('Flats')
    resident = read_csv('Residents')
    owner = read_csv('Owners')
    relat = read_csv('Relatives')

    for i in house:
        s = i.split()
        h = Houses(address=str(s[0]), number_of_rooms=int(s[1]), living_space=float(s[2]))
        session.add(h)


    for i in flats:
        s = i.split()
        f = Flats(house_id=int(s[0]), amount_of_space=float(s[1]), number_of_rooms=int(s[2]), apartment_number=int(s[3]))
        session.add(f)

    for i in resident:
        s = i.split()
        res = Residents(flat_id=int(s[0]), full_name=str(s[1]))
        session.add(res)

    for i in owner:
        s = i.split()
        o = Owners(flat_id=int(s[0]), benefit_type=str(s[1]), account_number=int(s[2]), full_name=str(s[3]))
        session.add(o)

    for i in relat:
        s = i.split()
        rel = Relatives(owner_id=int(s[0]), resident_id=int(s[1]))
        session.add(rel)
    session.commit()



if __name__ == '__main__':
    print('connecting...')

    session = set_connect()
    session = create_database(DATABASE_URI)


    fill_db(session)
    print('db created!')
    session.close()
    print('session closed')
