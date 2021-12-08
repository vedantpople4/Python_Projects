from pytube import YouTube

def audio(yt):
    my_streams = yt.streams.filter(only_audio = True)
    for streams in my_streams:
        print(f"Audio itag : {streams.itag} Quality : {streams.abr} ")

    input_itag = input("Enter itag value: ")
    audio = yt.streams.get_by_itag(input_itag)

    audio.download()
    print("Audio is downloading as ", yt.title+".mp4")

link = "https://www.youtube.com/watch?v=WGQF0XYxE2U"
yt = YouTube(link)
audio(yt)