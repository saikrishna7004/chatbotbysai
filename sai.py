import json, requests, time, random, urllib, calendar, news, pickle, utils, music, movie, replykey
from googlesearch import search
from datetime import datetime, timezone

TOKEN = "1532672197:AAGBrhsDRQl5LLOch3bzqwka9AxKbIkrYDk"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

pw=[]
pwr=[]

def get_url(url):
	response = requests.get(url)
	content = response.content.decode("utf8")
	return content

def get_json_from_url(url):
	content = get_url(url)
	js = json.loads(content)
	return js

def get_updates(offset=None):
	url = URL + "getUpdates?timeout=100"
	if offset:
		url += "&offset={}".format(offset)
	js = get_json_from_url(url)
	return js

def get_last_update_id(updates):
	update_ids = []
	for update in updates["result"]:
		update_ids.append(int(update["update_id"]))
	return max(update_ids)

def get_last_chat_id_and_text(updates):
	num_updates = len(updates["result"])
	last_update = num_updates - 1
	text = updates["result"][last_update]["message"]["text"]
	chat_id = updates["result"][last_update]["message"]["chat"]["id"]
	return (text, chat_id)

def getmsg(updates):
 for update in updates["result"]:
		try:
			if update.__contains__("message"):
				type = str(typecheck(update))
				if type=="text":
					text = update["message"]["text"]
				else:
					text = "media"
				chat = update["message"]["chat"]["id"]
				if update["message"][type].__contains__("file_id"):
					if type=="video":
						file_id = update["message"][type]["file_id"]
					else:
						file_id = update["message"][type][0]["file_id"]
				else:
					file_id = " "
			else:
				pass
		except Exception as e:
			print(e)
 return chat, type, file_id, text

