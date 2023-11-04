import random
import pymysql
from app import app
from db import mysql
from flask import jsonify
from flask import Flask, request
import threading
from concurrent.futures import ThreadPoolExecutor
import time

###############################################################################################

users = []

@app.route('/test', methods=['POST'])
def add_user():
    executor = ThreadPoolExecutor(max_workers=10)
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

########################################################################################

users_fast = []

@app.route('/test_fast', methods=['POST'])
def add_user_fast():
    global users_fast
    if len(users_fast) >= 3:
        return "User limit reached. Cannot add more users.", 400
    account_num = len(users_fast)
    login_num = random.randint(1111, 9999)
    account_name = "account: " + str(account_num) + "| Login Pin: " + str(login_num)

    user_name = request.form.get('username')

    Account_full = user_name + " | " + account_name

    if user_name is not None:
        users_fast.append(Account_full)
        return f"User '{user_name}' added successfully."

    return "User name not provided.", 400

####################################################################################3

users_fixed = []

@app.route('/test_fixed', methods=['POST'])
def add_user_fixed():
    global users_fixed

    lock = threading.Lock()
    user_name = request.form.get('username')
    if user_name is not None:
        with lock:
            if len(users_fixed) <= 2:
                account_num = len(users_fixed)
                login_num = random.randint(1111, 9999)
                account_name = "account: " + str(account_num) + "| Login Pin: " + str(login_num)
                Account_full = user_name + " | " + account_name
                users_fixed.append(Account_full)
                return f"User '{user_name}' added successfully."
            else:
                return "User limit reached. Cannot add more users.", 400

###################################################################################

@app.route('/users', methods=['GET'])
def list_users():
    return jsonify(users)

@app.route('/users_fast', methods=['GET'])
def list_users_fast():
    return jsonify(users_fast)

@app.route('/users_fixed', methods=['GET'])
def list_users_fixed():
    return jsonify(users_fixed)

@app.route('/logout', methods = ['GET'])
def rm_users():
    global users
    global users_fast
    global users_fixed
    users = []
    users_fast = []
    users_fixed = []
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')