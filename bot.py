import telebot, random, movie, news, datetime, calendar, json, replykey, pickle, music, time
from googlesearch import search
from telebot import types
bot = telebot.TeleBot("1532672197:AAGBrhsDRQl5LLOch3bzqwka9AxKbIkrYDk")
pw=[]
pwr=[]

# import requests
# requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT"

def reply(message):
	chat=message.from_user.id
	text=message.text
	first_name=message.from_user.first_name
	date_today = datetime.datetime.fromtimestamp(int(message.date))

	print(first_name)
	print(chat)
	print(text)

	file_object = open('./history/'+str(chat)+".txt", 'a')
	file_object.write(first_name+" "+"\n")
	file_object.write(text+"  "+"\n")
	file_object.write(str(date_today)+"\n")
	file_object.write("\n")
	keyboard=keyfunc(message)
	
	if "hi"==text.lower() or "hello"==text.lower() or "namaste"==text.lower() or "hola"==text.lower():
		cap=random.choice(['Hello, Welcome', 'Hello there!', 'Hey there!', 'Namaste!', 'Hola!'])
		bot.send_message(chat,cap)
		bot.send_message(chat,"Hope you're doing well.", reply_markup=keyboard)
	elif text=="Append":
		bot.send_message(chat, "Append")
	elif text=="Send Post":
		reply_type=filetype(message)
		if str(chat)=="903774501":
			chat_group = "-1001387572466"
			bot.send_message(chat, "Trying to `Send Post`...", parse_mode="Markdown", reply_markup=keyboard)
		elif str(chat)=="1467813172":
			chat_group = "-1001162021879"
			bot.send_message(chat, "Trying to `Send Post`...", parse_mode="Markdown", reply_markup=keyboard)
		else:
			chat_group = ""
			bot.send_message(chat, "You are not the  `Admin`. You have no right to `Send Post`.", parse_mode="Markdown", reply_markup=keyboard)
		
		try:
			reply_key=message.reply_to_message.json["reply_markup"]
		except:
			reply_key={}
		#print(reply_key)
		reply_key=json.dumps(reply_key)
		
		if reply_type=="text":
			reply_doc = message.reply_to_message.json["text"]
		elif reply_type=="photo":
			reply_doc = message.reply_to_message.json["photo"][0]["file_id"]
		else:
			reply_doc = message.reply_to_message.json[reply_type]["file_id"]
		
		try:
			reply_cap = message.reply_to_message.json["caption"]
		except:
			reply_cap = ""
				
		if reply_type=="text":
			#print(message.reply_to_message.reply_markup.keyboard)
			bot.send_message(chat_group, reply_doc, reply_markup=reply_key)
			bot.send_message(chat, "`Post Sent`", parse_mode="Markdown", reply_markup=keyboard)		
		elif reply_type=="photo":
			print(message.reply_to_message.json)
			print(reply_doc)
			bot.send_photo(chat_group, reply_doc, caption=reply_cap, reply_markup=reply_key)
			bot.send_message(chat, "`Post Sent`", parse_mode="Markdown", reply_markup=keyboard)
		elif reply_type=="video":
			print(reply_doc)
			bot.send_video(chat_group, reply_doc, caption=reply_cap, reply_markup=reply_key)
			bot.send_message(chat, "`Post Sent`", parse_mode="Markdown", reply_markup=keyboard)
		elif reply_type=="document":
			reply_doc = message.reply_to_message.json["document"]["file_id"]
			print(reply_doc)
			bot.send_document(chat_group, reply_doc, caption=reply_cap, reply_markup=reply_key)
			bot.send_message(chat, "`Post Sent`", parse_mode="Markdown", reply_markup=keyboard)
		elif reply_type=="voice":
			reply_doc = message.reply_to_message.json["voice"]["file_id"]
			print(reply_doc)
			bot.send_voice(chat_group, reply_doc, caption=reply_cap, reply_markup=reply_key)
			bot.send_message(chat, "`Post Sent`", parse_mode="Markdown", reply_markup=keyboard)
		elif reply_type=="audio":
			reply_doc = message.reply_to_message.json["audio"]["file_id"]
			print(reply_doc)
			bot.send_audio(chat_group, reply_doc, caption=reply_cap, reply_markup=reply_key)
			bot.send_message(chat, "`Post Sent`", parse_mode="Markdown", reply_markup=keyboard)
		else:
			bot.send_message(chat, "There is  `No Post`  to send.\n\nTo  `Send Post` , Click on  `Send Post to Subscribers`  for more details.", parse_mode="Markdown", reply_markup=keyboard)
	elif text=="Send Post Reply":
		reply_type=filetype(message)
		if str(chat)=="903774501":
			chat_group = "-1001387572466"
			bot.send_message(chat, "Trying to `Send Post`...", parse_mode="Markdown", reply_markup=keyboard)
		elif str(chat)=="1467813172":
			chat_group = "-1001162021879"
			bot.send_message(chat, "Trying to `Send Post`...", parse_mode="Markdown", reply_markup=keyboard)
		else:
			chat_group = ""
			bot.send_message(chat, "You are not the  `Admin`. You have no right to `Send Post`.", parse_mode="Markdown", reply_markup=keyboard)
		
		reply_key = {
		"inline_keyboard": [
			[
				{"text": "👍", "callback_data": "good"},
				{"text": "👎", "callback_data": "ok"}
			]
		]
		}
		#print(reply_key)
		reply_key = json.dumps(reply_key)
		
		if reply_type=="text":
			reply_doc = message.reply_to_message.json["text"]
		elif reply_type=="photo":
			reply_doc = message.reply_to_message.json["photo"][0]["file_id"]
		else:
			reply_doc = message.reply_to_message.json[reply_type]["file_id"]
		
		try:
			reply_cap = message.reply_to_message.json["caption"]
		except:
			reply_cap = ""
				
		if reply_type=="text":
			#print(message.reply_to_message.reply_markup.keyboard)
			bot.send_message(chat_group, reply_doc, reply_markup=reply_key)
			bot.send_message(chat, "`Post Sent`", parse_mode="Markdown")		
		elif reply_type=="photo":
			print(message.reply_to_message.json)
			print(reply_doc)
			bot.send_photo(chat_group, reply_doc, caption=reply_cap, reply_markup=reply_key)
			bot.send_message(chat, "`Post Sent`", parse_mode="Markdown", reply_markup=keyboard)
		elif reply_type=="video":
			print(reply_doc)
			bot.send_video(chat_group, reply_doc, caption=reply_cap, reply_markup=reply_key)
			bot.send_message(chat, "`Post Sent`", parse_mode="Markdown", reply_markup=keyboard)
		elif reply_type=="document":
			reply_doc = message.reply_to_message.json["document"]["file_id"]
			print(reply_doc)
			bot.send_document(chat_group, reply_doc, caption=reply_cap, reply_markup=reply_key)
			bot.send_message(chat, "`Post Sent`", parse_mode="Markdown", reply_markup=keyboard)
		elif reply_type=="voice":
			reply_doc = message.reply_to_message.json["voice"]["file_id"]
			print(reply_doc)
			bot.send_voice(chat_group, reply_doc, caption=reply_cap, reply_markup=reply_key)
			bot.send_message(chat, "`Post Sent`", parse_mode="Markdown", reply_markup=keyboard)
		elif reply_type=="audio":
			reply_doc = message.reply_to_message.json["audio"]["file_id"]
			print(reply_doc)
			bot.send_audio(chat_group, reply_doc, caption=reply_cap, reply_markup=reply_key)
			bot.send_message(chat, "`Post Sent`", parse_mode="Markdown", reply_markup=keyboard)
		else:
			bot.send_message(chat, "There is  `No Post`  to send.\n\nTo  `Send Post` , Click on  `Send Post to Subscribers`  for more details.", parse_mode="Markdown", reply_markup=keyboard)
	elif text.lower()=="fi":
		reply_type=filetype(message)
		
		if reply_type=="text":
			reply_doc = message.reply_to_message.json["text"]
			bot.send_message(message.from_user.id, "`"+reply_doc+"`", parse_mode="Markdown")
		elif reply_type=="photo":
			reply_doc = message.reply_to_message.json["photo"][0]["file_id"]
			bot.send_message(message.from_user.id, "`"+reply_doc+"`", parse_mode="Markdown")
		else:
			reply_doc = message.reply_to_message.json[reply_type]["file_id"]
			bot.send_message(message.from_user.id, "`"+reply_doc+"`", parse_mode="Markdown")	
	elif "website" in text.lower() or "site" in text.lower():
		cap="Checkout our Website: \nhttps://saikrishna.epizy.com/form.\n\nAny Suggestions are Welcomed. \nSubmit your Suggestions in our Website."
		web = types.InlineKeyboardMarkup(row_width=3)
		a = types.InlineKeyboardButton(text="Website", url="saikrishna.epizy.com/form")
		b = types.InlineKeyboardButton(text="Suggestions", url="saikrishna.epizy.com/form/index-services.html")
		web.add(a, b)
		bot.send_photo(chat,"AgACAgUAAxkBAAIW22AYKPHVugHFO6vFtQWP62MWOTcMAAL3qjEbQhXAVP9yv__eMTgc59T-bnQAAwEAAwIAA20AA1sQAAIeBA",cap, reply_markup=web)
		bot.send_message(chat, "", reply_markup=keyboard)
	elif "what" in text.lower() and "you" in text.lower() and "do" in text.lower() or "what" in text.lower() and "u" in text.lower() and "do" in text.lower() or "wt" in text.lower() and "you" in text.lower() and "do" in text.lower() or "wt" in text.lower() and "u" in text.lower() and "do" in text.lower():
		text1="I can answer you some basic questions. Test me now. Send your suggestions to our Website or Personally. Type 'Website' for more."
		bot.send_message(chat, text1, reply_markup=keyboard)
	elif "who" in text.lower() and "you" in text.lower() or "who" in text.lower() and "u" in text.lower():
		text1="Hi, I'm a ChatBot 🤖🤖. I can answer you some basic questions. Test me now. Send your suggestions to our Website or Personally. Type 'Website' for more."
		bot.send_message(chat, text1, reply_markup=keyboard)
	elif "how are you" in text.lower() or "how" in text.lower() and "doing" in text.lower() or "how" in text.lower() and "do" in text.lower() or "how" in text.lower() and "dng" in text.lower():
		text1="I'm fine, Thanks. Hoping same from you"
		bot.send_message(chat, text1, reply_markup=keyboard)
	elif "fine" in text.lower():
		text1="Good to know"
		bot.send_message(chat, text1, reply_markup=keyboard)
	elif "doubt" in text.lower():
		text1="Ask my Owner @saikrishna7004"
		bot.send_message(chat, text1, reply_markup=keyboard)
	elif "media" in text.lower():
		text1=f"You have sent a  `{str(type).title()}`."
		bot.send_message(chat, text1, reply_markup=keyboard)
	elif "send post to subscribers" in text.lower():
		text1="To `Send Post` to Subscribers: \n\n`Step1:` Send your `File` or `Media` to this `ChatBot`. \n\n`Step2:` `Reply` to the `File` or `Media` saying `Send Post`. \n\nOnly for `Admins`."
		bot.send_message(chat, text1, reply_markup=keyboard, parse_mode="Markdown")
	elif "calendar" in text.lower() or "calender" in text.lower():
		d=str(date_today).split("-")
		text1="`"+calendar.month(int(d[0]), int(d[1]))+"`"
		print(text1.replace("`",""))
		bot.send_message(chat, text1, reply_markup=keyboard, parse_mode="Markdown")
	elif "news" in text.lower():
		result=news.newsapi()
		t=result[0]
		d=result[1]
		u=result[2]
		for i in range(0,len(t)):
			key = types.InlineKeyboardMarkup(row_width=3)
			a = types.InlineKeyboardButton(text="Read Full", url=u[i])
			key.add(a)
			bot.send_message(chat, t[i]+"\n\n"+d[i], reply_markup=key)
		bot.send_message(chat, "👍", reply_markup=keyboard)
	elif text=="Loading":
		text1="I'll show you a small loading sequence."
		r=bot.send_message(chat, text1)
		key = {
		"inline_keyboard": [
			[
				{"text": "👍", "callback_data": "good"},
				{"text": "👎", "callback_data": "ok"}
			]
		]
		}
		message_id=r.id
		loading(chat, message_id, reply_markup=json.dumps(key))
	elif "solve" in text.lower():
		que=text.lower().replace('solve',' ').strip()
		if "power" in que:
			try:
				que1=que.replace(' ','').replace("power","").replace("(","").replace(")","").strip()
				que2=que1.split(",")
				x=que2[0]
				y=que2[1]
				z=power(x,y)
				text1=str(z)
			except:
				text1="I'm unable to answer the Question. Please verify the question and try again."
		
		else:
			try:
				ans=eval(que)
				text1=str(ans)
			except:
				text1="I'm unable to answer the Question. Please verify the question and try again."
		bot.send_message(chat, text1, reply_markup=keyboard)
	elif "https://youtu" in text.lower():
		import youtube
		title = youtube.you(text)
		bot.send_video(chat, open("youtube/"+title+".mp4", "rb"))
	elif "thank" in text.lower():
		text1="It's my Pleasure 😃."
		bot.send_message(chat, text1, reply_markup=keyboard)
	elif "bye" in text.lower() or "see you" in text.lower() or "tata" in text.lower():
		text1="Good bye 👋. \nHope you return soon."
		bot.send_message(chat, text1, reply_markup=keyboard)
	elif "help" in text.lower() or "/help" in text.lower():
		text1="Hello, I'm a ChatBot🤖🤖. \nYou can chat with me.\nIf I don't know something, I'll search it in Google.\n\n"+"Contact my owner for more details in our Website. \nType or Click on 'Website' for more."
		text2="Here are some commands I can do: \n\nHi, Hello, Namaste, Hola\nWebsite, Site, Web\nHow r u\nI'm fine\nWho r u\nSolve somequestion\nSolve power(x,y) => It gives x^y \nLoading \nSongs \nMovies \nHistory \nPwr \nCalender \nBye \n\n"
		bot.send_message(chat, text1, reply_markup=keyboard)
		bot.send_message(chat, text2, reply_markup=keyboard)
	elif "history" in text.lower():
		key=replykey.key
		bot.send_message(chat, "Please Enter the Password: ", reply_markup=json.dumps(key))
	elif "pwr"==text.lower():
		key=replykey.key2
		bot.send_message(chat, "Enter the New Password: ", reply_markup=json.dumps(key))
	elif text=="Songs":
		text1="Select an  `Album`  from here. Enjoy the  `Music`  🎶🎧🎵🎶."
		bot.send_message(chat, text1, reply_markup=json.dumps(music.musickey), parse_mode="Markdown")
	elif "search" in text.lower():
		if text.lower().replace('search','').strip()!="":
			text2="Searching for "+text.lower().replace('search','').strip()+". Please wait..."
			bot.send_message(chat, text2, reply_markup=keyboard)
			ans=google_func(text.lower().replace('search','').strip(),5)
			for x in ans:
				bot.send_message(chat, x, reply_markup=keyboard)  
		else:
			text1="Type what you want to Search. Type 'Search' and add your search keywords to search."
			bot.send_message(chat, text1, reply_markup=keyboard)
	elif "m1" in text.lower() or "m2" in text.lower() or "m3" in text.lower() or "m4" in text.lower() or "m5" in text.lower() or "m6" in text.lower() or "m7" in text.lower() or "m8" in text.lower() or "m9" in text.lower() or "m10" in text.lower() or "m11" in text.lower() or "m12" in text.lower() or "m13" in text.lower() or "m14" in text.lower() or "m15" in text.lower():
		moviesend(chat, text)
	elif "movie" in text.lower():
		bot.send_message(chat, "Select Movie Below", reply_markup=movie.key1)				
	else:
		text1="👍"
		text2="You said: "+text+". I'm searching in google. Please wait..."
		bot.send_message(chat, text2, reply_markup=keyboard)
		ans = google_func(text, 5)
		for x in ans:
			bot.send_message(chat, x)
		bot.send_message(chat, text1, reply_markup=keyboard)

