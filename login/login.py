from tkinter import *
from .login_checks import *

current_user_field = ''
current_password_field = ''

"""
Main login windows with tkinter
Username input
Password input
Account creation
"""


# opens window with fields to create new user
def create_user(username):
    def get_new_user_fields():
        new_password = password_field.get()
        new_dob = dob_field.get()
        new_artist = fave_artist_field.get()
        new_genre = fave_genre_field.get()

        valid_password = validate_password(new_password)
        valid_dob = validate_dob(new_dob)

        valid_new_account = False
        if valid_password and valid_dob:
            valid_new_account = True

        else:
            if not valid_password:
                error_label.config(text='Password must contain: Uppercase, lowercase and number')
            if not valid_dob:
                error_label.config(text='Invalid DOB. Check format.')

        if valid_new_account:
            with openSQL() as sql:
                sql.execute("INSERT INTO user VALUES(?, ?, ?, ?, ?, '{}')", (username, new_password, new_dob, new_artist, new_genre))
            create_account.destroy()

    def return_to_login():
        create_account.destroy()
        login()

    create_account = Tk()
    create_account.config(bg='blue')
    create_account.title('Create Account')

    password_label = Label(text='Password', bg='blue', fg='white')
    password_field = Entry(show='*', width=40)

    dob_label = Label(text='DOB (dd.mm.yyyy)', bg='blue', fg='white')
    dob_field = Entry(width=40)

    fave_artist_label = Label(text='Favourite Artist', bg='blue', fg='white')
    fave_artist_field = Entry(width=40)

    fave_genre_label = Label(text='Favourite Genre', bg='blue', fg='white')
    fave_genre_field = Entry(width=40)

    password_label.grid(column=1, row=1)
    password_field.grid(column=2, row=1)

    dob_label.grid(column=1, row=2)
    dob_field.grid(column=2, row=2)

    fave_artist_label.grid(column=1, row=3)
    fave_artist_field.grid(column=2, row=3)

    fave_genre_label.grid(column=1, row=4)
    fave_genre_field.grid(column=2, row=4)

    submit_button = Button(text='Enter', command=get_new_user_fields)
    submit_button.grid(row=5, column=2)

    quit_button = Button(text='Return to Login', command=return_to_login)
    quit_button.grid(row=6, column=2)

    error_label = Label(text='', fg='red')
    error_label.grid(row=7, column=2)

    create_account.mainloop()


def login():
    # gets username field
    def get_fields():
        global current_user_field
        username = username_box.get()
        if username != '' and username != ' ':
            current_user_field = username
            login_window.destroy()

    # gets password field
    def get_password_field():
        global current_password_existing
        current_password_existing = password_field.get()
        password_input.destroy()

    def return_to_login():
        global returned_to_login
        returned_to_login = True
        password_input.destroy()
        login()


    # main window, inputs username
    login_window = Tk()
    login_window.config(bg='blue')
    login_window.title('Login')

    username_button_frame = Frame()
    username_button_frame.grid(column=2, row=2)

    username_field = Label(text='Username', bg='blue', fg='white')
    username_box = Entry(width=50)
    submit_button = Button(username_button_frame, text='Enter', command=get_fields)
    exit_button = Button(username_button_frame, text='Quit', bg='red', command=exit)

    username_field.grid(column=1, row=1)
    username_box.grid(column=2, row=1)

    submit_button.pack(side='left')
    exit_button.pack(side='left')

    login_window.mainloop()

    # check if the username exists
    global current_user_field
    user_exists = check_user(current_user_field)

    if not user_exists:
        print('User not found, create new')
        # runs create new user form
        create_user(current_user_field)
        return current_user_field

    print('Username Found')
    while True:
        returned_to_login = False

        # runs enter password form
        password_input = Tk()
        password_input.config(bg='blue')
        password_input.title('Verify Password')

        password_label = Label(text='Password', bg='blue', fg='white')
        password_field = Entry(show='*')
        password_submit_button = Button(text='Submit', command=get_password_field, width=30)
        password_login_button = Button(text='Return to login', command=return_to_login, width=30)

        password_label.grid(row=1, column=1)
        password_field.grid(row=1, column=2)
        password_submit_button.grid(row=2, column=2)
        password_login_button.grid(row=3, column=2)

        password_input.mainloop()

        if not returned_to_login:
            try:
                if current_password_existing == check_user_password(current_user_field):
                    return current_user_field
            except NameError:
                pass
            else:
                print('Password Incorrect')
