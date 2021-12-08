from pytube import YouTube

def video(yt):
    my_streams = yt.streams.filter(file_extension = 'mp4' , only_video = True)
    for streams in my_streams:
        print(f"Video itag : {streams.itag} Resolution : {streams.resolution}")

    input_tag = input("Enter the Tag Value: ")
    video = yt.streams.get_by_itag(input_tag)
    video.download()
    print("Video is downloading as ", yt.title + ".mp")

link = "https://www.youtube.com/watch?v=WGQF0XYxE2U"
yt = YouTube(link)
video(yt)