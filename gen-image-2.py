from diffusers import StableDiffusionXLPipeline
import torch
from PIL import Image

# Инициализация модели (загрузка 1 раз)
pipe = StableDiffusionXLPipeline.from_pretrained(
    "segmind/SSD-1B",
    torch_dtype=torch.float32,
    use_safetensors=True,
    variant="fp16"
).to("cpu")

# Задайте ваш текстовый запрос (промпт)
prompt = "A fantasy landscape with dragons, glowing crystals, and a waterfall, trending on ArtStation"

# Генерация изображения
image = pipe(
    prompt,
    num_inference_steps=25,  # Число шагов (меньше = быстрее, но хуже качество)
    guidance_scale=7.5        # Сила соответствия промту (рекомендуется 7-10)
).images[0]

# Сохранение изображения
image.save("result-1.jpg")
print("Изображение сохранено как result-1.jpg")