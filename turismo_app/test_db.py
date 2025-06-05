from sqlalchemy import text
from turismo_app.database import SessionLocal

# este mis amores es para q vena que la conexion si sirve 

def test_connection():
    try:
        session = SessionLocal()
        result = session.execute(text("SELECT 1"))
        print("✅ Conexión exitosa a la base de datos.")
    except Exception as e:
        print(f"❌ Error al conectar a la base de datos: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    test_connection()
