#!/usr/bin/py3
python
from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'kido3871@gmail.com'
app.config['MAIL_PASSWORD'] = 'hidden'

mail = Mail(app)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    Handles the contact form submission.
    """
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        send_email(name, email, message)

    return render_template('portfolio.html')

@app.route('/')
def portfolio():
    """
    Renders the portfolio.html template.
    """
    return render_template('portfolio.html')

def send_email(name, email, message):
    """
    Sends an email with the submitted contact form information.
    """
    msg = Message('New Contact Form Submission',
                  sender='kido3871@gmail.com',
                  recipients=['kido3871@gmail.com'])
    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    mail.send(msg)

if __name__ == "__main__":
    app.run(debug=True)
