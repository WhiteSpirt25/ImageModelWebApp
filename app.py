import os
from flask import Flask, request, render_template,url_for
from PIL import Image
from model import MlModel

model = MlModel()


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if request.files:
            print('Taking image!')
            
            image = request.files['pet_image']
            temp_file = os.path.join('static','temp', image.filename)
            
            try:
                os.remove(temp_file)
            except OSError:
                pass

            image.save(temp_file)
            normal_image = Image.open(temp_file)
            score = model.predict(normal_image)

            return render_template('image_score.html',image_score=score,temp_filename = image.filename)
        print('No file')
    return render_template('image_score.html')

@app.route('/reload', methods=['GET','POST'])
def reload_model():
    model=MlModel()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5005)
