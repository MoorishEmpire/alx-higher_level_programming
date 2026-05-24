#!/usr/bin/python3
"""
prints all City objects from the database 'hbtn_0e_14_usa'
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session


if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    tuples_res = session.execute(
        select(State.name, City.id, City.name)
        .join(City, State.id == City.state_id)
        .order_by(City.id)
    ).all()

    for state_name, city_id, city_name in tuples_res:
        print(f'{state_name}: ({city_id}) {city_name}')

    session.close()