def replycall(call):
	#print(call)
	chat = call.message.chat.id
	try:
		from_id = call.from_user.id
	except:
		from_id = chat
		print("paki")
	data = call.data
	this_id = call.message.message_id
	print(this_id)
	print(from_id)
	open("password.txt", 'a').close()
	if data=="m1" or data=="m2" or data=="m3" or data=="m4" or data=="m5" or data=="m6" or data=="m7" or data=="m8" or data=="m9" or data=="m10" or data=="m11" or data=="m12" or data=="m13" or data=="m14" or data=="m15":
		name=movie.moviecheck(data)
		n=movie.names[name][5]
		bot.edit_message_text("You have Selected:\n"+n+"\n\n"+"Select Quality", chat, reply_markup=json.dumps(movie.sizekeyedit(data)), message_id=this_id)
	elif data=="m0":
		bot.edit_message_text("Select Movie Below", chat, reply_markup=movie.key1,  message_id=this_id)
	elif "m1" in data or "m2" in data or "m3" in data or "m4" in data or "m5" in data or "m6" in data or "m7" in data or "m8" in data or "m9" in data or "m10" in data or "m11" in data or "m12" in data or "m13" in data or "m14" in data or "m15" in data:
		moviesend(chat, data)
	elif data=="pta":
		key=replykey.key
		bot.edit_message_text("Please Enter the Password: ", chat, reply_markup=json.dumps(key), message_id=this_id)
	elif data=="good" or data=="ok":
		file_name='react/'+str(chat)+"_"+str(this_id)+".txt"
		try:
			react=open(file_name, 'rb')
		except:
			react=open(file_name, 'wb')
			pickle.dump([[],[]],react)
			react=open(file_name, 'rb')
		passs=pickle.load(react)
		print(passs)
		if data=="good":
			if passs[0].__contains__(from_id):
				passs[0].remove(from_id)
				bot.answer_callback_query(call.id, "You took you reaction back.")
			else:
				passs[0].append(from_id)
				bot.answer_callback_query(call.id, "You reacted : "+data)
			if passs[1].__contains__(from_id):
				passs[1].remove(from_id)
			else:
				pass
		else:
			if passs[1].__contains__(from_id):
				passs[1].remove(from_id)
				bot.answer_callback_query(call.id, "You took you reaction back.")
			else:
				passs[1].append(from_id)
				bot.answer_callback_query(call.id, "You reacted : "+data)
			if passs[0].__contains__(from_id):
				passs[0].remove(from_id)
			else:
				pass
		passs[0]=list(set(passs[0]))
		passs[1]=list(set(passs[1]))
		print(passs)
		p0=str(len(passs[0]))
		p1=str(len(passs[1]))
		if p0=="0":
			p0=""
		if p1=="0":
			p1=""
		kgo = {
					"inline_keyboard": [
						[
							{"text": "👍 "+p0, "callback_data": "good"},
							{"text": "👎 "+p1, "callback_data": "ok"}
						]
					]
			}
		bot.edit_message_reply_markup(chat, this_id, reply_markup=json.dumps(kgo))
		react1=open(file_name, 'wb')
		pickle.dump(passs, react1)
	elif "q1" in data or "q2" in data or "q3" in data or "q4" in data or "q5" in data or "q6" in data or "q7" in data or "q8" in data or "q9" in data or "q0" in data or "qt" in data or "qw" in data:
		pw.append(data)
		print(pw)
		print("\n")
		if data=="qt":
			fp=open('password/'+str(chat)+'.txt', 'rb')
			try:
				pas = pickle.load(fp)
			except:
				bot.edit_message_text('It seems like you have not set any Password. \n\nPlease type "pwr" and set a Password.', chat, message_id=this_id)
				pw.clear()
				pas = ""
			if pw==pas:
				print("Correct Password\n")
				bot.edit_message_text("Correct Password", chat, message_id=this_id)
				pw.clear()
				time.sleep(2)
				try:
					text1=str(int(int(file_len("history/"+str(chat)+".txt"))/4))+" Messages till now."
					clear = {
					"inline_keyboard": [
							[
								{"text": "📥 Get History 📥", "callback_data": "gh"}
							],
							[
								{"text": "❌ Clear History ❌", "callback_data": "ch"}
							],
						]
					}
				except:
					text1="History is empty"
					clear = {}
				bot.edit_message_text(text1, chat, reply_markup=json.dumps(clear), message_id=this_id)
			elif pas=="":
				pass
			else:
				print("Wrong Pasword\n\n")
				ta = {
					"inline_keyboard": [
						[
							{"text": "Try Again", "callback_data": "pta"}
						]
					]
				}
				bot.edit_message_text("Wrong Password", chat, reply_markup=json.dumps(ta), message_id=this_id)
				pw.clear()
		elif data=="qw":
			pw.clear()
	elif data=="ch":
		open('history/'+str(chat)+'.txt', 'w').close()
		text1="0 Messages till now."
		bot.edit_message_text(text1, chat, message_id=this_id)
	elif data=="gh":
		try:
			file=open('history/'+str(chat)+'.txt','r')
			bot.send_document(chat, file, caption="History")
		except:	
			bot.send_message(chat, "The history is empty")			   
	elif data=="clear":
		bot.edit_message_text("_🚫 This message was deleted_", chat, message_id=this_id, parse_mode="Markdown")
		time.sleep(3)
		bot.delete_message(chat, this_id)
		bot.delete_message(chat, this_id-1)
	elif "cs" in data:
		r="a"+data.replace("cs", "")
		mf=[]
		for x in range(len(music.files[r])):
			mf.append(types.InputMediaAudio(music.files[r][x]))
		bot.send_media_group(chat, mf)		 		
	elif "r1" in data or "r2" in data or "r3" in data or "r4" in data or "r5" in data or "r6" in data or "r7" in data or "r8" in data or "r9" in data or "r0" in data or "rt" in data or "rw" in data:
		pwr.append(data.replace("r","q"))
		print(pwr)
		print("\n\n")
		if data=="rt":
			open("password/"+str(chat)+".txt", "w").close()
			with open("password/"+str(chat)+".txt", 'wb') as fp:
				pickle.dump(pwr, fp)
				fp.close()
			print("Password Reset Successful\n\n")
			pwr.clear()
			bot.edit_message_text("Password Reset Successful", chat, message_id=this_id)
		elif data=="rw":
			pwr.clear()

