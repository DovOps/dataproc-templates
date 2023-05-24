# Common
GCP_PROJECT = "GCP_PROJECT"
PROJECT = "PROJECT"
REGION = "REGION"
GCS_STAGING_LOCATION = "GCS_STAGING_LOCATION"
SUBNET = "SUBNET"
IS_PARAMETERIZED = "IS_PARAMETERIZED"
MAX_PARALLELISM =  "MAX_PARALLELISM"
SERVICE_ACCOUNT = "SERVICE_ACCOUNT"
JDBCTOJDBC_OUTPUT_MODE_ARG="jdbctojdbc.output.mode"
BATCH_SIZE_ARG="jdbctojdbc.output.batch.size"

# Write modes
OUTPUT_MODE_OVERWRITE = "overwrite"
OUTPUT_MODE_APPEND = "append"


# MYSQL TO SPANNER
## Command Line Arguments
OUTPUT_NOTEBOOK_ARG = "output.notebook"
MAX_PARALLELISM_ARG = "max.parallelism"
MYSQL_HOST_ARG = "mysql.host"
MYSQL_PORT_ARG = "mysql.port"
MYSQL_USERNAME_ARG = "mysql.username"
MYSQL_PASSWORD_ARG = "mysql.password"
MYSQL_DATABASE_ARG = "mysql.database"
MYSQLTABLE_LIST_ARG = "mysql.table.list"
MYSQL_OUTPUT_SPANNER_MODE_ARG = "mysql.output.spanner.mode"
SPANNER_INSTANCE_ARG = "spanner.instance"
SPANNER_DATABASE_ARG = "spanner.database"
# provide table & pk column which do not have PK in MYSQL "{"table_name":"primary_key"}"
SPANNER_TABLE_PRIMARY_KEYS_ARG = "spanner.table.primary.keys"

## Notebook Arguments
MYSQL_HOST = "MYSQL_HOST"
MYSQL_PORT = "MYSQL_PORT"
MYSQL_USERNAME = "MYSQL_USERNAME"
MYSQL_PASSWORD = "MYSQL_PASSWORD"
MYSQL_DATABASE = "MYSQL_DATABASE"
MYSQLTABLE_LIST = "MYSQLTABLE_LIST"
MYSQL_OUTPUT_SPANNER_MODE = "MYSQL_OUTPUT_SPANNER_MODE"
SPANNER_INSTANCE = "SPANNER_INSTANCE"
SPANNER_DATABASE = "SPANNER_DATABASE"
SPANNER_TABLE_PRIMARY_KEYS = "SPANNER_TABLE_PRIMARY_KEYS"

#ORACLE TO POSTGRES
## Command Line Arguments
ORACLE_HOST_ARG = "oracle.host"
ORACLE_PORT_ARG = "oracle.port"
ORACLE_USERNAME_ARG = "oracle.username"
ORACLE_PASSWORD_ARG = "oracle.password"
ORACLE_DATABASE_ARG = "oracle.database"
ORACLETABLE_LIST_ARG = "oracle.table.list"
POSTGRES_HOST_ARG="<POSTGRES_HOST"
POSTGRES_PORT_ARG="POSTGRES_PORT"
POSTGRES_USERNAME_ARG="POSTGRES_USERNAME"
POSTGRES_PASSWORD_ARG="POSTGRES_PASSWORD"
POSTGRES_DATABASE_ARG="POSTGRES_DATABASE"
POSTGRES_SCHEMA_ARG="POSTGRES_SCHEMA"



## Notebook Arguments
ORACLE_HOST = "ORACLE_HOST"
ORACLE_PORT = "ORACLE_PORT"
ORACLE_USERNAME = "ORACLE_USERNAME"
ORACLE_PASSWORD = "ORACLE_PASSWORD"
ORACLE_DATABASE = "ORACLE_DATABASE"
ORACLETABLE_LIST = "ORACLETABLE_LIST"
POSTGRES_HOST="<POSTGRES_HOST"
POSTGRES_PORT="POSTGRES_PORT"
POSTGRES_USERNAME="POSTGRES_USERNAME"
POSTGRES_PASSWORD="POSTGRES_PASSWORD"
POSTGRES_DATABASE="POSTGRES_DATABASE"
POSTGRES_SCHEMA="POSTGRES_SCHEMA"