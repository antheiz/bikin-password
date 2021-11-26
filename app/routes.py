from app import app
from flask import render_template
# import the necessary modules!
import random
import string

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<int:id>/')
def generate_password(id):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all = lower + upper + num + symbols

    temp = random.sample(all, id)

    password = "".join(temp)

    return render_template('index.html', data=password)



# # input the length of password
# length = int(input("\nEnter the length of password: "))

# # define data
# lower = string.ascii_lowercase
# upper = string.ascii_uppercase
# num = string.digits
# symbols = string.punctuation
# # string.ascii_letters

# # combine the data
# all = lower + upper + num + symbols

# # use random
# temp = random.sample(all, length)

# # create the password
# password = "".join(temp)

# # print the password
# print(password)