def file_len(fname):
    with open(fname,"r", encoding='utf8', errors='ignore') as f:
        for i, l in enumerate(f):
            type(l)
            pass
    return i + 1

# Handles all text messages that contains the commands '/start' or '/help'.
@bot.message_handler(commands=['start'])
def handle_start(message):
	#print(message)
	keyboard=keyfunc(message)
	text1="Hello, my name is ChatBot\nMade using Python\nMade by Sai Krishna\nI'm a ChatBot"
	bot.send_message(message.from_user.id, text1, reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def handle_help(message):
	#print(message)
	text1="Hello, I'm a ChatBot🤖🤖. \nYou can chat with me.\nIf I don't know something, I'll search it in Google.\n\n"+"Contact my owner for more details in our Website. \nType or Click on 'Website' for more."
	text2="Here are some commands I can do: \n\nHi, Hello, Namaste, Hola\nWebsite, Site, Web\nHow r u\nI'm fine\nWho r u\nSolve somequestion\nSolve power(x,y) => It gives x^y \nLoading \nSongs \nMovies \nHistory \nPwr \nCalender \nBye \n\n"
	keyboard=keyfunc(message)
	bot.send_message(message.from_user.id, text1, reply_markup=keyboard)
	bot.send_message(message.from_user.id, text2, reply_markup=keyboard)

@bot.message_handler(commands=['settings'])
def handle_settings(message):
	#print(message)
	text1="There is nothing to setup."
	text2="CAACAgIAAxkBAAIx9GBgksL3pnLZ6VjyjptNN49OjmljAAI4BQACP5XMCivNw0w_QtinHgQ"
	keyboard=keyfunc(message)
	bot.send_message(message.from_user.id, text1, reply_markup=keyboard)
	bot.send_sticker(message.from_user.id, text2, reply_markup=keyboard)

# Handles all callback_data
@bot.callback_query_handler(func=lambda call: True)
def test_callback(call):
	#print(call.message.chat)
	print(call.data)
	#print(call.message.message_id)
	replycall(call)

def mov(ques):
	ques=ques.lower().replace("movie","")
	print(ques)
	res=sort(ques)
	results = []
	i=1
	for ques1 in res:
		if i>10:
			break
		if movie.names.__contains__(ques1):
			mnq = movie.names[ques1]
			for x in range(0,5):
				if mnq[x]!="0":
					try:
						mnq[6]
						results.append(types.InlineQueryResultCachedVideo(i, mnq[x], mnq[5], "\nSize: " + movie.msize(x)))
						print(results)
					except IndexError:
						results.append(types.InlineQueryResultCachedDocument(i,  mnq[x], mnq[5], "\nSize: " + movie.msize(x)))
					i+=1
		i+=1
	return results		
	
@bot.inline_handler(func=lambda query: True)
def inline_test(query):
	#print(query)
	chat=query.from_user.id
	first_name=query.from_user.first_name
	ques=query.query
	iqi=query.id
	print(chat)
	print(first_name)
	print("query:", ques)
	
	if ques=="":
		bot.answer_inline_query(iqi, results=[], switch_pm_text="Type something..😁", switch_pm_parameter="start")
	elif "movie" in ques:
		results=mov(ques)
		try:
			bot.answer_inline_query(iqi, results, switch_pm_text="Found "+str(len(results))+" results", switch_pm_parameter="start")
		except Exception as e:
			print(e)
	elif ques=="loading":
		kkey =  {
					"inline_keyboard": [
						[
							{"text": "👍", "callback_data": "good"},
							{"text": "👎", "callback_data": "ok"}
						]
					]
			}
		res=[types.InlineQueryResultArticle(12, "Reaction Test", "Reaction Test. Press any emoji below.", kkey)]
		bot.answer_inline_query(iqi, results=res, switch_pm_text="Results found", switch_pm_parameter="start")

	else:
		bot.answer_inline_query(iqi, results=[], switch_pm_text="No results found😞", switch_pm_parameter="start")
		return
		
# Handles all sent documents and audio files
@bot.message_handler(content_types=['document', 'audio', 'photo', 'video', 'voice', 'animation', 'sticker'])
def handle_docs_audio(message):
	#print(message)
	bot.send_message(message.from_user.id, "You have sent  `"+message.content_type.capitalize()+"` .", parse_mode="Markdown")

@bot.channel_post_handler(content_types=["text"])
def channel_post(message):
	#print(message)
	chat=message.chat.id
	text=message.text
	first_name=message.chat.title
	date_today = datetime.datetime.fromtimestamp(int(message.date))
	print(first_name)
	print(chat)
	print(text)
	if text=="Loading":
		text1="I'll show you a small loading sequence."
		r=bot.send_message(chat, text1)
		key = {
		"inline_keyboard": [
			[
				{"text": "👍", "callback_data": "good"},
				{"text": "👎", "callback_data": "ok"}
			]
		]
		}
		message_id=r.id
		loading(chat, message_id, reply_markup=json.dumps(key))

# Handles all text messages that match the regular expression
@bot.message_handler(regexp="SOME_REGEXP")
def handle_message(message):
	pass

@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
	#print(message.text)
	print(message.chat.type)
	reply(message)
	
# Handlers can be stacked to create a function which will be called if either message_handler is eligible
# This handler will be called if the message starts with '/hello' OR is some emoji
@bot.message_handler(commands=['hello'])
def send_something(message):
    bot.reply_to(message, message.text)

def filetype(message):
	if message.json["reply_to_message"].__contains__("text"):									 
		mtype = "text"
	elif message.json["reply_to_message"].__contains__("photo"):
		mtype = "photo"
	elif message.json["reply_to_message"].__contains__("video"):
		mtype = "video"
	elif message.json["reply_to_message"].__contains__("voice"):
		mtype = "voice"
	elif message.json["reply_to_message"].__contains__("animation"):
		mtype = "animation"
	elif message.json["reply_to_message"].__contains__("document"):
		mtype = "document"
	elif message.json["reply_to_message"].__contains__("audio"):
		mtype = "audio"
	elif message.json["reply_to_message"].__contains__("sticker"):
		mtype = "sticker"
	else:
		mtype = "other"
	return mtype

def moviesend(chat, text):
	#print(text)
	a=text.lower().split(" ")
	a1=a[0].strip()
	name=movie.moviecheck(a1.lower())
	#print(name)
	if len(a)==1:
		size="a"
	else:
		a2=a[1].strip()
		size=movie.sizecheck(a2.lower())
	#print(size) 
	doc_type="document" 
	if size=="a":
		lst=[]
		text1="Loading, please wait..."
		r=bot.send_message(chat, text1)
		#print(r)
		message_id = r.id
		#print(message_id)
		loading(chat, message_id , "Here is your requested Movie.", skip=5)
		try:
			movie.names[name][6]
			doc_type="video"
		except:
			pass
		def docvideo(x, doc_type="document", cap=""):
			if doc_type=="video":
				return types.InputMediaVideo(x, caption=cap, parse_mode="Markdown")
			return types.InputMediaDocument(x, caption=cap, parse_mode="Markdown")
		for x in range(0,5):
			if movie.names[name][x]!="0":
				ms=movie.msize(x)
				mn=movie.names[name][5]
				mc="*@saikrishnakarnati "+mn+" "+ms+"\n✯ ━━━━━━━ ✧ ━━━━━━━━ ✯\nhttps://t.me/saikrishnakarnati*"
				lst.append(docvideo(movie.names[name][x], doc_type, mc))
			else:
				pass
		bot.send_media_group(chat, lst)
	elif size==5:
		bot.send_message(chat, "`Quality Not Found.` \n\nPlease try another  `Quality` .")
	else:
		if movie.names[name][size]!="0":
			file_id=movie.names[name][size]
			text1="Loading, please wait..."
			r=bot.send_message(chat, text1)
			#print(r.id)
			message_id = r.id
			loading(chat, message_id , "Here is your requested Movie.", skip=5)
			mn=movie.names[name][5]
			ms=movie.msize(size)
			mc="*@saikrishnakarnati "+mn+" "+ms+"\n✯ ━━━━━━━ ✧ ━━━━━━━━ ✯\nhttps://t.me/saikrishnakarnati*"
			try:
				movie.names[name][6]
				doc_type="video"
			except:
				pass
			if doc_type=="document":
				bot.send_document(chat, file_id, caption=mc, parse_mode="Markdown")
			else:
				bot.send_video(chat, file_id, caption=mc, parse_mode="Markdown")
		else:
			bot.send_message(chat, "`Quality Not Found.` \n\nPlease try another  `Quality` .", parse_mode="Markdown")

def loading(chat_id, message_id, final="How's it?", reply_markup=None, skip=1):
    i=0
    time.sleep(0.5)
    for i in range(0,11):
      if i%skip==0:
        #print (i)
        j=10-i
        em="["+i*"▓"+j*"▒"+"]"+"\n\n"+str(i*10)+"% Done"+"\n\nLoading, please wait..."
        bot.edit_message_text(em, chat_id, message_id=message_id)
        #print("")
        #time.sleep(0.3)
    bot.edit_message_text(final, chat_id, message_id=message_id, reply_markup=reply_markup)
    #time.sleep(0.5)

def power(x,y):
	z=float(x)**float(y)
	if "e" in str(z):
		z0=round(float(str(z).split("e")[0]), 4)
		ans=str(z0)+" × 10 ^"+str(z).split("e")[1].replace("+"," ")
		return ans
	return z

def google_func(q, n):
	l=[]
	for i in search(query=q,tld='co.in',num=10,stop=n,pause=1):
		l.append(i.replace("_", r"\_"))
	return l

def sort(ques):
	set=['master','krack','rangde','sbsb','red',
		'bangarubullodu','alluduadhurs','aranya',
		'30rpe','check','jathiratnalu','sreekaram',
		'uppena','pogaru','naandhi']
	ans=[]
	for x in set:
		if ques in x:
			ans.append(x)
	print(ans)
	return ans

def keyfunc(message):
		chat=message.from_user.id
		if str(chat)=="903774501" or str(chat)=="1467813172":
			lastbtn='Send Post To Subscribers'
		else:
			lastbtn='Feedback'																																																																																																																																																																																																										 
		keyboard = types.ReplyKeyboardMarkup(row_width=2)
		itembtn1 = types.KeyboardButton('Movies')
		keyboard.row(itembtn1)
		itembtn2 = types.KeyboardButton('Website')
		itembtn3 = types.KeyboardButton('Help')
		keyboard.row(itembtn2,itembtn3)
		itembtn4 = types.KeyboardButton('Songs')
		itembtn5 = types.KeyboardButton('News')
		keyboard.row(itembtn4,itembtn5)
		itembtn6 = types.KeyboardButton(lastbtn)
		keyboard.row(itembtn6)
		return keyboard

bot.polling(none_stop=True)