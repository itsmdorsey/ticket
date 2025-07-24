from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

#connect to postgresql database
DATABASE_URL = "postgresql://userdb:userdb@192.168.1.243/ticket"
engine = create_engine(DATABASE_URL, echo=True)

#list all tables in postgresql database
Base = declarative_base()
class Ticket(Base):
    __tablename__ = 'tickets'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
# Create the table in the database
Base.metadata.create_all(engine)
# Create a session factory
Session = sessionmaker(bind=engine)
# Create a session
session = Session() 
# Function to add a new ticket
def add_ticket(title, description=None):
    new_ticket = Ticket(title=title, description=description)
    session.add(new_ticket)
    session.commit()
    return new_ticket
session.close()

add_ticket("DB is down", "the databse is not resonding")