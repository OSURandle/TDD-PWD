def check_pwd(pwd):
    if len(pwd) < 8 or len(pwd) > 20:
        return False

    if pwd.isdigit():
        return False

    if pwd.islower():
        return False

    return True
