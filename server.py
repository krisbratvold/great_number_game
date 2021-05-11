from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
import random

@app.route('/')
def index():
    if 'rand_num' not in session:
        session['rand_num'] = random.randint(1, 100)
    if 'number' not in session:
            return render_template ('index.html')
    elif int(session['number']) > int(session['rand_num']):
        return render_template ('index.html', sentence = 'Too High!', rand_num = session['rand_num'], num = session['number'])
    elif int(session['number']) < int(session['rand_num']):
        return render_template ('index.html', sentence = 'Too Low!', rand_num = session['rand_num'], num = session['number'] )
    elif int(session['number']) == int(session['rand_num']):
        return render_template ('index.html', sentence = f"The number was {session['rand_num']}", rand_num = session['rand_num'], num = session['number'])

@app.route('/guess',methods=['POST'])
def determine_guess():
    session['number'] = request.form['number']
    return redirect('/')

@app.route('/restart')
def clear():
    session.clear()
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)