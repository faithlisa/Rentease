from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a new instance of the declarative_base class
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    remember_me = Column(Boolean, default=False)

    def __repr__(self):
        return f"<User(username='{self.username}', remember_me={self.remember_me})>"

# Create an engine that stores data in the local directory's sqlite.db file.
engine = create_engine('sqlite:///users.db')

# Create all tables in the engine. This is equivalent to "Create Table" statements in raw SQL.
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

# Example of adding a new user
new_user = User(username='exampleuser', password='examplepassword', remember_me=True)
session.add(new_user)
session.commit()

# Querying the database
for user in session.query(User).all():
    print(user)

# Close the session
session.close()
