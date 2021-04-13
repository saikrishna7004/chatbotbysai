import pytube
def you(link):
	yt = pytube.YouTube(link)
	print(yt)
	stream = yt.streams[5]
	print(stream)
	print(stream.download("youtube"))
	return yt.title
if __name__=="__main__":
	you("https://youtu.be/oK_rLUl2_8w")