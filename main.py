from pytube import YouTube


def main(video_id: str):
    link = f"https://www.youtube.com/watch?v={video_id}"
    yt = YouTube(link)

    print("Title: ", yt.title)
    print("View: ", yt.views)
    print("Author: ", yt.author)
    print("Channel: ", yt.channel_url)

    yd = yt.streams.get_highest_resolution()
    yd.download('./YTfolder')

if __name__ == '__main__':
    video_id = input("What's the video id ?")
    main(video_id)
