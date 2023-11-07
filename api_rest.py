from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name)
