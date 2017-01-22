Flask for Fun and Profit
------------------------

Based on the PyBay 2016 talk by Armin Ronacher.
Here are the [slides](https://speakerdeck.com/player/94a53afb6a524ad88f301f62166a27e4?#).
Here is the [talk](https://youtu.be/1ByQhAM5c1I). 

Run with a virtualenv:

    pip install -e .
    export FLASK_APP=myapp._devapp
    export FLASK_DEBUG=1
    flask run

API behavior (using httpie):

    http ":5000/add?a=1&b=2"
    http POST :5000/subtract a:=1 b:=24123

Highlights:

- Custom Voluptuous decorator for data validation

Coming soon:

- add pagination example
- add in flask-sqla
    + context for improved security example
- testing