def echo_all(updates):
	for update in updates["result"]:
		try:
			if update.__contains__("message"):
				mtype = typecheck(update)
				if mtype=="text":
					text = update["message"]["text"]
					caption = ""
					type(caption)
				else:
					text = "media"
					if update["message"].__contains__("caption"):
						caption = update["message"]["caption"]
					else:
						caption = ""
				if update["message"].__contains__("reply_to_message"):
					reply_msg = update["message"]["reply_to_message"]
					type(reply_msg)
					if update["message"]["reply_to_message"].__contains__("document"):
						reply_type = "document"
						reply_doc = update["message"]["reply_to_message"]["document"]["file_id"]
					elif update["message"]["reply_to_message"].__contains__("video"):
						reply_type = "video"
						reply_doc = update["message"]["reply_to_message"]["video"]["file_id"]
					elif update["message"]["reply_to_message"].__contains__("photo"):
						reply_type = "photo"
						reply_doc = update["message"]["reply_to_message"]["photo"][0]["file_id"]
					elif update["message"]["reply_to_message"].__contains__("voice"):
						reply_type = "voice"
						reply_doc = update["message"]["reply_to_message"]["voice"]["file_id"]
					elif update["message"]["reply_to_message"].__contains__("audio"):
						reply_type = "audio"
						reply_doc = update["message"]["reply_to_message"]["audio"]["file_id"]
					else:
						reply_type = "text"
						reply_doc = update["message"]["reply_to_message"]["text"]
					if update["message"]["reply_to_message"].__contains__("caption"):
						reply_cap = update["message"]["reply_to_message"]["caption"]
					else:
						reply_cap = ""
					print("\n"+reply_type)
					print(reply_doc)
					print("\n"+reply_cap)
				else:
					reply_msg = ""
					reply_type = ""
					reply_doc = ""
					reply_cap = ""
				
				
				timestamp = update["message"]["date"]
				chat = update["message"]["chat"]["id"]
				first_name = update["message"]["chat"]["first_name"]
				if update["message"]["chat"].__contains__("last_name"):
					last_name = update["message"]["chat"]["last_name"]
				else:
					last_name = ""
				message_id = update["message"]["message_id"]
				if update["message"][mtype].__contains__("file_id") or update["message"][mtype][0].__contains__("file_id"):
					if mtype=="photo":
						file_id = update["message"][mtype][0]["file_id"]
					else:
						file_id = update["message"][mtype]["file_id"]		   
				else:
					file_id = ""					  
				date_today = datetime.fromtimestamp(int(timestamp))   
				file_object = open('./history/'+str(chat)+".txt", 'a')
				file_object.write(first_name+" "+last_name+"\n")
				file_object.write(text+"  "+file_id+"\n")
				file_object.write(str(date_today)+"\n")
				file_object.write("\n")
				print(first_name)
				print(chat)
				print(text+'\n')
			
				if str(chat)=="903774501" or str(chat)=="1467813172":
					keyboard = long_keyboard([['Movies'],['Website','Help'],['Songs','News'],['Send Post To Subscribers']])
				else:
					keyboard = long_keyboard([['Movies'],['Website','Help'],['Songs','News'], ['Feedback']])																																																																																																																																																																																																										 
				
				if reply_doc=="Type your feedback here":
					fb = open('fb.txt','a')
					fb.write(first_name)
					fb.write("\n")
					fb.write(str(chat))
					fb.write("\n")
					fb.write(text)
					fb.write("\n\n")
					reply("Thanks for your valuable Feedback 😃.", chat, keyboard, message_id)
					break
				else:
					pass
				
				if len(text)>=250:
					reply("Long text message",chat, keyboard, message_id)
					break
				else:
					pass
					
				
				if text=="Send Post":   
					if str(chat)=="903774501":
						chat_group = "-1001185534031"
					elif str(chat)=="1467813172":
						 chat_group = "-1001162021879"
					else:
						 chat_group = ""
						 reply("You are not the  `Admin`. You have no right to `Send Post`.",chat)
					reply("Trying to `Send Post`...",chat)
					print(file_id)
					if reply_type=="text":
						reply(reply_doc, chat_group)
						reply("`Post Sent`", chat)		
					elif reply_type=="photo":
						utils.send_photo(chat_group, reply_doc, reply_cap)
						reply("`Post Sent`", chat)
					elif reply_type=="video":
						utils.send_video(chat_group, reply_doc, reply_cap)
						reply("`Post Sent`", chat)
					elif reply_type=="document":
						utils.send_document(chat_group, reply_doc, reply_cap)
						reply("`Post Sent`", chat)
					elif reply_type=="voice":
						utils.send_voice(chat_group, reply_doc, reply_cap)
						reply("`Post Sent`", chat)
					elif reply_type=="audio":
						utils.send_audio(chat_group, reply_doc, reply_cap)
						reply("`Post Sent`", chat)
					else:
						reply("There is  `No Post`  to send.\n\nTo  `Send Post` , Click on  `Send Post to Subscribers`  for more details.",chat)
				elif text=="Songs":
					text1="Select an  `Album`  from here. Enjoy the  `Music`  🎶🎧🎵🎶."
					dreply(text1, chat, music.musickey, message_id)
				elif text=="Loading":
					text1="I'll show you a small loading sequence."
					reply(text1, chat, message_id=message_id)
					key = {
					"inline_keyboard": [
						[
							{"text": "Good", "callback_data": "Good"},
							{"text": "Ok", "callback_data": "Ok"}
						]
					]
					}
					utils.loading(chat, message_id+1, reply_markup=key)
				elif text=="Fi":
				    text1=reply_doc.replace("_","\_")
				    reply(text1, chat, keyboard, message_id)
				elif "m1" in text.lower() or "m2" in text.lower() or "m3" in text.lower() or "m4" in text.lower() or "m5" in text.lower() or "m6" in text.lower() or "m7" in text.lower() or "m8" in text.lower() or "m9" in text.lower() or "m10" in text.lower() or "m11" in text.lower() or "m12" in text.lower() or "m13" in text.lower() or "m14" in text.lower() or "m15" in text.lower():
					moviesend(text, chat, message_id)
				elif "movie" in text.lower():
					utils.reply("Select Movie Below", chat, message_id, movie.key)
				elif "history" in text.lower():
					key=replykey.key
					utils.reply("Please Enter the Password: ", chat, message_id, key)
				elif "pwr"==text.lower():
					key=replykey.key2
					utils.reply("Enter the New Password: ", chat, message_id, key)
				elif "feedback" in text.lower() or "feed" in text.lower() and "back" in text.lower():
					text1="Type your feedback here"
					dreply(text1, chat, {'force_reply':True}, message_id)
				else:
					analysis(text, chat, keyboard, message_id, mtype, date_today)
			elif update.__contains__("callback_query"):
				chat = update["callback_query"]["from"]["id"]
				first_name = update["callback_query"]["from"]["first_name"]
				if update["callback_query"].__contains__("game_short_name"):
				    print("game")
				    cqi = update["callback_query"]["id"]
				    url = "https://www.mathsisfun.com/games/2048.html"
				    utils.startgame(cqi, url)
				    break
				data = update["callback_query"]["data"]
				text = update["callback_query"]["message"]["text"]
				this_id = update["callback_query"]["message"]["message_id"]
				print(first_name)
				print(chat)
				print(data+"\n")
				open("password.txt", 'a').close()
				if data=="m1" or data=="m2" or data=="m3" or data=="m4" or data=="m5" or data=="m6" or data=="m7" or data=="m8" or data=="m9" or data=="m10" or data=="m11" or data=="m12" or data=="m13" or data=="m14" or data=="m15":
					name=movie.moviecheck(data)
					n=movie.names[name][5]
					utils.editkey(chat, this_id, "You have Selected:\n"+n+"\n\n"+"Select Quality", movie.sizekeyedit(data))
				elif data=="m0":
					utils.editkey(chat, this_id, "Select Movie Below", movie.key)
				elif "m1" in data or "m2" in data or "m3" in data or "m4" in data or "m5" in data or "m6" in data or "m7" in data or "m8" in data or "m9" in data or "m10" in data or "m11" in data or "m12" in data or "m13" in data or "m14" in data or "m15" in data:
					moviesend(data, chat)
				elif data=="news":
					r=google_func(text, 1)
					reply(r[0], chat)
				elif data=="pta":
					key=replykey.key
					utils.editkey(chat, this_id, "Please Enter the Password: ", key)
				elif "q1" in data or "q2" in data or "q3" in data or "q4" in data or "q5" in data or "q6" in data or "q7" in data or "q8" in data or "q9" in data or "q0" in data or "qt" in data or "qw" in data:
					pw.append(data)
					print(pw)
					print("\n")
					if data=="qt":
						with open ('password/'+str(chat)+'.txt', 'rb') as fp:
							try:
								pas = pickle.load(fp)
							except:
								utils.editkey(chat, this_id, 'It seems like you have not set any Password. \n\nPlease type "pwr" and set a Password.')
								pw.clear()
								break
						if pw==pas:
							print("Correct Password\n")
							utils.editkey(chat, this_id, "Correct Password")
							pw.clear()
							time.sleep(2)
							text1=str(int(int(utils.file_len("history/"+str(chat)+".txt"))/4))+" Messages till now."
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
							utils.editkey(chat, this_id, text1, clear)
						else:
							print("Wrong Pasword\n\n")
							ta = {
								"inline_keyboard": [
									[
										{"text": "Try Again", "callback_data": "pta"}
									]
								]
							}
							utils.editkey(chat, this_id, "Wrong Password", ta)
							pw.clear()
					elif data=="qw":
						pw.clear()
				elif data=="ch":
					open('history/'+str(chat)+'.txt', 'w').close()
					text1="0 Messages till now."
					utils.editkey(chat, this_id, text1)
				elif data=="gh":
					file='history/'+str(chat)+'.txt'
					r=utils.send_document_local(chat, file, "History")
					if r.__contains__("error_code"):
						if r['description']=='Bad Request: file must be non-empty':
							reply("The history is empty", chat)			   
				elif data=="clear":
					utils.editkey(chat, this_id, "🚫 𝘛𝘩𝘪𝘴 𝘮𝘦𝘴𝘴𝘢𝘨𝘦 𝘸𝘢𝘴 𝘥𝘦𝘭𝘦𝘵𝘦𝘥")
					time.sleep(3)
					delete(chat, this_id)
					delete(chat, this_id-1)
				elif "cs" in data:
					r="a"+data.replace("cs", "")
					utils.send_media(music.files[r], chat, "audio")		 		
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
						utils.editkey(chat, this_id, "Password Reset Successful")
					elif data=="rw":
						pwr.clear()
			elif update.__contains__("inline_query"):
			    chat = update["inline_query"]["from"]["id"]
			    first_name = update["inline_query"]["from"]["first_name"]
			    query = update["inline_query"]["query"]
			    iqi = update["inline_query"]["id"]
			    print(chat)
			    print(first_name)
			    print("query:", query)
			    query=query.lower()
			    if movie.names.__contains__(query):
			        results = []
			        mnq = movie.names[query]
			        for x in range(5):
			          if mnq[x]!="0":
			            results.append({ "type":"document", 
			             "id":x, 
			             "title":mnq[5],
			             "description":"\nSize: " + movie.msize(x),
			             "document_file_id": mnq[x]
			           })
			        print(utils.answerinline(iqi, results).json())
			    elif "game" in query:
			        results=[{ "type":"game", 
			             "id":100, 
			             "game_short_name":"test"
			           }]
			        print(utils.answerinline(iqi, results).json())
			else:
				break
		 
			
		except Exception as e:
			print(e)

