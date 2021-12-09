from pytube import Playlist

def video(yt):
    print(yt.title)
    for video in yt.videos:
        try:
            video.streams.first().download(video.title)
        except Exception as e:
            print(e, type(e))
    print("Playlist is Download")

link=""
p = Playlist(link)
video(p)