from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

bookings = []
booking_counter = 1


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/book")
def book_page():
    source = request.args.get("from")
    destination = request.args.get("to")
    date = request.args.get("date")

    return render_template(
        "book.html",
        source=source,
        destination=destination,
        date=date
    )


@app.route("/book", methods=["POST"])
def confirm_booking():
    global booking_counter

    name = request.form["name"]
    source = request.form["source"]
    destination = request.form["destination"]
    date = request.form["date"]
    seats = request.form["seats"]
    amount = request.form["amount"]
    bus = request.form["bus"]
    time = request.form["time"]

    booking = {
        "id": booking_counter,
        "name": name,
        "source": source,
        "destination": destination,
        "date": date,
        "seats": seats,
        "amount": amount,
        "bus": bus,
        "time": time
    }

    bookings.append(booking)
    booking_counter += 1

    return redirect(url_for("show_bookings"))


@app.route("/bookings")
def show_bookings():
    return render_template("bookings.html", bookings=bookings)


# ✅ IMPORTANT FIX FOR DEPLOYMENT
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))   # dynamic port
    app.run(host="0.0.0.0", port=port)
