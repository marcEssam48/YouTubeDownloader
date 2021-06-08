import pytube
def DownloadFunction(link,Flag):
    try:
        yt = pytube.YouTube(link)
        if Flag == "A":
            stream = yt.streams.filter(only_audio=True).all()
            stream[0].download()
        elif Flag == "V":
            stream = yt.streams.first()
            stream.download("/Downloads")
    except:
        DownloadFunction(link, Flag)
    return "Downloaded"