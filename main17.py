from pytube import YouTube

#todo: 1) Get video like, 2) Where to save? 3) Create Youtube oject 4) Download the Video

#Video link
link = "https://www.youtube.com/watch?v=bgBKEr5BYbw"

savePath = "E:\$PYTHON$"

try:

    # Youtube object Creating
    youTubeObject = YouTube(link)
    print(youTubeObject.title)
    print(youTubeObject.description)
    print(youTubeObject.streams)

    # cHECKING STREAMS
    for x in youTubeObject.streams.filter(only_video=True):
        print(x)

    #getting the needed stream
    youtubeStream = youTubeObject.streams.get_highest_resolution()

#Doenloading video
    youtubeStream.download(savePath)


except Exception as e:
    print("Error"+str(e))