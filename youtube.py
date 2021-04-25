import pytube, shutil

def you(link):
	yt = pytube.YouTube(link)
	print(yt)
	print(yt.title)
	stream = yt.streams.filter(abr="50kbps", type="audio")[0]
	stream1=yt.streams.filter(res="144p")[0]
	print(stream)
	print(stream1)
	print(stream.download("youtube","temp"))
	print(stream1.download("youtube","temp1"))
	shutil.copy('youtube/temp.webm', 'youtube/audio.mp3')
	try:
		shutil.copy('youtube/temp1.webm', 'youtube/video.mp4')
	except:
		shutil.copy('youtube/temp1.mp4', 'youtube/video.mp4')
	combine_audio('./youtube/audio.mp3', './youtube/video.mp4', './youtube/temp2.mp4')
	return "temp2.mp4"

def combine_audio(inpaud, inpvid, outp):
	#import ffmpeg
	#input_video = ffmpeg.input(inpvid)
	#input_audio = ffmpeg.input(inpaud)
	#ffmpeg.concat(input_video, input_audio, v=1, a=1).output(outp).run()
	import os
	cmd = "ffmpeg -i "+inpvid+" -i "+inpaud+"^ -c copy "+outp
	os.system(cmd)

if __name__=="__main__":
	
	you("http://www.youtube.com/watch?v=9RTaIpVuTqE")
