from PIL import Image

# Если константа ANTIALIAS отсутствует (что характерно для Pillow 10+),
# задаём её как эквивалент Image.Resampling.LANCZOS.
if not hasattr(Image, 'ANTIALIAS'):
    Image.ANTIALIAS = Image.Resampling.LANCZOS

from moviepy.editor import VideoFileClip, clips_array

# Настройки
video_paths = ['video_0.mp4', 'video_1.mp4', 'video_2.mp4']  # Замените на ваши файлы
output_path = 'merged_video.mp4'
target_size = (640, 360)  # Задайте нужный размер

# Загружаем видеофайлы
video_clips = [VideoFileClip(video) for video in video_paths]

# Изменяем размер каждого видео
resized_clips = [clip.resize(target_size) for clip in video_clips]

# Объединяем видео в один кадр (в ряд)
final_clip = clips_array([resized_clips])

# Сохраняем итоговое видео с заданными кодеками
final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

# Освобождаем ресурсы
for clip in resized_clips:
    clip.close()
final_clip.close()

print(f'Итоговое видео сохранено как {output_path}')