## `/api/weather/current`

**User Weather Endpoint**

**Description:** This endpoint allows you to retrieve the current weather for the user's location.

**Accepted HTTP Method**: GET

**Permissions**: Requires user authentication. (JWT Token)

**Input Parameters**:  None

**Responses**:
   
 - **HTTP 200 OK**:
  Successful request. Returns the current weather for the user's location.
 - **HTTP 400 Bad Request**:
 Invalid location. Returns an error response with an HTTP 400 status code.
 

Example GET Request:

```
{
    "location": "Chisinau"
}
```

Example Response:

```python
{
    "location": "Chișinău",
    "temperature": 27.24,
    "weather_description": "clear sky",
    "humidity": 28,
    "wind_speed": 3.09
}
```

______________________________________________________________________________________________________________________________

## `/api/weather/search`

**Search Weather Endpoint**


**Description:** This endpoint allows you to search for weather information by city name and zip code.

**Accepted HTTP Method**: GET

**Permissions**: Requires user authentication. (JWT Token)
    
**Input Parameters**:  `search_details` *(string)*: City name or zip code.

**Responses**:
   
 - **HTTP 200 OK**:
  Successful request. Returns the current weather for the user's location.
 - **HTTP 400 Bad Request**:
 Invalid input parameters. Returns an error response with an HTTP 400 status code.

Example GET Request:
```python
{
    "search_details": "London"
}

GET / api / weather / search?search_details = London
```

Example Response:

```python
{
  "location": "London",
  "temperature": 18.67,
  "weather_description": "broken clouds",
  "humidity": 82,
  "wind_speed": 5.14
}
    
```

____________________________________________________________________________________________________________________________

## `/api/weather/forecast`

**Forecast Weather Endpoint**

**Description:** This endpoint allows you to retrieve the forecast weather for the user's location or specified location.

**Accepted HTTP Method**: GET

**Permissions**: Requires user authentication. (JWT Token)

**Optional Input Parameters**:  `search_details` *(string)*: City name or zip code.

**Responses**:
   
 - **HTTP 200 OK**:
  Successful request. Returns the current weather for the user's location.
 - **HTTP 400 Bad Request**:
 Invalid input parameters. Returns an error response with an HTTP 400 status code.


Example GET Request:
```python
{
    "search_details": "Soroca"
}

GET / api / weather / forecast?search_details=Soroca
```

Example Response:
```python
[
  {
    "day": "Monday at 12:00",
    "location": "Soroca",
    "temperature": 25.22,
    "weather_description": "clear sky",
    "humidity": 24,
    "wind_speed": 5.44
  },
  {
    "day": "Monday at 15:00",
    "location": "Soroca",
    "temperature": 25.35,
    "weather_description": "clear sky",
    "humidity": 25,
    "wind_speed": 4.03
  },
  {
    "day": "Tuesday at 00:00",
    "location": "Soroca",
    "temperature": 14.99,
    "weather_description": "few clouds",
    "humidity": 56,
    "wind_speed": 2.95
  },
  {
    "day": "Tuesday at 09:00",
    "location": "Soroca",
    "temperature": 24.7,
    "weather_description": "clear sky",
    "humidity": 31,
    "wind_speed": 8.76
  },
    
__________________________________________________________________________________________________________________________________
]

and so on until 5-7 days.
```
