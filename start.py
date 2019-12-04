#from pytube import YouTube
# 특정영상 다운로드
#YouTube('https://youtube.com/watch?v=9bZkp7q19f0').streams.first().download()

from pytube import YouTube

# yt = YouTube('https://www.youtube.com/watch?v=mhfp6Z8z1cI').streams.all()
# for i in yt:
#     print(i)

u_list = [
    'https://www.youtube.com/watch?v=WW2vcbBkyRk&list=WL',
    'https://www.youtube.com/watch?v=Boz6QhrxE8E&list=WL&index=2&t=0s',
    'https://www.youtube.com/watch?v=xHCFLeei5Wg&list=WL&index=3',
    'https://www.youtube.com/watch?v=9bZkp7q19f0&list=WL&index=4',
    'https://www.youtube.com/watch?v=Ngyjoe86hPg&list=WL&index=5',
    'https://www.youtube.com/watch?v=MPX-ojIEbDI&list=WL&index=7'
]
for u in u_list:
    yt = YouTube(u)

    print("영상 제목 : ", yt.title)
    # 에러남
    # print("영상 길이 : ", yt.length)
    # print("영상 평점 : ", yt.rating)
    # print("영상 썸네일 링크 : ", yt.thumbnail_url)
    # print("영상 조회수 : ", yt.views)
    #print("영상 설명 : ", yt.description)
    yt.streams\
        .filter(progressive=True, file_extension='mp4')\
        .order_by('resolution')\
        .desc()\
        .first().download('./video')
    # yt.init()
    print("다운로드 완료")

#유튜브 전용 인스턴스 생성
# yt = YouTube('https://youtube.com/watch?v=9bZkp7q19f0')
# # print(yt.streams.filter(only_audio=True).all())
# # 특정영상 다운로드
# yt.streams.filter(only_audio=True).first().download('./audio')
print('완료')
