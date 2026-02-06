from PIL import Image
# Otevři logo
img = Image.open('./assets/logo.png')
# Zmenši ho na rozumný rozměr (např. šířka 200px)
w_percent = (200 / float(img.width))
h_size = int((float(img.height) * float(w_percent)))
img = img.resize((200, h_size), Image.Resampling.LANCZOS)
# Ulož jako WebP s vyšší kompresí
img.save('./assets/logo.webp', 'webp', quality=60, lossless=False)
