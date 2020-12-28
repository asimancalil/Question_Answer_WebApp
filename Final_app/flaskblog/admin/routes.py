from flaskblog import app
from flask import render_template, request, url_for


@app.route("admin/")
def admin_index():
    return render_template()
