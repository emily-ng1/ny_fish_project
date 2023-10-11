from flask import Flask, jsonify, render_template
import psycopg2
from api.models import Fish, WaterQuality
from api.lib.db import build_from_record, build_from_records, find, find_all, get_db
#from settings import DB_NAME, DB_USER,DB_PASSWORD


def create_app(db_name, user, password):
    app=Flask(__name__, template_folder='views')

    app.config.from_mapping(
        DB_NAME=db_name,
        DB_USER=user,
        DB_PASSWORD=password
    )

    @app.route("/")
    def home_page():
        return render_template("index.html")


    #fish
    @app.route("/fishes")
    def fish_index():
        conn=get_db()
        # conn = psycopg2.connect(database=DB_NAME, 
        #                         user=app.config["USER"],
        #                         password=app.config["PASSWORD"])
        objs=find_all(Fish, conn)
        #dicts=[obj.__dict__ for obj in objs]
        add_relations=[obj.to_json(conn) for obj in objs]
        return add_relations

    @app.route("/fishes/<fish_id>")
    def fish_show(fish_id):
        conn = get_db()
        obj=find(Fish, fish_id, conn)
        #dict=obj.__dict__
        add_relation=obj.to_json(conn)
        return add_relation
    

    #waterquality
    @app.route("/waterqualities")
    def waterquality_index():
        conn = get_db()
        objs=find_all(WaterQuality, conn)
        add_relations=[obj.to_json(conn) for obj in objs]
        return add_relations

    @app.route("/waterqualities/<waterquality_id>")
    def waterquality_show(waterquality_id):
        conn = get_db()
        obj=find(WaterQuality, waterquality_id, conn)
        add_relation=obj.to_json(conn)
        return add_relation



    return app

