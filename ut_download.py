import os
import subprocess

import pytube

yt = pytube.YouTube("https://www.youtube.com/watch?v=9bZkp7q19f0") #다운받을 동영상 URL 지정

vids= yt.streams.all()

#영상 형식 리스트 확인
for i in range(len(vids)):
    print(i,'. ',vids[i])

vnum = int(input("다운 받을 화질은? "))
#저장 경로 지정(Windows or mac)
parent_dir = "./"
vids[vnum].download(parent_dir) #다운로드 수행

new_filename = input("변환 할 mp3 파일명은?")

default_filename = vids[vnum].default_filename 
#cmd 명령어 수행
subprocess.call(['ffmpeg', '-i',
    os.path.join(parent_dir, default_filename),
    os.path.join(parent_dir, new_filename)
])

print('동영상 다운로드 및 mp3 변환 완료!')
