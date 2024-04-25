#!/bin/bash

# Load MySQL environment variables from .env file
if [ -f .env ]; then
    export $(cat .env | grep -v '#' | xargs)
else
    echo "Error: .env file not found."
    exit 1
fi

# Path to the SQL dump file (schema.sql)
SQL_DUMP_FILE="/vagrant/ntfs/zabbix-sql-scripts-6.4.5-release.gz"

# Check if the gzipped SQL dump file exists
if [ ! -f "$SQL_DUMP_FILE" ]; then
    echo "Error: $SQL_DUMP_FILE does not exist."
    exit 1
fi

# Decompress the gzipped SQL dump file
gunzip -c "$SQL_DUMP_FILE" > schema.sql

# Import the schema using docker exec
docker exec -i mysql-zabbix mysql -u root -pP@ssw0rd#001 zbxlabdb < schema.sql

# Clean up the temporary schema.sql file
rm schema.sql

# The import was successful
echo "Schema import successful."