from flask import Flask, request, render_template, redirect, url_for, send_file, make_response
from io import BytesIO
import boto3
from cryptography.fernet import Fernet


app = Flask(__name__)
s3 = boto3.client('s3')

BUCKET_NAME = 'bucket2114092'  


ENCRYPTION_KEY = Fernet.generate_key()  
cipher_suite = Fernet(ENCRYPTION_KEY)


@app.route('/')
def index():
    return render_template('upload.html')  


@app.route('/upload', methods=['POST'])
def upload_image():
    
    if 'image' not in request.files:
        return "No file part in the request"

    file = request.files['image']
    
    
    if file.filename == '':
        return "No selected file"

    
    encrypt = request.form.get('encrypt', 'off') == 'on'

    
    file_data = file.read()

    
    if encrypt:
        file_data = cipher_suite.encrypt(file_data)
        file_name = 'encrypted_' + file.filename
    else:
        file_name = file.filename

    
    s3.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=file_data)

    return "Image uploaded successfully!"


@app.route('/images')
def list_images():
    
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    
    images = [item['Key'] for item in response.get('Contents', [])]

    
    filter_encrypted = request.args.get('filter_encrypted', 'off') == 'on'

    if filter_encrypted:
        images = [img for img in images if img.startswith('encrypted_')]

    return render_template('images.html', images=images)



@app.route('/download/<filename>')
def download_image(filename):
    try:
        obj = s3.get_object(Bucket=BUCKET_NAME, Key=filename)
        file_data = obj['Body'].read()

        if filename.startswith('encrypted_'):
            file_data = cipher_suite.decrypt(file_data)

        file_stream = BytesIO(file_data)
        response = make_response(send_file(file_stream, as_attachment=True, download_name=filename))
        return response
    except Exception as e:
        return f"Error downloading file: {str(e)}"

if __name__ == "_main_":
    app.run(debug=True, host='0.0.0.0', port=5000)
 
