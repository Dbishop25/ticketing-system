from flask import Flask, request, redirect
import sqlite3
from database import init_db

app = Flask(__name__)

# Create database if it doesn't exist
init_db()


@app.route("/")
def home():
    return """
    <h1>IT Ticketing System</h1>

    <a href="/create">Create Ticket</a>
    <br><br>

    <a href="/tickets">View Tickets</a>
    """


@app.route("/create", methods=["GET", "POST"])
def create_ticket():

    if request.method == "POST":

        title = request.form["title"]
        description = request.form["description"]

        conn = sqlite3.connect("tickets.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO tickets (title, description) VALUES (?, ?)",
            (title, description)
        )

        conn.commit()
        conn.close()

        return redirect("/tickets")

    return """
    <h2>Create Ticket</h2>

    <form method="POST">

        Title:<br>
        <input type="text" name="title"><br><br>

        Description:<br>
        <textarea name="description"></textarea><br><br>

        <button type="submit">Submit Ticket</button>

    </form>
    """


@app.route("/tickets")
def tickets():

    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tickets")
    rows = cursor.fetchall()

    conn.close()

    html = "<h2>All Tickets</h2>"

    for row in rows:

        html += f"""
        <div style='border:1px solid black; padding:10px; margin:10px;'>

        <b>ID:</b> {row[0]} <br>
        <b>Title:</b> {row[1]} <br>
        <b>Description:</b> {row[2]} <br>
        <b>Status:</b> {row[3]}

        </div>
        """

    html += "<br><a href='/'>Back Home</a>"

    return html


if __name__ == "__main__":
    app.run(debug=True)