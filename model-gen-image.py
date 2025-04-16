from diffusers import StableDiffusionXLPipeline
from diffusers.utils import make_image_grid
import torch
from PIL import Image

# Используем CPU-версию пайплайна с автоматическим выбором типа данных
pipe = StableDiffusionXLPipeline.from_pretrained(
    "segmind/SSD-1B",
    torch_dtype=torch.float32,  # Используем FP32 для CPU
    use_safetensors=True,
    variant="fp16"  # Сохраняем FP16 для экономии памяти
)

# Переносим модель на CPU
pipe.to("cpu")

# Для ускорения работы на CPU можно включить оптимизации:
torch.set_num_threads(16)  # Укажите количество ядер вашего процессора