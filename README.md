# fly-ai-project-video-to-clip

## 폴더 설명
- "원본동영상" 폴더 : 엑셀 파일에 올려둔 아기 동영상(2~48번)을 모두 다운로드하여 모아둔 폴더
- "클립동영상" 폴더 : 원본동영상의 모든 영상들을 1초 간격의 클립으로 잘라 모아둔 폴더
    - 이름명 규칙 : {원본동영상 이름}-1, {원본동영상 이름}-2, ...
- "테스트용" 폴더 : 무시하세요

## 사용 환경
Python 3.10.11<br>
opencv-python, moviepy 모듈 필요
```
pip install opencv-python
pip install moviepy
```

## 사용 방법
```
git clone https://github.com/SeoyoungOhMe/fly-ai-project-video-to-clip.git
```

- 클립동영상을 그대로 다운로드 받아 사용하거나, video-cut.py를 실행하여 클립동영상을 직접 만들 수도 있음.
- 필요 시 다음의 코드 실행 :
```
python video-cut.py
```

