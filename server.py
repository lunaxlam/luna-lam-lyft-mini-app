"""Server for mini app for Lyft"""
 
from flask import Flask, render_template, request, redirect, flash, jsonify
from os import environ

# Create a Flask instance
app = Flask(__name__)

# Set secret key to enable use of sessions and flash messages
app.secret_key = environ["FLASK_SECRET_KEY"]

# Define server routes

@app.route("/")
def show_form():
    """Display form"""

    flash("MAY SPECIAL! All string cutting 50% off!")

    return render_template("form.html")


@app.route("/test", methods=["POST"])
def test():
    """Return a JSON object of a modified string"""

    string_to_cut = request.form.get("string_to_cut")

    standard_string = ""

    # Standardize the form input in case user wraps string in quotes
    for char in string_to_cut:
        if char != '"' and char != "'":
            standard_string += char

    cut_string = ""

    for i in range(2, len(standard_string), 3):
        cut_string += standard_string[i]
    
    modified_string = {"return_string": cut_string}
    
    return jsonify(modified_string)




if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0")