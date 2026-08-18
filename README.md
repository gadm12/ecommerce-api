# E-Commerce REST API

A backend E-Commerce REST API built with **Django, Django REST Framework, and PostgreSQL**.

The API provides user authentication, product browsing, category filtering, and shopping cart management. It uses token-based authentication to protect user-specific functionality and provides RESTful endpoints for interacting with products and cart data.

## Preview

![E-Commerce API Preview](assets/ecommerce-api.png)

## Features

- User signup
- User login and logout
- Token authentication
- Retrieve authenticated user information
- View all store items
- View individual items
- Filter items by category
- Add items to a shopping cart
- View cart contents
- Calculate cart total
- Increase item quantity
- Decrease item quantity
- Automatically remove items when quantity reaches zero
- Remove items from the cart
- PostgreSQL database
- Automated Django tests

## Technologies

- Python
- Django
- Django REST Framework
- PostgreSQL
- Token Authentication
- Docker
- REST APIs
- Django Test Framework

## API Endpoints

### Authentication

| Method | Endpoint                | Description                                         |
| ------ | ----------------------- | --------------------------------------------------- |
| POST   | `/api/v1/users/signup/` | Create a new client, cart, and authentication token |
| POST   | `/api/v1/users/login/`  | Log in and retrieve/create an authentication token  |
| POST   | `/api/v1/users/logout/` | Log out and delete the authentication token         |
| GET    | `/api/v1/users/info/`   | Retrieve authenticated client information           |

### Items

| Method | Endpoint                             | Description                                    |
| ------ | ------------------------------------ | ---------------------------------------------- |
| GET    | `/api/v1/items/`                     | View all items                                 |
| GET    | `/api/v1/items/<item_id>/`           | View an individual item                        |
| POST   | `/api/v1/items/<item_id>/`           | Add an item to the authenticated client's cart |
| GET    | `/api/v1/items/category/<category>/` | Filter items by category                       |

### Cart

| Method    | Endpoint                                                 | Description                        |
| --------- | -------------------------------------------------------- | ---------------------------------- |
| GET       | `/api/v1/cart/`                                          | View cart items and total price    |
| PUT/PATCH | `/api/v1/cart/method/<method>/cart_item/<cart_item_id>/` | Increase or decrease item quantity |
| DELETE    | `/api/v1/cart/<cart_item_id>/`                           | Remove an item from the cart       |

The cart quantity endpoint accepts:

```text
add
sub
```
