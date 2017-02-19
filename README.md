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

Interaction with the API using httpie (`pip install httpie`):

    http ":5000/v1.0/sum?a=1&b=2"
    http :5000/v1.0/difference a:=1 b:=2

Coming soon:

- add pagination example
- add in flask-sqla
    + context for improved security example
- testing