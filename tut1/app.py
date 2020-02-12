try:
    import os
    from flask import Flask

    from flask import Flask, request, \
        render_template, redirect, url_for, \
        session, send_file

    from flask import (Flask,
                       request,
                       redirect,
                       session)

except Exception as e:
    print("Some Modules are Missing {}".format(e))

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"


@app.route('/',  methods=["GET", "POST"])
def index():

    return render_template('Home.html')


if __name__ == '__main__':
    app.run(debug=True)
