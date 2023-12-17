#!/usr/bin/python3
"""
This script prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        state_name = sys.argv[4]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}",
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    print(f"{state.id}: {state.name}" if state else "Not found")

    session.close()
