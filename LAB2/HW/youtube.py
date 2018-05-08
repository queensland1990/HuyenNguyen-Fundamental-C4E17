from youtube_dl import YoutubeDL

#sample 1: download a singl youtube video
# dl=YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=WHK5p7JL7g4'])
# print(dl)

#sample 2: download multiple youtube video
# dl=YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=wNVIn-QS4DE', 'https://www.youtube.com/watch?v=JZjRrg2rpic'])
# print(dl)

# sample 3: Download audio
options={
'format':"bestaudio/audio"
}
dl=YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=CIJrGH5TFjY'])
print(dl)

#sample 4: search and download the first videoOffset
# options={
#     'default_search':'ytsearch',
#     'max_dowloads': 1
# }
# dl=YoutubeDL(options)
# dl.download(["shape of my heart","backstreetboys"])
# print(dl)

#Sample 5: search and download the first audio
options={
    'default_search':"ytsearch",
    'max_dowloads': 1,
    "format":"bestaudio/audio"
}

dl=YoutubeDL(options)
dl.download(["shape of my heart backstreetboys"])
