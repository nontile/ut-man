import os
import subprocess
import pytube

# 설운도	https://www.youtube.com/watch?v=WW2vcbBkyRk&list=WL
# 김건모	https://www.youtube.com/watch?v=Boz6QhrxE8E&list=WL&index=2&t=0s
# 홍진영	https://www.youtube.com/watch?v=xHCFLeei5Wg&list=WL&index=3
# 싸이	https://www.youtube.com/watch?v=9bZkp7q19f0&list=WL&index=4
# 터보	https://www.youtube.com/watch?v=Ngyjoe86hPg&list=WL&index=5
# 깅연자	https://www.youtube.com/watch?v=MPX-ojIEbDI&list=WL&index=7
target = "https://www.youtube.com/watch?v=WW2vcbBkyRk&list=WL"
yt = pytube.YouTube(target)
vids = yt.streams.all()

for i in range(len(vids)):
    print("번호 {} - {}".format(i, vids[i]))

vnum = int(input("번호선택: "))
parent_dir = "D:\\workspaces\\download\\"
new_name = input("파일명 입력: ") 
org_name = vids[vnum].default_filename
subprocess.call(['ffmpeg', '-i',
                 os.path.join(parent_dir, org_name),
                 os.path.join(parent_dir, new_name)
                 ])
print("완료")
