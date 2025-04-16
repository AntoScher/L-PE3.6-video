from diffusers import StableDiffusionXLPipeline
from diffusers.utils import make_image_grid
import torch
from PIL import Image
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем Hugging Face токен из переменной окружения (укажи его в файле .env как HF_TOKEN=your_token)
hf_token = os.environ.get("HF_TOKEN")

# Загружаем модель без ревизии fp16, для CPU лучше использовать torch.float32
pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float32,
    use_auth_token=hf_token
)

# Переводим модель на CPU
pipe = pipe.to("cpu")

# Генерируем изображение по текстовой подсказке
prompt = "A fantasy landscape with dragons, glowing crystals, and a waterfall, trending on ArtStation"
result = pipe(prompt, num_inference_steps=25, guidance_scale=7.5)
image = result.images[0]

# Сохраняем полученное изображение
image.save("result-2.jpg")
print("Изображение успешно сохранено как result-2.jpg")