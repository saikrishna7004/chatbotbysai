import pytube
def you(link):
	yt = pytube.YouTube(link)
	print(yt)
	stream = yt.streams.filter(res="144p", mime_type="video/mp4")[0]
	print(stream)
	print(stream.download("youtube","temp"))
	return yt.title
if __name__=="__main__":
	you("https://youtu.be/oK_rLUl2_8w")
