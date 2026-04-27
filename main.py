from extract import get_weather
from transform import transform_weather
from load import load_weather
from pydantic import ValidationError
from logger import get_logger

logger = get_logger("main")

CIUDADES = ["Lima", "Cusco", "Arequipa"]

def run_etl():
    logger.info("=== Iniciando ETL de clima ===")
    exitosos = 0
    fallidos = 0

    for ciudad in CIUDADES:
        try:
            raw   = get_weather(ciudad)
            clean = transform_weather(raw)
            load_weather(clean)
            exitosos += 1
        except ValidationError as e:
            logger.warning(f"Dato invalido en {ciudad}: {e}")
            fallidos += 1
        except Exception as e:
            logger.error(f"Fallo {ciudad}: {e}")
            fallidos += 1

    logger.info(f"=== ETL finalizado: {exitosos} exitosos, {fallidos} fallidos ===")

if __name__ == "__main__":
    run_etl()