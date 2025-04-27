from flask import Flask, render_template
import pymysql

app = Flask(__name__)

connection = pymysql.connect(
    host='dbecom.cnsc6gsk4w0n.ap-southeast-2.rds.amazonaws.com',
    user='admin',
    password='uts123321!',
    database='ecommerce_db',
    cursorclass=pymysql.cursors.DictCursor  # ini penting supaya hasilnya dict, bukan tuple
)

@app.route('/')
def show_products():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM produk")
        products = cursor.fetchall()

    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
