#!/usr/bin/python3
""" script that lists all State objects """

from relationship_city import Base, City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name_db = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, name_db),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    sts = session.query(State).order_by(State.id).all()
    for st in sts:
        print('{}: {}'.format(st.id, st.name))
        for ct in st.cities:
            print('	{}: {}'.format(ct.id, ct.name))
