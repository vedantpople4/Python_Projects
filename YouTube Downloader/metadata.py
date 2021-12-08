from pytube import YouTube

def video(yt):
    print('Title: ', yt.title)
    print('Total Length: ', yt.length, ' seconds')
    print('Total Views: ', yt.views)
    print('Video Rating: ', round(yt.rating))
    print('Thumbnail URL: ', yt.thumbnail_url)

link = "https://www.youtube.com/watch?v=WGQF0XYxE2U"
yt = YouTube(link)

video(yt)