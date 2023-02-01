from django.shortcuts import render, redirect
import torch
from diffusers import DiffusionPipeline, EulerDiscreteScheduler
import os
from .models import *


# Create your views here.
def index(request):
    # form = PromptModelForm()
    # print(os.getcwd()
    # 給編號

    prompt, description = '', ''
    image = 'image/test.jpg'
    scale, seed, steps = 0, 0, 0
    height = [size for size in range(128, 1025, 128)]
    width = [size for size in range(128, 1025, 128)]
    categories = Category.objects.all()
    promptBase = PromptBase.objects.all().values()

    if request.method == "POST":
        prompt = request.POST['prompt']
        scale = float(request.POST['scale'])
        seed = int(request.POST['seed'])
        steps = int(request.POST['steps'])
        height = int(request.POST['height'])
        width = int(request.POST['width'])
        print(prompt, scale, seed, steps, sep='\n')
        image = generate(prompt, scale, seed, steps, height, width)
    context = {
        'promptBase': promptBase,
        'categories': categories,
        'prompt': prompt,
        'image': image,
        'scale': scale,
        'seed': seed,
        'steps': steps,
        'height': height,
        'width': width,
        'description': description
    }
    print(promptBase.values())
    # print(request.POST['prompt'])

    return render(request, 'gallery/index.html', context)


def generate(prompt, scale, seed, steps, height, width):
    device = "cuda" if torch.cuda.is_available() else 'cpu'
    model_id = "stabilityai/stable-diffusion-2"
    auth_token = "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"

    scheduler = EulerDiscreteScheduler.from_pretrained(
        model_id, subfolder="scheduler")
    pipe = DiffusionPipeline.from_pretrained(
        model_id, use_auth_token=auth_token, scheduler=scheduler).to(device)
    # use_auth_token = auth_token
    # with autocast(device):

    """
    seed : 能控制圖片生成的多樣性，
    step : 次數越多，文本推理步驟就越多
    SCALE:
    """

    generator = torch.Generator(device).manual_seed(seed)  # seed設定，seed越高
    image = pipe(prompt,  height=height, width=width, guidance_scale=scale,
                 num_inference_steps=steps, generator=generator).images[0]
    image.save(f'statics/image/test.jpg')

    return f'image/test.jpg'
