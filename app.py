from flask import Flask, render_template, request, redirect, url_for
from functions import Functions

app = Flask(__name__)
functions = Functions()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_user', methods=['POST'])
def set_user():
    name = request.form['name']
    occupation = request.form['occupation']
    image = request.files['image']
    image_path = 'user_data/user_image.jpg'
    image.save(image_path)
    return functions.display_user(name, occupation, image_path)

@app.route('/cats', methods=['POST'])
def set_cat():
    cat_name = request.form['cat_name']
    cat_data = functions.get_cat_data(cat_name)
    return cat_data

@app.route('/view_cat_image/<cat>', methods=['GET'])
def view_cat_image(cat):
    return functions.view_cat_image(cat)

@app.route('/mirror_image/<cat>', methods=['GET'])
def mirror_image(cat):
    return functions.mirror_image(cat)

@app.route('/threshold_image/<cat>', methods=['GET'])
def threshold_image(cat):
    return functions.threshold_image(cat)

@app.route('/play_sound/<cat>', methods=['GET'])
def play_sound(cat):
    return functions.play_sound(cat)

@app.route('/reverse_sound/<cat>', methods=['GET'])
def reverse_sound(cat):
    return functions.reverse_sound(cat)

@app.route('/view_video', methods=['GET'])
def view_video():
    return functions.view_video()

@app.route('/clip_video', methods=['GET'])
def clip_video():
    return functions.clip_video()

if __name__ == '__main__':
    app.run(debug=True)
