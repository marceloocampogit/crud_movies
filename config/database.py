import os
from sqlalchemy import create_engine #Motor de base de datos
from sqlalchemy.orm.session import sessionmaker #Crear una sesion en la base de datos
from sqlalchemy.ext.declarative import declarative_base #Manipular tablas

sqlite_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.abspath(__file__))

# Creo direccion de base de datos
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

# Creo motor de base de datos con mi url
engine = create_engine(database_url, echo=True)

# Creo una sesion con mi motor de base de datos
session = sessionmaker(bind=engine)

base = declarative_base()