def typecheck(update):
	if update["message"].__contains__("text"):									 
		mtype = "text"
	elif update["message"].__contains__("photo"):
		mtype = "photo"
	elif update["message"].__contains__("video"):
		mtype = "video"
	elif update["message"].__contains__("voice"):
		mtype = "voice"
	elif update["message"].__contains__("animation"):
		mtype = "animation"
	elif update["message"].__contains__("document"):
		mtype = "document"
	elif update["message"].__contains__("audio"):
		mtype = "audio"
	elif update["message"].__contains__("sticker"):
		mtype = "sticker"
	else:
		mtype = "other"
	return mtype

def moviesend(text, chat, message_id=None, doc_type="document"):
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
	if size=="a":
		lst=[]
		text1="Loading, please wait..."
		r=jreply(text1, chat)
		message_id = r["result"]["message_id"]
		#print(message_id)
		utils.loading(chat, message_id , "Here is your requested Movie.", skip=5)
		mcap=[]
		for x in range(0,5):
			if movie.names[name][x]!="0":
				lst.append(movie.names[name][x])
				ms=movie.msize(x)
				mn=movie.names[name][5]
				mc="@saikrishnakarnati "+mn+" "+ms+"\n✯ ━━━━━━━ ✧ ━━━━━━━━ ✯\nhttps://t.me/saikrishnakarnati"
				mcap.append(mc)
			else:
				pass
		try:
			movie.names[name][6]
			doc_type="video"
		except:
			pass
		utils.send_media(lst, chat, doc_type, caption=mcap, parse_mode="")
	elif size==5:
		reply("`Quality Not Found.` \n\nPlease try another  `Quality` .", chat, message_id=message_id)
	else:
		if movie.names[name][size]!="0":
			file_id=movie.names[name][size]
			text1="Loading, please wait..."
			r=jreply(text1, chat)
			message_id = r["result"]["message_id"]
			utils.loading(chat, message_id , "Here is your requested Movie.", skip=5)
			mn=movie.names[name][5]
			ms=movie.msize(size)
			mc="@saikrishnakarnati "+mn+" "+ms+"\n✯ ━━━━━━━ ✧ ━━━━━━━━ ✯\nhttps://t.me/saikrishnakarnati"
			try:
				movie.names[name][6]
				doc_type="video"
			except:
				pass
			if doc_type=="document":
				utils.send_document(chat, file_id, mc, parse_mode="")
			else:
				utils.send_video(chat, file_id, mc, parse_mode="")
		else:
			reply("`Quality Not Found.` \n\nPlease try another  `Quality` .", chat)

