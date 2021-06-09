from django.shortcuts import render
from django.shortcuts import render, redirect
#pytub package for download youtube video
from pytube import YouTube
import os
from django.http import FileResponse
import pafy
from django.conf import settings
import psycopg2
from datetime import datetime
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

dbHost = settings.DATABASES['default']['HOST']
dbUsername = settings.DATABASES['default']['USER']
dbPassword = settings.DATABASES['default']['PASSWORD']
dbName = settings.DATABASES['default']['NAME']
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
            local_dt = datetime.now()
            sql = 'INSERT INTO public."DownLoader_links"( link, auther, "VideoName" , date_download)VALUES ('
            sql+= "'"+str(embedlink)+"','"+str(video.author)+"','"+str(video.username)+"','"+str(local_dt)+"');"
            print(sql)
            connection = psycopg2.connect(user=dbUsername,
                                          password=dbPassword,
                                          host=dbHost,
                                          database=dbName)
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            result = cursor.fetchall()
            # print(result)

            # count = int(sc.GetNumber()) + 1
            # sc.WriteCounts(count)
            # with open("DownLoader/LOGS/Users_Videos.txt", "a") as file:
            #     file.write(str(count) + ". " + str(embedlink) + " | " + str(video.username) + " | " + str(video.author))
            #     file.write("\n")
            #     file.write("######################################################################################################")
            #     file.write("\n")
            #     file.write("\n")
            #     file.close()
        except Exception  as e:
            print(e)

            # sc.RestoreData(video,embedlink)

        return render(request, 'Downloader.html', context)
    return render(request, 'Downloader.html')

