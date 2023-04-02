from flask import Flask, jsonify, render_template
import psycopg2
from api.models import Fish
from api.lib.db import build_from_record, build_from_records


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
        fish_records=cursor.fetchall()
        fish_objs=build_from_records(Fish, fish_records)
        fish_dicts=[fish_obj.__dict__ for fish_obj in fish_objs]
        return jsonify(fish_dicts)

    @app.route("/fishes/<fish_id>")
    def fish_show(fish_id):
        pass

    return app

