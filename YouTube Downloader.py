"""
Welcome to the simplest youtube videos And playlists downloader
By: Yousef Jarbou
"""
from pytube import YouTube
from pytube import Playlist

print("Salam! Welcome to Yousef's YouTube downloader ^_^")
print('Enter v if you want to download one video')
print('Enter p if you want to download a playlist')


def single(url):
    vv=False
    try:
        video_caller=YouTube(url)
        vv=True
    except:
        print('\nops !!!\ninvalid URL!!!')
        vv=False

    if vv==True:
        try:
            # video_caller.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download('Downloads')
            print('Choose the resolution, Highest=h, Lowest=l')
            q=input('H/L?:')
            print('this my take sometime, leave it and it will work InshaaAllah!')
            print(video_caller.title)
            print('is downloading...')
            if(q=='h' or q=='H'):
                highest_resolution_stream=video_caller.streams.get_highest_resolution()
                highest_resolution_stream.download('Downloads')
            elif(q=='l' or q=='L'):
                lowest=video_caller.streams.get_lowest_resolution()
                lowest.download('Downloads')
            print("Done!!")
        except:
            print('\nops !!!\nError!!!')


def play(url):
    vv=False
    try:
        playlist=Playlist(url)

        print('Number of videos in playlist: %s'%len(playlist.video_urls))
        pl=len(playlist.video_urls)
        vv=True
    except:
        print('\nops !!!\ninvalid URL!!!')

    if vv:
        try:
            print(f'Choose the resolution for all {pl} videos, Highest=h, Lowest=l')
            q=input('H/L?:')

            print('this my take sometime, leave it and it will work InshaaAllah!')
            i=1
            if(q=='h' or q=='H'):
                for video in playlist.videos:
                    print(video.title)
                    print('is downloading...')
                    # video.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download('Downloads')
                    highest_resolution_stream=video.streams.get_highest_resolution()
                    highest_resolution_stream.download('Downloads')

                    print(f'{i}/{pl} Done')
                    i+=1
            elif(q=='l' or q=='L'):
                for video in playlist.videos:
                    print(video.title)
                    print('is downloading...')
                    # video.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download('Downloads')
                    lowest=video.streams.get_lowest_resolution()
                    lowest.download('Downloads')

                    print(f'{i}/{pl} Done')
                    i+=1
            print("Done!!")
        except:
            print('\nops !!!\nError!!!')


x=input('v/p?')
if(x=='v' or x=='V'):
    print('Ready to download one single video')
    u=input('Paste the URL here please:')
    single(u)

elif (x=='p' or x=='P'):
    print('Ready to download all playlist videos!')
    u=input('Paste Playlist URL here please:')
    play(u)

else:
    print(f'wrong input, i asked for v or p... sorry you entered {x}')

