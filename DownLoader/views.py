from django.shortcuts import render
from django.shortcuts import render, redirect
#pytub package for download youtube video
from pytube import YouTube
import os
from django.http import FileResponse
import pafy
import DownLoader.Scrapping as sc
# def index(request):
#     return render(request,"Downloader.html")
#
# def Downloading(request):
#     link = request.POST["link"]
#     Flag = request.POST["flag"]
#     # DFD.DownloadFunction(link,Flag)
#     video = pafy.new(link)
#     embedlink = link.replace("watch?v=", "embed/")
#     context = {
#         'yobj': video,
#         'embedlink': embedlink,
#     }
#     return render(request,"Downloader.html")

def ytb_down(request):
    if request.method == 'POST':
        url = request.POST.get('ylink')
        video = pafy.new(url)
        embedlink = url.replace("watch?v=", "embed/")
        context = {
            'yobj': video,
            'embedlink': embedlink,
        }
        try:
            count = int(sc.GetNumber()) + 1
            sc.WriteCounts(count)
            with open("DownLoader/LOGS/Users_Videos.txt", "a") as file:
                file.write(str(count) + ". " + str(embedlink) + " | " + str(video.username) + " | " + str(video.author))
                file.write("\n")
                file.write(
                    "######################################################################################################")
                file.write("\n")
                file.write("\n")
                file.close()
        except:
            print("0")

            # sc.RestoreData(video,embedlink)

        return render(request, 'Downloader.html', context)
    return render(request, 'Downloader.html')

