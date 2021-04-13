import pytube
def you(link):
	yt = pytube.YouTube(link)
	print(yt)
	stream = yt.streams.filter(res="144p", mime_type="video/mp4")[0]
	print(stream)
	try:
		fil=open("temp.mp4","rb")
		temptext=fil.read()
		if temptext=="":
			filed="temp"
		else:
			filed="temp1"
	except:
		open("temp.mp4","wb").close()
		filed="temp"
	
	print(stream.download("youtube",filed))
	return filed
if __name__=="__main__":
	you("https://youtu.be/oK_rLUl2_8w")