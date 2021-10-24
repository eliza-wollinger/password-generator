from flask import *
import random as rd
import string as st

special_characters = '!@#$%&*()-=+_.?'
characters_lower = st.ascii_lowercase
characters_upper = st.ascii_uppercase

randomize = rd.SystemRandom()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello World</h1>"

@app.route("/getPass", methods=['POST', 'GET'])
def get_pass():
    # print(request.form["specialChars"])
    password = gen_password(request.form)
    return password

def gen_password(options):
    has_special_chars = options["specialChars"]
    has_capital_letters = options["capitalLetters"]
    has_numbers = options["numbers"]
    size = options["size"]

    structure = characters_lower

    if(has_special_chars == "true"):
        structure += special_characters
    if(has_capital_letters == "true"):
        structure += characters_upper
    if(has_numbers == "true"):
        structure += st.digits
    
    result = ''.join(randomize.choice(structure) for i in range(int(size)))

    return result