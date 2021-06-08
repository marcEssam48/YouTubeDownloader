import os
def RestoreData(video,embedlink):
    count = int(GetNumber()) + 1
    WriteCounts(count)
    with open("DownLoader/LOGS/Users_Videos.txt","a") as file:
        file.write(str(count) + ". " + str(embedlink) + " | " + str(video.username) + " | " + str(video.author) )
        file.write("\n")
        file.write("######################################################################################################")
        file.write("\n")
        file.write("\n")
        file.close()


def GetNumber():
    with open("DownLoader/LOGS/counts","r") as file:
        count = file.read()
        file.close()
    return count

def WriteCounts(count):
    with open("DownLoader/LOGS/counts","w") as file:
        file.write(str(count))
        file.close()


