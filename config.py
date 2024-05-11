# General Server Configs
import os

# default dev credentials

# dev -> Implemented in case we want to use write back(ToDB) approach later
DB_HOST = os.environ.get("DB_HOST", "aiven_link")
DB_PORT = os.environ.get("DB_PORT", "db_port")
DB_DATABASE = os.environ.get("DB_DATABASE", "db_name")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "db_password")
DB_USER = os.environ.get("DB_USER", "db_user")
ENVIRONMENT = os.environ.get("ENVIRONMENT", "env_name")


API_KEY = "TEST"
