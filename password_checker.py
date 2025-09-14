def strong_password(password):
    """This function checks if the password is strong or not."""
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    special_characters = "!@#$%^&*()-+?_=,<>/"
    if not any(char in special_characters for char in password):
        return False
    return True
