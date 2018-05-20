#!/bin/bash

# Exit if command fails
set -e
# Treat unset variables as errors
set -u

# Set user as current account
user=$(whoami)

# Install Postgres 10
sudo sh -c "echo 'deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main' >> /etc/apt/sources.list.d/pgdg.list"
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y postgresql-common
sudo apt-get install -y postgresql-10 postgresql-contrib libpq-dev

# Create superuser account as self for local management
sudo -u postgres createuser $user -s

# Set env vars for colors
YELLOW='\033[1;33m'
NC='\033[0m'

# Collect arguments from user
# Project specific values
printf "${YELLOW}Database name:\n${NC}"
read database
printf "${YELLOW}Username:\n${NC}"
read username
printf "${YELLOW}Password:\n${NC}"
read password

# Create database and user
RUN_ON_PSQL="psql -X -U $user --set ON_ERROR_STOP=on --set AUTOCOMMIT=off postgres"
$RUN_ON_PSQL <<SQL
CREATE DATABASE $database;
CREATE USER $username WITH PASSWORD '$password';
ALTER ROLE $username SET client_encoding TO 'utf8';
ALTER ROLE $username SET default_transaction_isolation TO 'read committed';
ALTER ROLE $username SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE $database TO $username; 
ALTER USER $username CREATEDB;
commit;
SQL

exit 0
