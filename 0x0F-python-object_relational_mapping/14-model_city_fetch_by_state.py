#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}",
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State.name, City.id, City.name).join(City)

    for state_name, city_id, city_name in query:
        print(f"{state_name}: ({city_id}) {city_name}")

    session.close()
