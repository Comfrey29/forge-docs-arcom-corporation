from flask import Blueprint, render_template, request, jsonify, send_file
from io import BytesIO

main = Blueprint('main', __name__)

@main.route('/')
def editor():
    return render_template('forge/editor.html')

@main.route('/download', methods=['POST'])
def download():
    content = request.form.get('content', "")
    buf = BytesIO()
    buf.write(content.encode('utf-8'))
    buf.seek(0)
    return send_file(
        buf,
        mimetype='text/html',
        as_attachment=True,
        download_name='document.html'
    )
