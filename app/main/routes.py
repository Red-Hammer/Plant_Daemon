from flask import render_template
from app.main import bp
from app import db
from utils import plant_getter as pg


@bp.route('/')
@bp.route('/home')
def home():
    context = pg('shaggy')
    return render_template(
        'home.html',
        title='Home',
        **context
    )