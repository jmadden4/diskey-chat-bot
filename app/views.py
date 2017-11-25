from app import app
import json
import datetime


from flask import jsonify, render_template, request, url_for, jsonify, make_response

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		return render_template('index.html')
	return render_template('index.html')


@app.route('/_askChatBot/<id>', methods=['GET', 'POST'])
def askChatBot(id):
	time_stamp = datetime.datetime.now()
	id = time_stamp	
	id_to_post = id
	#from diskeyChatBotModel import stemmer
	id = -1
	#id = time_stamp
	#id_to_send = 
	question="hello mr bear?"
	print id_to_post
	print id
	#return json.dumps({'status': 'OK','question':question})
	return jsonify(id_to_post)

@app.route('/_fetchFromChatBot/<id>', methods=['GET', 'POST'])
def fetchFromChatBot(id):
	import os, sys, random
	#from diskeyChatBotModel import words	
	#os.system('python /home/joe/workspace/diskey-bot/diskeyChatBotModel.py')
	#resp = words
	#resp = "wowww"
	#os.system('python /home/joe/workspace/diskey-bot/diskeyChatBotResponse.py')
	from diskeyChatBotResponse import response
	input1 = "shark"
	input2 = "pup"
	input3 = "sleepy"
	imgPath1 = url_for('static', filename='sharkDog.jpg')	
	imgPath2 = url_for('static', filename='DiscoDayCare.jpg')
	imgPath3 = url_for('static', filename='tiredTuckedIn.jpg')
	combos = [0, 1, 2]
	comboTemp = random.choice(combos)	
	combo = comboTemp
	imgs = [imgPath1, imgPath2, imgPath3]
	imgTemp = imgs[combo]
	imgPath = imgTemp
	
	imgString = "<img src="+imgPath+" width=100px height=170px></img>" 
	inputOptions = [input1, input2, input3]	
	resp1 = response(input1)
	resp2 = response(input2)
	resp3 = response(input3)
	respInput = [input1, input2, input3]
	#respTemp = random.choice(respInput)
	respTemp = respInput[combo]
	respTemp2 = response(respTemp)
	responseTable =  "<table class=""table"">\
				<thead>\
				 <tr>\
				     <th>Input Value #1</th>\
				     <th>Input Value #2</th>\
				     <th>Diskey Bot Output</th>\
				</thead>\
				</tr>\
				<tbody>\
				<tr>\
				     <td><h4>"+imgString+"</h4></td>\
				     <td><h4>"+respTemp+"</h4></td>\
				     <td><h4>"+respTemp2+"</h4></td>\
				</tr>\
				</tbody>\
			</table>"
	#resp = "Response from Diskey Bot is: " + "<h3>" + respTemp2 + "</h3><br/>"+ "\n" + "\n" + "Input was: "+respTemp + "\n"
	return responseTable