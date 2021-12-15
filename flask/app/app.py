from flask import Flask, session, request, make_response, render_template_string
from secret import secret_key, secret_payload, filter


app = Flask(__name__)
app.config["SECRET_KEY"] = secret_key


@app.route('/', methods=['GET', 'POST'])
def index_handler():
    if request.method == 'POST':
        name = request.form['name']
        if 'admin' in name or name == '':
            return "who are you!"
        else:
            payload = secret_payload
            session['role'] = payload
            return render_template_string("Hello,{{var}}", var=name)
    else:
        rsp = make_response("try to post 'name'")
        rsp.headers['hint'] = "Part of the source in /source"
        return rsp


@app.route('/source')
def source():
    f = open(__file__, 'r')
    rsp = f.read()
    f.close()
    return rsp[rsp.index('source'):]


@app.route('/admin')
def admin_handler():
    try:
        role = session.get('role')
        if not isinstance(role, dict):
            raise Exception
    except Exception:
        return '~~~~~~hacker!'
    if role.get('is_admin') == 1:
        flag = role.get('flag') or 'admin'
        flag = filter(flag)
        message = "%s, I hope you have a good time!your flag is " % flag
        return render_template_string(message)
    else:
        return "I don't know you"


if __name__ == '__main__':
    app.run('0.0.0.0', port=80)

