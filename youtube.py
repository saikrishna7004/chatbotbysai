import pytube, subprocess

def you(link):
	yt = pytube.YouTube(link)
	print(yt)
	print(yt.title)
	stream = yt.streams.filter(abr="50kbps", type="audio")[0]
	stream1=yt.streams.filter(res="144p")[0]
	print(stream)
	print(stream1)
	print(stream.download("youtube","temp"))
	print(stream.download("youtube","temp1"))
	combine_audio('./youtube/temp.webm', './youtube/temp1.mp4', './youtube/temp2.mp4')
	return "temp2"

def combine_audio(inpaud, inpvid, outp):
	
	#import ffmpeg

	#input_video = ffmpeg.input(inpvid)

	#input_audio = ffmpeg.input(inpaud)

	#ffmpeg.concat(input_video, input_audio, v=1, a=1).output(outp).run()
	
	cmd = 'ffmpeg -y -i '+inpaud+'  -r 30 -i '+inpvid+'  -filter:a aresample=async=1 -c:a flac -c:v copy '+outp
	subprocess.call(cmd, shell=True)

if __name__=="__main__":
	
	you("https://youtu.be/KS6XeRkN_us")
	
