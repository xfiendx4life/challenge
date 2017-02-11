from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import hashlib

from db_ import Leader, Base
def initialize_db():
    engine = create_engine('sqlite:///users.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session

def db_query():
    session = initialize_db()
    person = session.query(Leader).all()
    return person
 
def update(leader_name, leader_password, rating):
    session = initialize_db()
    name = ''
    try:
        name = session.query(Leader).filter(Leader.name == leader_name).all()[0].name
    except:
        leader_password = hashlib.md5(leader_password.encode("utf-8")).hexdigest()
        new_leader = Leader(name = leader_name, password = leader_password, rating=rating)
        session.add(new_leader)
        session.commit()
        print('name added')
        return True
    return False

