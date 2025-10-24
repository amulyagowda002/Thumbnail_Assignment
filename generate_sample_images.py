from PIL import Image, ImageDraw, ImageFont
import os
os.makedirs('producer', exist_ok=True)

for i in range(1,6):
    img = Image.new('RGB', (1024,640), (50+i*30, 80+i*15, 120+i*10))
    d = ImageDraw.Draw(img)
    d.text((40,40), f'Sample Image {i}', fill=(255,255,255))
    img.save(os.path.join('producer', f'sample_{i}.jpg'), quality=85)
print('Generated 5 sample images in producer/ directory.')