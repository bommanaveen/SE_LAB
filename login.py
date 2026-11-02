
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "1234":
            return "Login Successful!"
        else:
            return "Invalid Username or Password!"

    return """
    <html>
    <body style="text-align:center; margin-top:100px;">

        <h2>Login Page</h2>

        <form method="POST">
            <input type="text" name="username"
            placeholder="Enter Username" required><br><br>

            <input type="password" name="password"
            placeholder="Enter Password" required><br><br>

            <button type="submit">Login</button>
        </form>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
