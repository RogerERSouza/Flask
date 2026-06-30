from flask import render_template, Blueprint
from models import filme, ingresso, sala, sessao

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def index():
    return render_template("index.html")