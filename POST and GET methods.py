from flask import Flask, render_template,request
app = Flask(__name__)
@app.route('/contact')
def contact():
return render_template('contacts.html')
# Route to handle form submission
@app.route('/submit', methods=['POST', 'GET'])
def submit():
if request.method == 'POST':
name = request.form['username']
msg = request.form['message']

else:
name = request.args.get('username')
msg = request.args.get('message')
return f"<h2>Thanks, {name}!</h2><p>Your message: {msg}</p>"
if __name__ == '__main__':
app.run(debug=True)
contacts.html
<!DOCTYPE html>
<html>
<head>
<title>Contact Page</title>
</head>
<body>
<h1>Contact Us</h1>
<!-- <form action="/submit" method="GET"> -->
<form action="/submit" method="POST">
<label>Name:</label>
<input type="text" name="username"><br><br>
<label>Message:</label>
<input type="text" name="message"><br><br>
<button type="submit">Send</button>
</form>
</body>
</html>
