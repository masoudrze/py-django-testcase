def validate_password(password):
    if not password:
        return False

    if len(password) < 8:
        return False

    return True