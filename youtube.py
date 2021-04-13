import pytube
def you(link):
	yt = pytube.YouTube(link)
	print(yt)
	stream = yt.streams.filter(progressive=True, res="360p")[0]
	print(stream)
	try:
		fil=open("youtube/temp.mp4","rb")
		temptext=fil.read()
		if temptext=="":
			filed="temp"
		else:
			filed="temp1"
	except:
		open("youtube/temp.mp4","wb").close()
		filed="temp"
	
	print(stream.download("youtube",filed))
	return filed
if __name__=="__main__":
	you("https://youtu.be/h9Am4CYaLng")