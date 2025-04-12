import requests
import os
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip
from dotenv import load_dotenv

load_dotenv()

# Настройки
PIXABAY_API_KEY = os.getenv("PIXABAY_API_KEY")
search_query = 'scuba diver'
per_page = 3
logo_path = 'ironeagl(40x40).png'


def download_pixabay_videos(query, per_page=3):
    url = 'https://pixabay.com/api/videos/'
    params = {
        'key': PIXABAY_API_KEY,
        'q': query,
        'per_page': per_page,
        'safesearch': 'true'
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        videos = response.json()['hits']
        video_paths = []
        for idx, video in enumerate(videos):
            video_files = video['videos']
            video_url = video_files.get('large', video_files.get('medium', video_files['small']))['url']

            video_response = requests.get(video_url)
            video_filename = f'video_{idx}.mp4'
            with open(video_filename, 'wb') as f:
                f.write(video_response.content)
            video_paths.append(video_filename)
        return video_paths
    else:
        print(f'Ошибка API: {response.status_code}')
        return []


def overlay_logo_on_video(video_path, logo_path, output_path):
    video_clip = VideoFileClip(video_path)
    if video_clip.audio is None:
        video_clip = video_clip.set_audio(None)

    logo = (ImageClip(logo_path)
            .set_duration(video_clip.duration)
            .resize(height=100)
            .margin(right=8, top=8, opacity=0)
            .set_pos(("right", "top")))

    final_video = CompositeVideoClip([video_clip, logo])
    final_video.write_videofile(output_path, codec='libx264', audio_codec='aac')
    video_clip.close()
    final_video.close()


if __name__ == '__main__':
    video_paths = download_pixabay_videos(search_query, per_page)
    if video_paths:
        for video_path in video_paths:
            output_path = f'logo_{video_path}'
            overlay_logo_on_video(video_path, logo_path, output_path)
            print(f'Создано: {output_path}')
    else:
        print('Видео не загружены')