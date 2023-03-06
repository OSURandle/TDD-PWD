def check_pwd(pwd):
    symbols = "~`!@#$%^&()_+-="
    if len(pwd) < 8 or len(pwd) > 20:
        return False

# Citation for the following function:
# Date: 03/05/2023
# Copied from /OR/ Adapted from /OR/ Based on:
# https://canvas.oregonstate.edu/courses/1901830/pages/exploration-random-testing?module_item_id=22851350
    if not any(char.isdigit() for char in pwd):
        return False

# Citation for the following function:
# Date: 03/06/2023
# Copied from /OR/ Adapted from /OR/ Based on:
# https://canvas.oregonstate.edu/courses/1901830/pages/exploration-random-testing?module_item_id=22851350
    if not any(char.islower() for char in pwd):
        return False

# Citation for the following function:
# Date: 03/06/2023
# Copied from /OR/ Adapted from /OR/ Based on:
# https://canvas.oregonstate.edu/courses/1901830/pages/exploration-random-testing?module_item_id=22851350
    if not any(char.isupper() for char in pwd):
        return False

# Citation for the following function:
# Date: 03/05/2023
# Copied from /OR/ Adapted from /OR/ Based on:
# https://canvas.oregonstate.edu/courses/1901830/pages/exploration-random-testing?module_item_id=22851350

    if not any(char in symbols for char in pwd):
        return False

    return True
