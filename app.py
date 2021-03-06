from flask import Flask, request, jsonify
from flask.ext.cors import CORS, cross_origin

# Local pack
from service import service

app = Flask(__name__)

cors = CORS(app, resources={r"/employeesList": {"origins": "http://localhost:4200"}})

@app.route("/")
def hello():
    return jsonify({"message": "Welcome to BFF service"})

# List employees
@app.route("/employeesList", methods=['GET'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def employeesList():
    """
    Expected request body
    Type: json
    body: none

    Expected response body
    Type: json
    body:
        [{
        "employee_number": STRING,
        "name": {
            "last": STRING,
            "first": STRING,
            "middle": STRING
        },
        ...]
    """

    return flask.jsonify(service.employeesList()), 200, {'Access-Control-Allow-Origin': '*'}


# Return if employee is absent
@app.route("/isEmployeeAbsent", methods=['GET'])
def isAbsent():
    if request.method == 'GET':
        """
        Expected request body
        Type: json
        body:
            {
                "employee_number": STRING,
                "date": DATE
            }

        Expected response body
        Type: json
        body:
            {
                "isAbsent": BOOL
            }
        """
        return jsonify(service.isEmployeeAbsent(request.json)), 200, {'Access-Control-Allow-Origin': 'http://localhost'}


# Status employee on specific day
@app.route("/employeeStatusOnDate", methods=['GET'])
def reasonAbsence():
    if request.method == 'GET':
        """
        Expected request body
        Type: json
        body:
            {
                "employee_number": STRING,
                "date": DATE
            }

        Expected response body
        Type: json
        body:
            {
                "status": STRING
            }
        """
        return jsonify(service.statusEmployeeOnDate(request.json)), 200, {'Access-Control-Allow-Origin': 'http://localhost:4200'}


# Group employees for Position
@app.route("/groupEmployeeByPosition", methods=['GET'])
def positionemployeeGroup():
    if request.method == 'GET':
        """
        Expected request body
        Type: json
        body:
            none

        Expected response body
        Type: json
        body:
            [
                {
                    "position_title": STRING
                    "employees_numbers":
                    [
                        "employee_number1",
                        "employee_number2",
                        ...
                        "employee_numberN",
                    ]
                },
                ...
            ]
        """
        return jsonify(service.groupEmployeeByPosition()), 200, {'Access-Control-Allow-Origin': 'http://localhost:4200'}


# Group employees for Position
@app.route("/groupEmployeeByWorkload", methods=['GET'])
def groupEmployeeByWorkload():
    if request.method == 'GET':
        """
        Expected request body
        Type: json
        body:
            none

        Expected response body
        Type: json
        body:
            [
                {
                    "workload": STRING
                    "employees_numbers":
                    [
                        "employee_number1",
                        "employee_number2",
                        ...
                        "employee_numberN",
                    ]
                },
                ...
            ]
        """
        return jsonify(service.groupEmployeeByWorkload()), 200, {'Access-Control-Allow-Origin': 'http://localhost:4200'}


# Get employee name employees by id
@app.route("/employeeName", methods=['GET'])
def getemployeeName():
    if request.method == 'GET':
        """
        Expected request body
        Type: json
        body:
            {
                "employee_number": STRING,
            }
        Expected response body
        Type: json
        body:
            {
                "name": {
                    "last": STRING,
                    "first": STRING,
                    "middle": STRING
                }
            }
        """
        return jsonify(service.employeeNameById(request.json)), 200, {'Access-Control-Allow-Origin': '*'}


# Get employee phone by id
@app.route("/employeePhone", methods=['GET'])
def getemployeePhone():
    if request.method == 'GET':
        """
        Expected request body
        Type: json
        body:
            {
                "employee_number": STRING,
            }

        Expected response body
        Type: json
        body:
            {
                "telephone": STRING,
            }
        """
        return jsonify(service.employeePhoneById(request.json)), 200, {'Access-Control-Allow-Origin': 'http://localhost:4200'}


# Get employee adress by id
@app.route("/employeeAdress", methods=['GET'])
def getemployeeAdress():
    if request.method == 'GET':
        """
        Expected request body
        Type: json
        body:
            {
                "employee_number": STRING,
            }

        Expected response body
        Type: json
        body:
            {
                "address": {
                    "description": STRING,
                    "city": STRING,
                    "state": STRING,
                    "zip": STRING
                }
            }
        """
        return jsonify(service.employeeAdressById(request.json)), 200, {'Access-Control-Allow-Origin': 'http://localhost:4200'}


# Get employee position by id
@app.route("/employeePosition", methods=['GET'])
def getemployeePosition():
    if request.method == 'GET':
        """
        Expected request body
        Type: json
        body:
            {
                "employee_number": STRING,
            }

        Expected response body
        Type: json
        body:
            "position": {
                "title": STRING,
                "salary": FLOAT,
                "hours": INTEGER,
                "date_of_employment": DATE
            }
        """
        return jsonify(service.employeePositionById(request.json)), 200, {'Access-Control-Allow-Origin': 'http://localhost:4200'}


# List employees absences on a date
@app.route("/listAbsencesOnDate", methods=['GET'])
def getlistAbsencesOnDate():
    if request.method == 'GET':
        """
        Expected request body
        Type: json
        body:
            {
                "date": DATE,
            }

        Expected response body
        Type: json
        body:
            "employees":
                [
                    "employeeNumber1",
                    "employeeNumber2",
                    ...
                    "employeeNumberN",
                ]
        """
        return jsonify(service.listAbsencesOnDate(request.json)), 200, {'Access-Control-Allow-Origin': 'http://localhost:4200'}


# List employees absences on a date
@app.route("/listEmpoyeesInRangeSalary", methods=['GET'])
def listEmpoyeesInRangeSalary():
    if request.method == 'GET':
        """
        Expected request body
        Type: json
        body:
            {
                "initial_salary": NUMBER,
                "end_salary": NUMBER
            }

        Expected response body
        Type: json
        body:
            "employees":
                [
                    "employeeNumber1",
                    "employeeNumber2",
                    ...
                    "employeeNumberN",
                ]
        """
        return jsonify(service.listEmpoyeesInRangeSalary(request.json)), 200, {'Access-Control-Allow-Origin': 'http://localhost:4200'}


if __name__ == '__main__':
    app.run(port=3000)
