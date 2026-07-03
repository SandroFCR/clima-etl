# 🌤️ clima-etl

**Pipeline ETL en Python que extrae, transforma y carga datos meteorológicos en tiempo real desde la API de OpenWeather hacia una base de datos MySQL.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?logo=mysql&logoColor=white)
![ETL](https://img.shields.io/badge/Data-ETL_Pipeline-orange)
![API](https://img.shields.io/badge/API-OpenWeather-yellow)

---

## 📌 Descripción

`clima-etl` es un pipeline de **Data Engineering** que automatiza el proceso completo de **Extract, Transform, Load (ETL)** para datos climáticos de múltiples zonas geográficas. El proyecto consume la **OpenWeather API**, normaliza y transforma la información recibida, y la persiste en una base de datos relacional **MySQL** para su posterior análisis.

Este proyecto forma parte de mi camino de aprendizaje en **Ingeniería de Datos**, aplicando conceptos de integración de APIs REST, modelado de datos y persistencia en bases de datos SQL.

## ⚙️ ¿Qué hace?

1. **Extract** (`extract.py`) — Se conecta a la **OpenWeather API** y obtiene datos climáticos en tiempo real de distintas zonas configuradas.
2. **Transform** (`transform.py`) — Limpia, valida y estructura los datos crudos (JSON) en un formato tabular listo para almacenar.
3. **Load** (`load.py`) — Inserta los registros procesados en la tabla `clima` de una base de datos **MySQL**, a través de la función `load_weather()`.
4. **Model** (`model.py`) — Define la estructura/esquema de los datos climáticos utilizados a lo largo del pipeline.
5. **Orquestación** (`main.py`) — Ejecuta el flujo ETL completo de principio a fin.

## 🛠️ Stack tecnológico

| Categoría | Tecnología |
|---|---|
| Lenguaje | Python |
| Fuente de datos | OpenWeather API (REST) |
| Base de datos | MySQL |
| Arquitectura | ETL Pipeline (Extract → Transform → Load) |
| Configuración | Variables de entorno (`.env`) |

## 📂 Estructura del proyecto

```
clima-etl/
├── extract.py      # Extracción de datos desde OpenWeather API
├── transform.py     # Limpieza y transformación de los datos
├── load.py           # Carga de datos en MySQL (tabla `clima`)
├── model.py          # Modelo/esquema de datos
├── main.py            # Orquestador del pipeline ETL
└── .env.example       # Variables de entorno necesarias
```

## 🚀 Instalación y uso

```bash
# Clonar el repositorio
git clone https://github.com/SandroFCR/clima-etl.git
cd clima-etl

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
```

Configura tu archivo `.env` con:

```
OPENWEATHER_API_KEY=tu_api_key
MYSQL_USER=tu_usuario
MYSQL_PASSWORD=tu_password
MYSQL_DATABASE=tu_base_de_datos
```

Ejecutar el pipeline:

```bash
python main.py
```

## 🔮 Mejoras futuras

- [ ] Orquestación automática con **cron** o **Apache Airflow**
- [ ] Dashboard de visualización de datos históricos
- [ ] Contenerización con **Docker**
- [ ] Tests unitarios para las etapas de transformación

## 👤 Autor

**Sandro** — [GitHub](https://github.com/SandroFCR)
