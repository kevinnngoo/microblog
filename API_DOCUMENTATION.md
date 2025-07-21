# Microblog API Documentation

## Overview
This is the RESTful API for the Microblog application, implementing Chapter 23 of the Flask Mega-Tutorial. The API provides endpoints for user management with token-based authentication.

## Base URL
```
http://localhost:5000/api
```

## Authentication

### Getting a Token
Before accessing protected endpoints, you need to obtain a token:

```bash
http --auth <username>:<password> POST http://localhost:5000/api/tokens
```

Example:
```bash
http --auth alice:dog POST http://localhost:5000/api/tokens
```

Response:
```json
{
    "token": "c6624d30b07eb53f1af2e4348d9e5018"
}
```

### Using the Token
Include the token in the Authorization header for protected endpoints:

```bash
http -A bearer --auth <token> GET http://localhost:5000/api/users
```

### Revoking a Token
```bash
http -A bearer --auth <token> DELETE http://localhost:5000/api/tokens
```

## Endpoints

### User Management

#### Create a New User
- **Method:** POST
- **URL:** `/users`
- **Authentication:** None required
- **Body:** JSON with username, email, password, and optionally about_me

Example:
```bash
http POST http://localhost:5000/api/users username=alice password=dog email=alice@example.com "about_me=Hello, my name is Alice."
```

#### Get a Single User
- **Method:** GET
- **URL:** `/users/<id>`
- **Authentication:** Token required

Example:
```bash
http -A bearer --auth <token> GET http://localhost:5000/api/users/1
```

#### Get All Users
- **Method:** GET
- **URL:** `/users`
- **Authentication:** Token required
- **Query Parameters:** 
  - `page` (optional): Page number (default: 1)
  - `per_page` (optional): Items per page (default: 10, max: 100)

Example:
```bash
http -A bearer --auth <token> GET http://localhost:5000/api/users page==2 per_page==5
```

#### Get User's Followers
- **Method:** GET
- **URL:** `/users/<id>/followers`
- **Authentication:** Token required
- **Query Parameters:** Same as Get All Users

#### Get Users Followed by User
- **Method:** GET
- **URL:** `/users/<id>/following`
- **Authentication:** Token required
- **Query Parameters:** Same as Get All Users

#### Update a User
- **Method:** PUT
- **URL:** `/users/<id>`
- **Authentication:** Token required (can only update own profile)
- **Body:** JSON with fields to update (username, email, about_me)

Example:
```bash
http -A bearer --auth <token> PUT http://localhost:5000/api/users/10 "about_me=Updated bio"
```

## Response Format

### User Resource
```json
{
    "id": 10,
    "username": "alice",
    "last_seen": "2025-07-21T03:22:49.951795+00:00",
    "about_me": "Hello, my name is Alice.",
    "post_count": 0,
    "follower_count": 0,
    "following_count": 0,
    "_links": {
        "self": "/api/users/10",
        "followers": "/api/users/10/followers",
        "following": "/api/users/10/following",
        "avatar": "https://www.gravatar.com/avatar/..."
    }
}
```

### Collection Resource
```json
{
    "items": [
        { /* user objects */ }
    ],
    "_meta": {
        "page": 1,
        "per_page": 10,
        "total_pages": 1,
        "total_items": 10
    },
    "_links": {
        "self": "/api/users?page=1&per_page=10",
        "next": null,
        "prev": null
    }
}
```

### Error Response
```json
{
    "error": "Bad Request",
    "message": "must include username, email and password fields"
}
```

## HTTP Status Codes
- `200` - OK
- `201` - Created (for new user registration)
- `204` - No Content (for token revocation)
- `400` - Bad Request
- `401` - Unauthorized
- `403` - Forbidden
- `404` - Not Found
- `500` - Internal Server Error

## Features Implemented
- ✅ RESTful API design with proper HTTP methods
- ✅ Token-based authentication
- ✅ JSON resource representations with hypermedia links
- ✅ Paginated collections
- ✅ Input validation and error handling
- ✅ Content negotiation for error responses
- ✅ Token expiration and revocation
- ✅ User CRUD operations

## Testing the API

You can test the API using HTTPie (included in the project) or any other HTTP client like curl or Postman.

### HTTPie Examples

1. Create a user:
```bash
http POST localhost:5000/api/users username=testuser password=secret email=test@example.com
```

2. Get a token:
```bash
http --auth testuser:secret POST localhost:5000/api/tokens
```

3. Use the token to access protected resources:
```bash
http -A bearer --auth <your-token> GET localhost:5000/api/users
```

4. Update your profile:
```bash
http -A bearer --auth <your-token> PUT localhost:5000/api/users/<your-id> about_me="New bio"
```

5. Revoke the token:
```bash
http -A bearer --auth <your-token> DELETE localhost:5000/api/tokens
```
