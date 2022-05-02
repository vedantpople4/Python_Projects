from pytube import YouTube

def video(yt):
    print('Title: ', yt.title)
    print('Total Length: ', yt.length, ' seconds')
    print('Total Views: ', yt.views)
    print('Video Rating: ', yt.rating)
    print('Thumbnail URL: ', yt.thumbnail_url)

link = "https://www.youtube.com/watch?v=k2aeH0xPMew"
yt = YouTube(link)

video(yt)