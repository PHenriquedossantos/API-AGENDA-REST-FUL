# API-AGENDA-REST-FUL


<h1>API de Agenda de contatos</h1>

Status: Developing ⚠️

### API created to store information about schedules, courts, locations, payments, and so on...

## The libraries used are:

+ aniso8601==9.0.1
+ click==8.1.3
+ colorama==0.4.6
+ Flask==2.2.3
+ Flask-RESTful==0.3.9
+ Flask-SQLAlchemy==3.0.3
+ greenlet==2.0.2
+ itsdangerous==2.1.2
+ Jinja2==3.1.2
+ MarkupSafe==2.1.2
+ pytz==2022.7.1
+ six==1.16.0
+ SQLAlchemy==2.0.3
+ typing_extensions==4.5.0
+ Werkzeug==2.2.3

## The API has the following routes:

+ GET /company/ - returns all registered companies
+ POST /company/ - creates a new company
+ GET /company/:id - returns a specific company
+ PUT /company/:id - updates a specific company
+ DELETE /company/:id - deletes a specific company
+ GET /customer/ - returns all registered customers
+ POST /customer/ - creates a new customer
+ GET /customer/:id - returns a specific customer
+ PUT /customer/:id - updates a specific customer
+ DELETE /customer/:id - deletes a specific customer
+ GET /place/ - returns all available courts/fields
+ POST /place/ - creates a new court/field
+ GET /place/:id - returns a specific court/field
+ PUT /place/:id - updates a specific court/field
+ DELETE /place/:id - deletes a specific court/field
+ GET /payment/ - returns all registered payment types
+ POST /payment/ - creates a new payment type
+ GET /payment/:id - returns a specific payment type
+ PUT /payment/:id - updates a specific payment type
+ DELETE /payment/:id - deletes a specific payment type
+ GET /scheduling/ - returns all scheduled times
+ POST /scheduling/ - creates a new scheduling
+ GET /scheduling/:id - returns a specific scheduling
+ PUT /scheduling/:id - updates a specific scheduling
+ DELETE /scheduling/:id - deletes a specific scheduling
+ GET /customer/:id/horarios - returns all scheduled times for a specific customer
For each resource, the API supports CRUD operations (Create, Read, Update, and Delete). In addition, there is a route to list the scheduled times for a specific customer.

## The models used are:


## To run the API, follow these steps:

## Install the VENV
	py -m venv env
	
## Activate venv for windows
	.\env\Scripts\activate

## Install the required libraries:
	pip install -r requirements.txt

	
## Start server:
	


Informações adicionais:

Versão da API: 1.0.0
Autor: [Henrique Santos]
