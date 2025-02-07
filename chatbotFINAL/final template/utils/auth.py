# Users
users = {
    "user1": "password1",
    "user2": "password2",
    "admin": "admin123"
}

def authenticate_user(username, password):
    return users.get(username) == password
