from sqlalchemy import create_engine, Column, Float, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

Base = declarative_base()

class SessionLog(Base):
    __tablename__='sessions'
    
    timestamp = Column(DateTime, primary_key=True)
    cpu_before = Column(Float)
    cpu_after = Column(Float)
    ram_before = Column(Float)
    ram_after = Column(Float)
    disk_before = Column(Float)
    disk_after = Column(Float)

engine = create_engine('sqlite:///cleanup_log.db', echo=False)
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

def log_session(before, after):
    session = Session()
    new_entry = SessionLog(
        timestamp=datetime.now(),
        cpu_before = before['cpu_percent'],
        cpu_after = after['cpu_percent'],
        ram_before = before['memory'],
        ram_after = after['memory'],
        disk_before = before['disk'],
        disk_after = after['disk']
    )
    session.add(new_entry)
    session.commit()
    session.close()