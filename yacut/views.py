from flask import flash, redirect, render_template

from . import app, db
from .constants import CUSTOMISED_SHORT_LINK_LENGTH, get_unique_short_id
from .forms import URLForm
from .models import URLMap


@app.route("/", methods=["POST", "GET"])
def main_page():
    form = URLForm()
    if form.validate_on_submit():
        custom_link = form.custom_id.data
        if not custom_link:
            custom_link = get_unique_short_id()
        elif URLMap.query.filter_by(short=custom_link).first():
            form.custom_id.errors = [f'Имя {custom_link} уже занято!']
            return render_template('index.html', form=form)
        if len(custom_link) > CUSTOMISED_SHORT_LINK_LENGTH:
            form.custom_id.errors = [f'Короткая ссылка {custom_link} слишком длинная!']
            return render_template('index.html', form=form)
        new_short_url = URLMap(
            original=form.original_link.data,
            short=custom_link,
        )
        db.session.add(new_short_url)
        db.session.commit()
        flash(f'Новая ссылка:<a href="http://localhost/{new_short_url.short}">'
              f'http://localhost/{new_short_url.short}')
    return render_template('index.html', form=form)


@app.route('/<string:short>', methods=['GET'])
def redirect_to_original_link(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original)
