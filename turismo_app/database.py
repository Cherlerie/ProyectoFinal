from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos no lo toquen plis 
USER = "turismo_bd"
PASSWORD = "reoteamo"
HOST = "mysql-turismo.alwaysdata.net"
DB_NAME = "turismo_bd"

# URL de conexión para PyMySQL
DATABASE_URL = "mysql+pymysql://turismo:reoteamo@mysql-turismo.alwaysdata.net/turismo_bd"
# DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