def power(x,y):
	z=float(x)**float(y)
	if "e" in str(z):
		z0=precision_round(z)
		ans=str(z0).replace('e',' × 10^').replace('+','')
		return ans
	return z
 
def google_func(q, n):
	l=[]
	for i in search(query=q,tld='co.in',num=10,stop=n,pause=1):
		l.append(i.replace("_", r"\_"))
	return l
	 
def precision_round(number, digits=3):
	power = "{:e}".format(number).split('e')[1]
	return round(number, -(int(power) - digits))

def build_keyboard(items):
	keyboard = [[item] for item in items]
	reply_markup = {"keyboard":keyboard, "one_time_keyboard": False}
	return json.dumps(reply_markup)

def long_keyboard(keyboard):
	reply_markup = {"keyboard":keyboard, "one_time_keyboard": False, "resize_keyboard": True}
	return json.dumps(reply_markup)

def delete(chat_id, message_id):
	url = URL + "deleteMessage?chat_id={}&message_id={}".format(chat_id, message_id)
	r=requests.get(url)
	return r

def clearchat(chat_id, message_id):
	print ("Deleting messages")
	id=message_id-49
	for x in range(id, message_id):
		delete(chat_id, x)
	print("Deleted\n")

def reply(text, chat_id, reply_markup=None, message_id=None):
	text = urllib.parse.quote_plus(text)
	url = URL + "sendMessage?text={}&chat_id={}&reply_to_message_id={}&parse_mode=Markdown".format(text, chat_id, message_id)
	if reply_markup:
		url+="&reply_markup={}".format(reply_markup)
	c = get_url(url)
	return c

