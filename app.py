from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template('about.html', name='ali')


@app.route('/posts/<post_name>')
def posts(post_name):
    all_posts = ['make-site-with-python', 'how-to-make-cake', 'all-os-can-show-gui', 'captain-code-coding']
    if post_name == all_posts[3]: # captain code coding
        return redirect(url_for('about'))
    elif post_name in all_posts:
        post_name = post_name.replace("-", " ")
        return render_template("posts.html", name=post_name, content=f"This is content of <b>{post_name}</b> post")
    else:
        return "Post Not Found!"


app.run('localhost', 80, debug=True)
