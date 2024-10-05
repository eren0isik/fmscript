from . import auth_bp
from flask import Blueprint, render_template, request, redirect, url_for, flash
import json
from .fmdb.FMDB import *

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    user_db = JSONDatabase('users')  # Initialize here
    if request.method == 'POST':
        # Formdan gelen verileri al
        username = request.form['username']
        password = request.form['password']

        # JSON dosyasını açıp kullanıcıları kontrol et
        users = user_db.get_users()

        # Kullanıcı adı ve şifreyi doğrula
        if username in users and users[username] == password:
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username or password')  # Hata mesajı
            return render_template('auth/login.html', error="Invalid credentials")
    
    return render_template('auth/login.html')
