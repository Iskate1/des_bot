from sqlalchemy import create_engine
import psycopg2
import cfg

print("Connecting to DB...")

# conn = psycopg2.connect(
#     dbname=cfg.DB_NAME,
#     host=cfg.DB_HOST,
#     user=cfg.DB_USER,
#     password=cfg.DB_PASSWORD,
#     port=cfg.DB_PORT
# )

# Подключение к серверу PostgreSQL на localhost с помощью psycopg2 DBAPI
engine = create_engine("postgresql+psycopg2://{}:{}@{}:{}/cfg.DB_NAME"
                       .format(cfg.DB_USER, cfg.DB_PASSWORD, cfg.DB_HOST, DB_PORT))
engine.connect()

print("Connection success")
