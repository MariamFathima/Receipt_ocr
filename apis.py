import base64
import fin
def convert_and_save(b64_string):
    with open("image.jpeg", "wb") as fh:
        fh.write(base64.decodebytes(b64_string.encode()))


from flask import Flask,redirect, url_for, request
#import Flask
app = Flask(__name__)


@app.route('/images',methods = ['POST'])
def get_images():
   if request.method == 'POST':
      data = request.json
      print(data)
      image = data['base_64_image_content']
      convert_and_save(image)
      return fin.tess("./image.jpeg")

if __name__ == '__main__':
   app.run(debug = True)