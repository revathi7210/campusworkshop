"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq1ipmbg5e4khq43b0-a.oregon-postgres.render.com",
        database="betsolworkshop",
        user="betsolworkshop_user",
        password="2JcnQf2mjpT8PQYM4e2CTWpmguKhLqNS")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
