# python-bff-sql
learning create backend for frontend query data from MySQL using python


# how to build docker image
docker build -t python-bff-sql .

# how to run
## Preriquisit 
### Create docker network
    docker network create python-bff-sql
### run the MS-SQL server
    docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=P@ssw0rd" --net python-bff-sql \
    -p 1433:1433 --name sql1 --hostname sql1 --rm -d \
    mcr.microsoft.com/mssql/server:2022-latest

### create database, table, and test-data
    docker exec -it sql1 "bash"
### then you will inside the container (bash).
    /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "P@ssw0rd"
### then you in sqlcmd shell.  Then run below set of commands.
    CREATE DATABASE TestDB;
    GO
    SELECT Name from sys.databases;
    GO
    USE TestDB;
    CREATE TABLE Inventory (id INT, name NVARCHAR(50), quantity INT);
    INSERT INTO Inventory VALUES (1, 'banana', 150); INSERT INTO Inventory VALUES (2, 'orange', 154);
    GO
    SELECT * FROM Inventory ;
    GO
 
## Docker command to run the server.
    docker run --rm --name python-bff-sql --net python-bff-sql -p 5000:5000 python-bff-sql:latest 

## Example curl command to test.
    curl -v http://localhost:5000/api/capture-time


## Example of output from curl command


## Example server console log that capture the response time

## Clean up
    docker kill    python-bff-sql sql1
    docker network rm python-bff-sql
