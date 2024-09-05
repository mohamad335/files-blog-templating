from flask import Flask, render_template
from post import Post
import requests
app = Flask(__name__)
import requests 
post_list=[]
response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
if response.status_code == 200:
    try:
        data = response.json()
        for post in data:
             post_list.append(Post(post['id'],post['title'], post['subtitle'], post['body']))
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print("No exception occurred.")

@app.route('/')
def home():
    return render_template("index.html", posts=post_list)
@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for post in post_list:
        if post.id == index:
            requested_post = post
        return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
