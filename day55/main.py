# from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def hello_world():
#    return '<h1 style="text-align:center">HELLO</h1>'\
#     '<p>world<p>'


# @app.route("/bye")
# @make_bold
# def say_bye():
#     return '<em><b>"Bye</b></em>"'
# @app.route("/username/<name>/<number>")
# def greet(name):
#     return f"hello there {name} you are {number} "


# if __name__ == "__main__":
#     app.run(debug=True)


# class user:
#     def __init__(self,name):
#         self.name=name
#         self.is_logged_in=False
# def is_auth_dec(function):
#     def wrapper(*args,**kwargs):
#         if args[0].is_logged_in==True:
#           function(args[0])
#     return wrapper

# @is_auth_dec
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post")
# new_user=user("thiru")
# new_user.is_logged_in=True
# create_blog_post(new_user)




from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)




















