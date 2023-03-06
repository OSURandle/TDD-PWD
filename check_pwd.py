def check_pwd(pwd):
    symbols = "~`!@#$%^&()_+-="
    if len(pwd) < 8 or len(pwd) > 20:
        return False

    if pwd.isdigit():
        return False

    if pwd.islower():
        return False

    if pwd.isupper():
        return False

    if not any(char in symbols for char in pwd):
        return False

    return True
