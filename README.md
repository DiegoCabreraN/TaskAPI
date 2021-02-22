# TaskAPI

A REST API for Task management

Install the requirements for the project with the following command

```
pip install -r requirements.txt -v
```

---
## Documentation

This api has the following endpoints. In order to make the correct petitions, make sure you follow the instructions.


```signup/```, in order to use this endpoint you have to send `username`, `password` and `email` as a JSON body.


```login/```, in order to access and get your `user_id` you have to use this method, the argumets for the body are `username` and `password`

```tasks/```,  this endpoint has supports 2 methods, `GET` to obtain a certain task, you need the `user_id` in the body, `POST` to create a task you'll need `user_id`, `title` and `description` in the JSON body.

```tasks/<int:id>``` this enpoint supports 3 methods, `GET, PUT, DELETE`:
- For `GET` and `DELETE` you'll need the `user_id` in the body
- For `PUT` you can update `title, description, or status`

