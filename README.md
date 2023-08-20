# Simple RESTAPI _FastAPI, JWT & OAuth._

## Index

1. [Summary](#summary).
2. [How to run it](#how-to-run-it).
3. [Endpoints](#endpoints).

---

## Summary

Hi I'm **Brayan Barreto** a Junior **Backend Developer** and I want to explain you this little project.

It's a simple RESTAPI that uses **FastAPi** and **JWT**.

In this project I manage:

- **HTTP** protocols.
- Authentication with **OAuth**.
- A database with **SQL**.
- Creating and checking **JSON Web Tokens (JWT)**.
- Unit tests with **PyTest**.

All this using the framework **"FastAPI"**.

If you want to proof it, follow the steps explained in the section [How to run it](#how-to-run-it).

---

## How to run it

1. [Create Database](#create-database-mysql).
2. [Enviroment Variables](#enviroment-variables).
3. [Install Requirements](#install-requirements).
4. [Testing](#testing).
5. [Proof API](#proof-api).

### Create Database _(MySQL)_

Run the query written in the file **"ddbb.sql"** ubicated in the directory **"src\database"** on PHPMyAdmin or MySQLWorkBench.

It will create a database with all the neccessary to run the project.

### Enviroment Variables

If you want to run it, you need to create a **".env"** file with the next variables:

```env
JWT_KEY="JWT_secret_key"
JWT_ALGORITHM="JWT_algorithm"
JWT_TOKEN_DURATION="JWT_token_duration_in_minutes"

MYSQL_HOST="database_host"
MYSQL_PORT="database_port"
MYSQL_USER="database_user"
MYSQL_PASSWORD="database_password"
MYSQL_DATABASE="database_name"
```

Obviously replacing all the values. For example:

```env
JWT_KEY="T6859b7Fde4e68cb65041b88a7ad5214df"
JWT_ALGORITHM="HS256"
JWT_TOKEN_DURATION=2

MYSQL_HOST="localhost"
MYSQL_PORT=3306
MYSQL_USER="root"
MYSQL_PASSWORD="hello123"
MYSQL_DATABASE="simpleapi_example"
```

### Install Requirements

First open the command console, then make sure you are in the root directory of the project and finally run the next command on the console:

```bash
py -m pip install -r requirements.txt
```

### Testing

Open the command console and get ubicate in the next directory **"src\tests\services"**, after that run the next command:

```bash
pytest test_authservices.py
```

And you should see a message like this:

```bash
collected 4 items

test_authservices.py ....                       100%

================= 4 passed in 2.89s =================
```

It meants that everything is ok.

### Proof API

Finally you can check the API with a **"API testing"** app.

Open the command line in the root of the project and run the next command:

```bash
py -m uvicorn index:app --reload
```

It's going to deploy the api on your local host (127.0.0.1).

Then you should see a message like this:

```bash
←[32mINFO←[0m:     Uvicorn running on ←[1mhttp://127.0.0.1:8000←[0m (Press CTRL+C to quit)
←[32mINFO←[0m:     Started reloader process [←[36m←[1m9176←[0m] using ←[36m←[1mStatReload←[0m
←[32mINFO←[0m:     Started server process [←[36m9140←[0m]
←[32mINFO←[0m:     Waiting for application startup.
←[32mINFO←[0m:     Application startup complete.
```

You'll copy the server connection (**127.0.0.1:8000** or **localhost:8000**) in the **API testing** and there you can check all the endpoints.

---

## Endpoints

Information: **IT'S SO IMPORTANT TO SEND A BEARER TOKEN WHEN YOU USE THE ENDPOINTS OF INDEX & USER (STILL IT'S EMPTY)**

If you want to know what are all the available **endpoints** run the server and copy this on the navigator: **"localhost:8000/docs"**.

There you can see all the **endpoints** of the projects and which HTTP verbs you need to select for **running eachone**.

---
