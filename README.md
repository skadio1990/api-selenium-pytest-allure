- TEST: Send a GET request with a non-existent 'id_' and verify if the server returns a proper error response.
```
➜ curl http://localhost:5555/users
[]
➜ curl http://localhost:5555/users/1
user not found   
```
-----------------
1. BUG: Issue with PUT request, upon update original user remains unchanged.
- TEST: Send a PUT request to update an existing user, and verify that the response contains the updated user data and that the original user in the users list is correctly modified.
```
➜ curl -d '{"name":"Denis", "id":"1"}' -H "Content-Type: application/json" -X POST http://localhost:5555/users
{"id":"1","name":"Denis"}
➜ curl http://localhost:5555/users/1                                                                          
{"id":"1","name":"Denis"}
➜ curl http://localhost:5555/users  
[{"id":"1","name":"Denis"}]
➜ curl -d '{"name":"Igor", "id":"1"}' -H "Content-Type: application/json" -X PUT http://localhost:5555/users/1
{"id":"1","name":"Igor"}
➜ curl http://localhost:5555/users/1                                                                          
{"id":"1","name":"Denis"}
```
-----------------
2. BUG: The create_user method allows the creation of users with missing 'name' or 'id' fields.
- TEST: Send a POST request with JSON data missing the 'name' or 'id' field, and verify if the server returns a proper error response.
```
➜ curl -d '{}' -H "Content-Type: application/json" -X POST http://localhost:5555/users  
{}
➜ curl http://localhost:5555/users 
[{"id":"1","name":"Denis"},{}]
```
-----------------
3. BUG: Lack of validation for duplicated users in the create_user method.
- TEST: Send a POST request with JSON data containing an 'id' that already exists in the users list, and verify if the server returns an appropriate error response.
```
➜ curl -d '{"name":"Igor", "id":"2"}' -H "Content-Type: application/json" -X POST http://localhost:5555/users
{"id":"2","name":"Igor"}
➜ curl -d '{"name":"Igor", "id":"2"}' -H "Content-Type: application/json" -X POST http://localhost:5555/users
{"id":"2","name":"Igor"}
```
-----------------
4. BUG: Lack of input validation in the create_user method.
- TEST: Send a POST request with an invalid 'id_' format, and verify if the server returns an appropriate error response.
```
➜ curl -d '{"name":"Igor2", "id":2}' -H "Content-Type: application/json" -X POST http://localhost:5555/users
{"id":2,"name":"Igor2"}
```
-----------------
5. BUG: In the delete_user method, comparing the 'id' as an integer instead of a string.
- TEST: Send a DELETE request to delete a user with a valid 'id' and verify if the user is correctly removed from the users list.
```
➜ curl http://localhost:5555/users                                                                          
[{"id":"1","name":"Igor"},{"id":2,"name":"Igor2"}]
➜ curl -X DELETE http://localhost:5555/users/1                                                            
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>500 Internal Server Error</title>
<h1>Internal Server Error</h1>
<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>
➜ curl -X DELETE http://localhost:5555/users/2
[{"id":"1","name":"Igor"}]
➜ curl http://localhost:5555/users                                                                          
[{"id":"1","name":"Igor"}]
```



