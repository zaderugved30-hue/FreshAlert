from flask import Flask, render_template, request, redirect, url_for, session
from datetime import date
import mysql.connector

app = Flask(__name__)
app.secret_key = "freshalert123"


def db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="MySQL@2026ABC",
        database="food_tracker_db"
    )


def query(sql, values=(), one=False):
    con = db()
    cur = con.cursor(dictionary=True)
    cur.execute(sql, values)
    data = cur.fetchone() if one else cur.fetchall()
    cur.close()
    con.close()
    return data


def change(sql, values=()):
    con = db()
    cur = con.cursor()
    cur.execute(sql, values)
    con.commit()
    cur.close()
    con.close()


def status(expiry):
    days = (expiry - date.today()).days

    if days < 0:
        return "Expired", "status-red"

    if days < 10:
        return f"{days} days left", "status-yellow"

    return "Safe", "status-green"


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    message = ""

    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        password = request.form["password"]

        if password != request.form["confirm_password"]:
            message = "Passwords do not match"

        elif query(
            "SELECT user_id FROM users WHERE username=%s",
            (username,), True
        ):
            message = "Username already exists"

        else:
            change(
                """INSERT INTO users(name,username,password,role)
                VALUES(%s,%s,%s,'U')""",
                (name, username, password)
            )
            return redirect(url_for("login"))

    return render_template("register.html", message=message)


@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        user = query(
            """SELECT * FROM users
            WHERE username=%s AND password=%s""",
            (
                request.form["username"],
                request.form["password"]
            ),
            True
        )

        if user:
            session["user_id"] = user["user_id"]
            session["username"] = user["username"]
            session["name"] = user["name"] or user["username"]
            session["role"] = user["role"]

            return redirect(url_for("dashboard"))

        message = "Invalid username or password"

    return render_template("login.html", message=message)


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))

    data = query(
        """SELECT
        COUNT(*) total,
        SUM(expiry_date < CURDATE()) expired,
        SUM(expiry_date >= CURDATE()
        AND expiry_date < DATE_ADD(CURDATE(),INTERVAL 10 DAY)) soon,
        SUM(expiry_date >= DATE_ADD(CURDATE(),INTERVAL 10 DAY)) safe
        FROM food_items""",
        one=True
    )

    upcoming = query(
        """SELECT * FROM food_items
        WHERE expiry_date >= CURDATE()
        ORDER BY expiry_date LIMIT 5"""
    )

    for food in upcoming:
        food["status"], food["status_class"] = status(food["expiry_date"])

    return render_template(
        "dashboard.html",
        total=data["total"],
        expired=data["expired"] or 0,
        soon=data["soon"] or 0,
        safe=data["safe"] or 0,
        upcoming_foods=upcoming,
        current_date=date.today()
    )


@app.route("/foods")
def foods():
    if "user_id" not in session:
        return redirect(url_for("login"))

    search = request.args.get("search", "")

    if search:
        food_list = query(
            """SELECT * FROM food_items
            WHERE food_name LIKE %s OR category LIKE %s
            ORDER BY expiry_date""",
            (f"%{search}%", f"%{search}%")
        )
    else:
        food_list = query(
            "SELECT * FROM food_items ORDER BY expiry_date"
        )

    for food in food_list:
        food["status"], food["status_class"] = status(food["expiry_date"])

    return render_template(
        "foods.html",
        foods=food_list,
        search=search,
        current_date=date.today()
    )


@app.route("/add", methods=["GET", "POST"])
def add_food():
    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        change(
            """INSERT INTO food_items
            (food_name,category,quantity,unit,
            purchase_date,expiry_date,supplier_id)
            VALUES(%s,%s,%s,%s,%s,%s,%s)""",
            (
                request.form["food_name"],
                request.form["category"],
                request.form["quantity"],
                request.form["unit"],
                request.form["purchase_date"],
                request.form["expiry_date"],
                request.form.get("supplier_id") or None
            )
        )

        return redirect(url_for("foods"))

    suppliers = query(
        "SELECT * FROM suppliers ORDER BY supplier_name"
    )

    return render_template(
        "add_food.html",
        suppliers=suppliers
    )


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_food(id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        change(
            """UPDATE food_items SET
            food_name=%s, category=%s, quantity=%s,
            unit=%s, purchase_date=%s, expiry_date=%s,
            supplier_id=%s WHERE food_id=%s""",
            (
                request.form["food_name"],
                request.form["category"],
                request.form["quantity"],
                request.form["unit"],
                request.form["purchase_date"],
                request.form["expiry_date"],
                request.form.get("supplier_id") or None,
                id
            )
        )

        return redirect(url_for("foods"))

    food = query(
        "SELECT * FROM food_items WHERE food_id=%s",
        (id,), True
    )

    suppliers = query(
        "SELECT * FROM suppliers ORDER BY supplier_name"
    )

    return render_template(
        "edit_food.html",
        food=food,
        suppliers=suppliers
    )


@app.route("/delete/<int:id>")
def delete_food(id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    change(
        "DELETE FROM food_items WHERE food_id=%s",
        (id,)
    )

    return redirect(url_for("foods"))


@app.route("/suppliers")
def suppliers():
    if "user_id" not in session:
        return redirect(url_for("login"))

    data = query(
        "SELECT * FROM suppliers ORDER BY supplier_name"
    )

    return render_template(
        "suppliers.html",
        suppliers=data
    )


@app.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect(url_for("login"))

    user = query(
        "SELECT * FROM users WHERE user_id=%s",
        (session["user_id"],),
        True
    )

    user["name"] = user["name"] or user["username"]

    return render_template(
        "profile.html",
        user=user
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)