def dreply(text, chat_id, reply_markup=None, message_id=None):
	text = urllib.parse.quote_plus(text)
	url = URL + "sendMessage?text={}&chat_id={}&reply_to_message_id={}&parse_mode=Markdown".format(text, chat_id, message_id)
	if reply_markup:
		reply_markup=json.dumps(reply_markup)
		url+="&reply_markup={}".format(reply_markup)
	c = get_url(url)
	return c
	
def qreply(text, chat_id, reply_markup=None, message_id=None):
	url = URL + "sendMessage?text={}&chat_id={}&reply_to_message_id={}&parse_mode=Markdown".format(text, chat_id, message_id)
	if reply_markup:
		url+="&reply_markup={}".format(reply_markup)
	get_url(url)

def jreply(text, chat_id):
	text = urllib.parse.quote_plus(text)
	url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
	c = requests.get(url)
	return c.json()
  
def main():
	last_update_id = None
	while True:
		#print("Updating...")
		updates = get_updates(last_update_id)
		if len(updates["result"]) > 0:
			last_update_id = get_last_update_id(updates) + 1
			echo_all(updates)
		time.sleep(0.5)
		
def analysis (text, chat, keyboard, message_id, type, date_today):
	try:
		if "hi"==text.lower() or "hello"==text.lower() or "namaste"==text.lower() or "hola"==text.lower():
			cap=random.choice(['Hello, Welcome', 'Hello there!', 'Hey there!', 'Namaste!', 'Hola!'])
			utils.send_photo(chat,"AgACAgUAAxkBAAIW5GAYKe-8aJNp-mhNtFzek-Mi3etOAAL8qjEbQhXAVNDJLOCBAvlQUZtccXQAAwEAAwIAA20AA7MQAAIeBA",cap, message_id)
			reply("Hope you're doing well.", chat, keyboard)
		elif "website" in text.lower() or "site" in text.lower():
			cap="Checkout our Website: \nhttps://saikrishna.epizy.com/form.\n\nAny Suggestions are Welcomed. \nSubmit your Suggestions in our Website."
			web = {
					"inline_keyboard": [
						[
							{"text": "Website", "url": "saikrishna.epizy.com/form"},
							{"text": "Suggestions", "url": "saikrishna.epizy.com/form/index-services.html"}
						]
					]
					}
			text1=""
			utils.send_photo(chat,"AgACAgUAAxkBAAIW22AYKPHVugHFO6vFtQWP62MWOTcMAAL3qjEbQhXAVP9yv__eMTgc59T-bnQAAwEAAwIAA20AA1sQAAIeBA",cap, message_id, web)
			reply(text1, chat, keyboard)
		elif "/start" in text.lower():
			text1="Hello, my name is ChatBot\nMade using Python\nMade by Sai Krishna\nI'm a ChatBot"
			reply(text1, chat, keyboard, message_id)
		elif "clear" in text.lower():
			text1="Deleting Messages..."
			reply(text1, chat, keyboard)
			clearchat(chat, message_id+2)
		elif "what" in text.lower() and "you" in text.lower() and "do" in text.lower() or "what" in text.lower() and "u" in text.lower() and "do" in text.lower() or "wt" in text.lower() and "you" in text.lower() and "do" in text.lower() or "wt" in text.lower() and "u" in text.lower() and "do" in text.lower():
			text1="I can answer you some basic questions. Test me now. Send your suggestions to our Website or Personally. Type 'Website' for more."
			reply(text1, chat, keyboard, message_id)
		elif "who" in text.lower() and "you" in text.lower() or "who" in text.lower() and "u" in text.lower():
			text1="Hi, I'm a ChatBot 🤖🤖. I can answer you some basic questions. Test me now. Send your suggestions to our Website or Personally. Type 'Website' for more."
			reply(text1, chat, keyboard, message_id)
		elif "how are you" in text.lower() or "how" in text.lower() and "doing" in text.lower() or "how" in text.lower() and "do" in text.lower() or "how" in text.lower() and "dng" in text.lower():
			text1="I'm fine, Thanks. Hoping same from you"
			reply(text1, chat, keyboard, message_id)
		elif "fine" in text.lower():
			text1="Good to know"
			reply(text1, chat, keyboard, message_id)
		elif "doubt" in text.lower():
			text1="Ask my Owner @saikrishna7004"
			reply(text1, chat, keyboard, message_id)
		elif "media" in text.lower():
			text1=f"You have sent a  `{str(type).title()}`."
			reply(text1, chat, keyboard, message_id)
		elif "send post to subscribers" in text.lower():
			text1="To `Send Post` to Subscribers: \n\n`Step1:` Send your `File` or `Media` to this `ChatBot`. \n\n`Step2:` `Reply` to the `File` or `Media` saying `Send Post`. \n\nOnly for `Admins`."
			reply(text1, chat, keyboard, message_id)
		elif "calendar" in text.lower() or "calender" in text.lower():
			d=str(date_today).split("-")
			text1="`"+calendar.month(int(d[0]), int(d[1]))+"`"
			print(text1.replace("`",""))
			reply(text1, chat, keyboard, message_id)
		elif "news" in text.lower():
			result=news.newsapi()
			t=result[0]
			d=result[1]
			u=result[2]
			for i in range(0,len(t)):
				key= {
					"inline_keyboard": [
						[
							{"text": "Read Full", "url": u[i]}
						]
					]
					}
				utils.reply(t[i]+"\n\n"+d[i], chat, reply_markup=key)
			qreply("👍", chat, keyboard, message_id)
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
			reply(text1, chat, keyboard, message_id)
		elif "thank" in text.lower():
			text1="It's my Pleasure 😃."
			reply(text1, chat, keyboard, message_id)
		elif "bye" in text.lower() or "see you" in text.lower() or "tata" in text.lower():
			text1="Good bye 👋. \nHope you return soon."
			reply(text1, chat, keyboard, message_id)
		elif "help" in text.lower() or "/help" in text.lower():
			text2="Hello, I'm a ChatBot🤖🤖. \nYou can chat with me.\nIf I don't know something, I'll search it in Google.\n\n"+"Contact my owner for more details in our Website. \nType or Click on 'Website' for more."
			text1="Here are some commands I can do: \n\nHi, Hello, Namaste, Hola\nWebsite, Site, Web\nHow r u\nI'm fine\nWho r u\nSolve somequestion\nSolve power(x,y) => It gives x^y \nLoading \nSongs \nMovies \nHistory \nPwr \nCalender \nBye \n\n"
			reply(text2, chat, keyboard, message_id)
			reply(text1, chat, keyboard)
		elif "search" in text.lower():
			if text.lower().replace('search','').strip()!="":
				ans=google_func(text.lower().replace('search','').strip(),5)
				for x in ans:
					reply(x,chat)  
				text1=""
			else:
				text1="Type what you want to Search. Type 'Search' and add your search keywords to search."
			reply(text1, chat, keyboard, message_id)
		elif "inline" in text.lower():
		    pass
		else:
			text1="👍"
			text2="You said: "+text+". I'm searching in google. Please wait..."
			reply(text2, chat, keyboard)
			ans = google_func(text, 5)
			for x in ans:
				reply(x, chat)
			reply(text1, chat, keyboard, message_id)
	except Exception as e:
		print(e)
  
if __name__ == '__main__':
	main()