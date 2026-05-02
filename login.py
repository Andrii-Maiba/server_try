#!/usr/bin/env python3
import cgi
import cgitb
import sqlite3
import bcrypt
import os

cgitb.enable()

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
username = form.getvalue('name')
password = form.getvalue('password')

if username and password:
    conn = sqlite3.connect('login.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
        print("<html><body><h2>Login successful!</h2><a href='/'>Back to home</a></body></html>")
    else:
        print("<html><body><h2>Invalid credentials</h2><a href='/logon.html'>Try again</a></body></html>")
else:
    print("<html><body><h2>Missing fields</h2><a href='/logon.html'>Back</a></body></html>")