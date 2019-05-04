# sample-python-api
backend engineer assessment

## Requirements

This project uses venv as isolated python environment for installation and running. Therefore, venv must be installed. All dependency library informations can be find in install.sh.
The project uses mariadb as the database and is tested with gunicorn in linux environment.

## Installation

Install all python module dependencies in requirements.txt

### Linux

mariadb installation

```
sudo apt-get mariadb
```

## Delpoy

Make necessary in information.py for the database connection before running the line below.

```
gunicorn __main__:api
```

## Usage

newlines are intentionally added for better reading 


* **C**RUD

```
curl -XGET http://127.0.0.1:8000/create 
	-d '{"customer_name":"NAME","customer_dob":"YYYY-MM-DD"}'
```

* C**R**UD

```
curl -XGET http://127.0.0.1:8000/read 
	-d '{"customer_name":"NAME"}'
```

* CR**U**D

```
curl -XGET http://127.0.0.1:8000/update 
	-d '{"customer_name":"NAME","customer_dob":"YYYY-MM-DD","customer_id":"ID_num"}'
```

* CRU**D**

```
curl -XGET http://127.0.0.1:8000/delete 
	-d '{"customer_name":"NAME"}'
```

### query of "to get names of the youngest customers"

```
select * from customers order by customer_dob limit 1;
```