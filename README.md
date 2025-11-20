# PySDDB
A Dynamic and Schemaless JSON Storage with REST Endpoints written in Python using the FastAPI framework.

## Why was this project made?
PySDDB's goal is not to take on big SQL Databases, but rather to provide a simple and intuitive interface for storing JSON files by transmitting them as payloads via HTTP.

It is mainly meant for small-medium apps which don't need the highest performance, but are supposed to be quick to develop.

## Planned Features
- Authentication (For example through a password)
- An Endpoint for mutating data in existing JSONs
- Being able to choose a folder to store JSONs in instead of being limited to Server-Root

## Endpoints
```POST /create/<id>```

This endpoint is for creating data. Send the JSON you want to store as a payload and the desired file name as its unique ID.

If the file was successfully created, the server will send status code ```201 Created```.

In case the file already exists, the server will respond with status code ```409 Conflict```.

---
```GET /read/<id>```

This endpoint is for reading data. The ID you enter will be the file name of the stored JSON. 

If it is found, the server will transmit the JSON file as an HTTP Payload along with status code ```200 OK```.

In case it is not found, the server will respond with status code ```404 Not Found```.

---
```DELETE /drop/<id>```

This endpoint is for deleting data. Just like with ```/read/<id>```, the entered ID will correspond to the name of the stored JSON file.

If the file to delete is found, the server will do so and respond with status code ```200 OK```.

If it's not found, nothing will be deleted and the server will respond with status code ```404 Not Found```.
