"""Server for lyft mini app"""
 
from flask import Flask, render_template, request, redirect, flash, jsonify

# Create a Flask instance
app = Flask(__name__)

# Define server routes

@app.route("/")
def show_form():
    """Display form"""

    return render_template("form.html")


@app.route("/test", methods=["POST"])
def test():
    """Return a JSON object of a modified string"""

    # Note: The following computation assumes that the user enters a string without any surrounding quotation marks in the form field

    string_to_cut = request.form.get("string_to_cut")

    cut_string = ""

    for i in range(2, len(string_to_cut), 3):
        cut_string += string_to_cut[i]
    
    modified_string = {"return_string": cut_string}
    
    return jsonify(modified_string)







if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0")