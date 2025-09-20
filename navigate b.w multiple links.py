from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
return render_template('index.html')
@app.route('/about')
def about():
return render_template('about.html')
@app.route('/social')

def social():
return render_template('social.html')
if __name__ == '__main__':
app.run(debug=True)

index.html
<!DOCTYPE html>
<html>
<head>
<title>Home Page</title>
</head>
<body>
<div >
<nav>
<a href="/">Home</a> |
<a href="/about">About</a> |
<a href="/social">Social</a>
</nav>
<h1>Hello...</h1>
<p>This is the Home Page.</p>
</div>
</body>
</html>
About.html
<!DOCTYPE html>
<html>
<head>
<title>About Page</title>
</head>
<body>
<nav>
<a href="/">Home</a> |
<a href="/about">About</a> |
<a href="/social">Social</a>
</nav>
<h1>About Us</h1>
<p>This is the About Page.</p>
</body>
</html>
Social.html

<!DOCTYPE html>
<html>
<head>
<title>links</title>
</head>
<body>
<div class="box">
<nav>
<a href="/">Home</a> |
<a href="/about">About</a> |
<a href="/social">Social</a>
</nav>
<h1>Our Logo:</h1>
<img src="image_path.jpg " target="_blank" >
</div>
</body>
</html>
