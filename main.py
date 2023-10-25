from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = '<your-email@gmail.com>'
app.config['MAIL_PASSWORD'] = '<your app password>'
mail = Mail(app)


@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        msg = Message("Hey", sender='noreply@demo.com',
                      recipients=['recipient@email.com'])
        msg.body = "Hey! Check out this cool email!"
        mail.send(msg)
        return "Sent email."
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
