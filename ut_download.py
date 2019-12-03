from pytube import YouTube
from tkinter import filedialog
from tkinter import *
import subprocess
import os


# 다운로드 현황 체크를 위한 함수 -> YouTube 객체 콜백함수로 들어감
def progress_bar(stream=None, chunk=None, file_handle=None, remaining=None):
    progress = (100 * (100000 - remaining)) / 100000
    print(title + "... : {:00.0f}% downloaded".format(progress), end='\r')


def file_path_select():
    root = Tk()  # GUI로 파일경로를 선택하기위해 tkinter 라는 라이브러리 사용
    root.dirName = filedialog.askdirectory()  # GUI로 파일경로 선택창이 나옴
    down_path = root.dirName
    root.destroy()  # gui 창 닫기
    return down_path


def video_len_ms(length):
    m, s = divmod(int(length), 60)  # length 분,초로 표시하기(60으로 나눈 몫과 나머지 출력)
    return m, s


def get_stream_by_itag(streams):
    while True:
        print(" \"itag\"를 이용해 특정 stream 선택(위 목록에서 itag를 선택하세요) :")
        itag = input()
        try:
            my_stream = streams.get_by_itag(itag)
            break
        except:
            print("ERROR / 유효한 itag가 아님.")
            continue
    return my_stream


def download_stream(stream, path, index):
    filename = ["_video", "_audio"]
    stream.download(path, filename[index])
    print("")


def yt_info(yt):
    print("{} 를 다운 받습니다. : ".format(yt.title))
    global title
    title = yt.title


def st_info(stl):
    for item in stl:
        print("선택된 stream : ", item)


# 코드출처 https://seolin.tistory.com/104
def ffmpeg_mix(path, _title):
    _title = _title.replace('/', '_')
    _title = _title.replace('\"', '-')
    _title = _title.replace("\'", '-')
    _title = "/" + _title + ".mp4"
    result = subprocess.Popen(["ffmpeg", "-i", path + "/_video.mp4", "-i", path + "/_audio.mp4", path + _title])
    # stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Filename에 replace가 들어가는 이유는 "/" 문자가 들어갈 경우 파일이름이 아니라 디렉토리로 인식하기 떄문입니다. replace없이 바로 집어넣을 경우 문제가 발생합니다.
    out, err = result.communicate()
    exitcode = result.returncode
    if exitcode != 0:
        print(exitcode, out.decode('utf8'), err.decode('utf8'))
    else:
        print('Completed')


def main():
    while True:
        print("다운받을 유튜브 영상 링크를 입력하세요")
        print("종료하시려면 q 를 입력하세요")
        yt_link = input().rstrip()
        if yt_link == 'q':
            break

        print("접속중,,,")
        try:
            yt = YouTube(yt_link, on_progress_callback=progress_bar)
        except:
            print("ERROR / 유효한 링크가 아님.")
            continue

        yt_info(yt)

        print("Stream 목록 :")
        for i, stream in enumerate(yt.streams.filter(adaptive=True, file_extension='mp4').all()):
            if str(stream).find("res=\"None\"") == -1:
                print(i + 1, " : ", stream)
        my_stream = get_stream_by_itag(yt.streams)
        my_audio_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).first()
        st_list = [my_stream, my_audio_stream]
        st_info(st_list)

        print("다운로드 경로 지정 : ", end="")
        down_path = file_path_select()
        print(down_path)

        print("해당 경로에 선택된 stream 다운로드 시작")
        for i, stream in enumerate(st_list):
            download_stream(stream, down_path, i)
        print("\n저장 완료 ffmpeg 합성 시작\n")
        ffmpeg_mix(down_path, yt.title)


if __name__ == "__main__":
    main()

# 설운도	https://www.youtube.com/watch?v=WW2vcbBkyRk&list=WL
# 김건모	https://www.youtube.com/watch?v=Boz6QhrxE8E&list=WL
# 홍진영	https://www.youtube.com/watch?v=xHCFLeei5Wg&list=WL
# 싸이	https://www.youtube.com/watch?v=9bZkp7q19f0&list=WL
# 터보	https://www.youtube.com/watch?v=Ngyjoe86hPg&list=WL
# 깅연자	https://www.youtube.com/watch?v=MPX-ojIEbDI&list=WL