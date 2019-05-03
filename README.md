# sample-python-api
backend engineer assessment

## Requirements

This project uses venv as isolated python environment for installation and running. Therefore, venv must be installed. All dependency library informations can be find in install.sh.
The project uses mariadb as the database and is tested with gunicorn in linux environment.

## Installation

Install all python module dependencies in requirements.txt

## Delpoy

```
gunicorn __main__:api
```

### Linux

installation mariadb

```
sudo apt-get mariadb
```

## Usage

newlines are intentionally added for better reading 

* **C**RUD

```
curl -XGET http://127.0.0.1:8000/create 
	-H "Content-Type:application/json" 
	-d '{"customer_name":"NAME","customer_dob":"YYYY-MM-DD"}'
```

* C**R**UD

```
curl -XGET http://127.0.0.1:8000/read 
	-H "Content-Type:application/json" 
	-d '{"customer_name":"NAME"}'
```

* CR**U**D

```
curl -XGET http://127.0.0.1:8000/update 
	-H "Content-Type:application/json" 
	-d '{"customer_name":"NAME","customer_dob":"YYYY-MM-DD","customer_id":"ID_num"}'
```

* CRU**D**

```
curl -XGET http://127.0.0.1:8000/delete 
	-H "Content-Type:application/json" 
	-d '{"customer_name":"NAME"}'
```

### query of "to get names of the youngest customers"

```
select * from customers order by customer_dob limit 1;
```