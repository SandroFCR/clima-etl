import mysql.connector
import os
from dotenv import load_dotenv
from logger import get_logger

load_dotenv()
logger = get_logger("load")

def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )

def init_db():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clima (
            id INT AUTO_INCREMENT PRIMARY KEY,
            ciudad VARCHAR(255) NOT NULL,
            pais VARCHAR(255) NOT NULL,
            temperatura FLOAT NOT NULL,
            sensacion FLOAT NOT NULL,
            humedad INT NOT NULL,
            descripcion VARCHAR(255) NOT NULL,
            viento_kmh FLOAT NOT NULL,
            timestamp VARCHAR(255) NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    logger.info("Tabla 'clima' inicializada")

def load_weather(data: dict):
    try:
        init_db()
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO clima
            (ciudad, pais, temperatura, sensacion, humedad, descripcion, viento_kmh, timestamp)
            VALUES
            (%(ciudad)s, %(pais)s, %(temperatura)s, %(sensacion)s, %(humedad)s,
             %(descripcion)s, %(viento_kmh)s, %(timestamp)s)
        """, data)
        conn.commit()
        conn.close()
        logger.info(f"Guardado exitoso: {data['ciudad']} - {data['temperatura']}C")
    except mysql.connector.Error as e:
        logger.error(f"Error al guardar en MySQL: {e}")
        raise