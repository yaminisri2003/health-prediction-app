from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# Database connection URL
DATABASE_URL = "sqlite:///health_data.db"

# Create database engine
engine = create_engine(DATABASE_URL)

# Base class for ORM models
Base = declarative_base()


# Patient Table Model
class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    dob = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    glucose = Column(Float, nullable=False)
    haemoglobin = Column(Float, nullable=False)
    cholesterol = Column(Float, nullable=False)
    remarks = Column(String)


# Create session factory
SessionLocal = sessionmaker(bind=engine)


# Create tables in database
Base.metadata.create_all(bind=engine)