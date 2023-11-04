import random
import pymysql
from app import app
from db import mysql
from flask import jsonify
from flask import Flask, request
import threading
from concurrent.futures import ThreadPoolExecutor
import time


users = []
user_limit = 3

executor = ThreadPoolExecutor(max_workers=10)

@app.route('/test', methods=['POST'])
def add_user():
    global users
    if len(users) >= 3:
        return "User limit reached. Cannot add more users.", 400
    time.sleep(0.01)
    account_num = len(users)
    login_num = random.randint(1111, 9999)
    account_name = "account: " + str(account_num) + "| Login Pin: " + str(login_num)

    user_name = request.form.get('username')

    Account_full = user_name + " | " + account_name

    if user_name is not None:
        users.append(Account_full)
        return f"User '{user_name}' added successfully."

    return "User name not provided.", 400


@app.route('/test1', methods=['GET'])
def list_users():
    return jsonify(users)

@app.route('/logout', methods = ['GET'])
def rm_users():
    global users
    users = []
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')