
import os
from flask import Flask, redirect, render_template, request, url_for
import json
import geocoder

from website.database import encrypt
from website.database.db import dbORM
from website.utils import helper, id_generator
from website.utils.DateToolKit import clean_date


def initialize_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sdadsadakmi23e'
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__).replace('\\', '/'), 'static/upload')
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
    
    @app.route("/dashboard")
    def dashboard():
        payload = helper.template_payload()
    
        try:
            client_ip = geocoder.ip('me').ip
        except:
            ip_address = request.remote_addr
            client_ip = ip_address
            
        helper.checkLoginAndLogin(client_ip)
        
        payload['LengthFunc'] = len
        payload['USERCHATS'] = dbORM.get_all("USERCSCAnonymousCHAT")[f'{helper.isFound("USERCSCAnonymousCHAT", "ip_address", client_ip)}']
        
        
        return render_template("dashboard.html", **payload)
    
    @app.route("/")
    def landing():
        
        return render_template("landing.html")
    
    @app.route("/your-rooms")
    def yourRooms():
        
        payload = helper.template_payload()
        try:
            client_ip = geocoder.ip('me').ip
        except:
            ip_address = request.remote_addr
            client_ip = ip_address
            
        payload['USERROOMS'] = helper.isFoundAll("CSCAnonymousCHATROOM" , "ouid", helper.checkLoginAndLogin(client_ip)['uid'])
        payload['DTK'] = clean_date

        
        return render_template("dashboard.html", **payload)
    
    @app.route("/create-chat-room", methods=['POST'])
    def createChatRoom():
        
        
        
        payload = helper.template_payload()
    
        try:
            client_ip = geocoder.ip('me').ip
        except:
            ip_address = request.remote_addr
            client_ip = ip_address
            
        helper.checkLoginAndLogin(client_ip)
        
        rid = id_generator.generate_id(6)
        new_room = {
            "room_name": request.form['room_name'],
            "datestamp": helper.getDateTime()[0],
            "rid": rid,
            "ouid": helper.checkLoginAndLogin(client_ip)['uid']
        }
        dbORM.add_entry("CSCAnonymousCHATROOM", encrypt.encrypter(str(new_room)))
        
        payload['LengthFunc'] = len
        payload['USERCHATS'] = helper.isFoundAll("CSCAnonymousCHAT", "ouid", helper.checkLoginAndLogin(client_ip)['uid'])
        
        return redirect(url_for("yourRooms"))
    
    @app.route("/add-chat", methods=['POST'])
    def addChat():
        payload = helper.template_payload
        try:
            client_ip = geocoder.ip('me').ip
        except:
            ip_address = request.remote_addr
            client_ip = ip_address
        
        helper.checkLoginAndLogin(client_ip)
        
            
        new_chat = {
            "message": "DEV DEV",
            "ip_address": client_ip,
            "ouid": helper.checkLoginAndLogin(client_ip)['uid'],
            "lat": f"{geocoder.ip('me').lat}",
            "lng": f"{geocoder.ip('me').lng}",
            "cid": id_generator.generate_id(16),
            "datestamp": helper.getDateTime()[0]
        }
        dbORM.add_entry("CSCAnonymousCHAT", encrypt.encrypter(str(new_chat)))
        
        payload['OUID'] = helper.checkLoginAndLogin(client_ip)['uid']
        
        return render_template("chat.html")
    
    @app.route("/room/<string:room_name>/<string:room_id>")
    def visitRoom(room_name, room_id):
        payload = helper.template_payload()
        
        try:
            client_ip = geocoder.ip('me').ip
        except:
            ip_address = request.remote_addr
            client_ip = ip_address
        
        helper.checkLoginAndLogin(client_ip)
        
        
        theRoom = dbORM.get_all("CSCAnonymousCHATROOM")[f'{helper.isFound("CSCAnonymousCHATROOM", "rid", room_id)}']
        print("mzilla", helper.checkLoginAndLogin(client_ip)['uid'])
        if helper.checkLoginAndLogin(client_ip)['uid'] == theRoom['ouid']:
            
            payload['ROOMCHATS'] = helper.isFoundAll("CSCAnonymousCHAT", "ouid", helper.checkLoginAndLogin(client_ip)['uid'])
            payload['ROOM_NAME'] = room_name
            payload['ROOM_ID'] = room_id
        
            return render_template("roomchats.html", **payload)
        
        else:
        
            payload['OUID'] = helper.checkLoginAndLogin(client_ip)['uid']
            
            return render_template("chat.html", **payload)
        
        
            
                
            
    
    return app
