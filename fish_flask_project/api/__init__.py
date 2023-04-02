from flask import Flask, jsonify, render_template
import psycopg2
#from fish_flask_project.settings import DB_NAME, DB_USER, DB_PASSWORD



def create_app(db_name, user, password):
    app=Flask(__name__, template_folder='views')

    app.config.from_mapping(
        DATABASE_NAME=db_name,
        USER=user,
        PASSWORD=password
    )

    @app.route("/")
    def home_page():
        return render_template("index.html")

    @app.route("/fishes")
    def fish_index():
        conn=psycopg2.connect(database=app.config["DATABASE_NAME"], user=app.config["USER"], password=app.config["PASSWORD"])
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM ny_fishes WHERE year=2021;")
        tuples=cursor.fetchall()
        return jsonify(tuples)

    @app.route("/fishes/<fish_id>")
    def fish_show(fish_id):
        pass

    return app

#app.run(debug=True).