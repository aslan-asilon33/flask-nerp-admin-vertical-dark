from flask import Flask, render_template
import os
from dotenv import load_dotenv

# Memuat variabel dari file .env
load_dotenv()

app = Flask(__name__)

# Konfigurasi Flask dari variabel .env
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DEBUG'] = os.getenv('DEBUG') == 'True'  # Mengkonversi string ke boolean

# Route untuk halaman utama
@app.route('/')
def home():
    return render_template('analytics.html')

if __name__ == '__main__':
    app.run()
