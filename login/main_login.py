from .login_checks import create_db
from .login import login


"""
Creates a database and initiates login. Returns the username logged in.
"""
def main_login():
    create_db()
    username = login()
    return username
