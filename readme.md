# **Luna Lam's String Cuttery**
A simple web application by [Luna Lam](https://github.com/lunaxlam)

## **Table of Contents**

* [Summary](https://github.com/lunaxlam/luna-lam-lyft-mini-app#overview)
* [Tech Stack](https://github.com/lunaxlam/luna-lam-lyft-mini-app#tech-stack) 
* [Installation](https://github.com/lunaxlam/luna-lam-lyft-mini-app#installation)

## **Summary**
*Luna Lam's String Cuttery* enables users to enter a desired string into a form. The form data is sent as a POST request to a specified route, which returns a JSON object with the key "return_string" and a string that contains every third-letter of the original string. 

## **Tech Stack**
Backend: Flask, Python<br />
Frontend: CSS 3, HTML5, Jinja2

## **Installation**

To run *Luna Lam's String Cuttery*: <br />

Clone or fork the [repository](https://github.com/lunaxlam/luna-lam-lyft-mini-app):

```
https://github.com/lunaxlam/luna-lam-lyft-mini-app
```

In the project directory, create and activate a virtual environment:
```
virtualenv env
source env/bin/activate
```

Install the project dependencies:
```
pip3 install -r requirements.txt
```

Create and save a Flask secret key in a file called <kbd>secrets.sh</kbd> in the following format:
```
export FLASK_SECRET_KEY="YOUR_KEY_HERE"
```

Source your Flask secret key:
```
source secrets.sh
```

Run the application:
```
python3 server.py
```

In your web browser, navigate to:
```
localhost:5000/
```
You can now access *Luna Lam's String Cuttery* !

