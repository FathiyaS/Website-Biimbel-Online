from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask (__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bimble_sma'
mysql= MySQL (app)

@app.route('/', methods = ['GET','POST'])
def dashboard ():
	return render_template('index.html')


@app.route('/data_pelajar/tambah', methods = ['GET','POST'])
def form():
    if request.method== "POST":
        details = request.form
        Nama = details ['Nama']
        Username = details['Username']
        Email = details['Email']
        Password = details['Password']
        JenisKelamin = details['JenisKelamin']
        Agama = details ['Agama']
        TanggalLahir = details['TanggalLahir']
        Kelas = details['Kelas']
        KelasBimbel = details ['KelasBimbel']
        Metode = details ['Metode']
        Alamat = details ['Alamat']
        Nohp = details ['Nohp']	
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO data_pelajar (Nama, Username, Email, Password, JenisKelamin, Agama, TanggalLahir , Kelas, KelasBimbel, Metode, Alamat, Nohp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (Nama, Username, Email, Password, JenisKelamin, Agama, TanggalLahir, Kelas, KelasBimbel, Metode, Alamat, Nohp))
        mysql.connection.commit()
        cur.close()
        return render_template('index2.html')
    return render_template('index1.html')
	
	


if (__name__) == ('__main__'):
    app.run(debug = True)
