#from pytube import YouTube
# 특정영상 다운로드
#YouTube('https://youtube.com/watch?v=9bZkp7q19f0').streams.first().download()

from pytube import YouTube

# yt = YouTube('https://www.youtube.com/watch?v=mhfp6Z8z1cI').streams.all()
# for i in yt:
#     print(i)
# YouTube('https://youtube.com/watch?v=9bZkp7q19f0').streams.first().download('./video')

#유튜브 전용 인스턴스 생성
yt = YouTube('https://youtube.com/watch?v=9bZkp7q19f0')
# print(yt.streams.filter(only_audio=True).all())
# 특정영상 다운로드
yt.streams.filter(only_audio=True).first().download('./audio')
print('완료')
