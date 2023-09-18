##  `api/users/register/ `
**User Register Endpoint**
```text
    Description:
    - This endpoint allows users to register and create a new account.
    
    Accepted HTTP Method:
    - POST

    Permissions:
    - AllowAny (Open access)

    Input Parameters:
    - first name (string): User's first name.
    - last name (string): User's last name.
    - email (string): User's email address.
    - password (string): User's password.


    Responses:
    - HTTP 201 Created:
        - Registration successful. Returns created account with an HTTP 201 status code.
    - HTTP 400 Bad Request:
        - Invalid input parameters. Returns an empty response with an HTTP 400 status code.
    
```

Example POST Request:

```python
{
    "first_name": "Cristian",
    "last_name": "Finica",
    "email": "user@example.com",
    "password": "Password"
}
 ```

Example Response:

```python
{
    "id": 3,
    "first_name": "string2",
    "last_name": "string",
    "email": "user2@example.com",
    "location": "Chisinau"
}
```
______________________________________________________________________________________________________________________________
# `api/users/login/`
 **User Login Endpoint**
```text
    Description:
    - This endpoint allows users to login and authenticate their account.
    
    Accepted HTTP Method:
    - POST

    Permissions:
    - AllowAny (Open access)

    Input Parameters:
    - email (string): User's email address.
    - password (string): User's password.

    Responses:
    - HTTP 200 OK:
        - Successful authentication. Returns a JSON object containing authentication tokens.
    - HTTP 401 Unauthorized:
        - Authentication failed due to an invalid password / email. Returns a JSON object with an error message.
```

Example POST Request:

```python
{
    "email": "user@example.com",
    "password": "Password"
}
```

Example Response:

```python
{
    "refresh": "string",
    "access": "string"
}
```
  