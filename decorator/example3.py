def require_loggin(func):
    def wrapper(user, *args, **kwargs):
        if not user["is_logged_in"]:
            return "Access Denied User Can not Get profile Because it is not authentic"
        return "Authentic " + func(user)
    return wrapper


@require_loggin

def view_profile(user):
    return f"User {user["user_name"]} Your Profile is here !!!"

user1 = {"user_name":"Nuredin", "is_logged_in": True}
user2 = {"user_name":"Hafiz", "is_logged_in": False}

print(view_profile(user2))