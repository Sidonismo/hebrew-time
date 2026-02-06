from PIL import Image
import os

def resize_and_convert():
    target_width = 500  # Maximální šířka, kterou na webu reálně potřebuješ
    assets_path = './assets'
    
    for root, dirs, files in os.walk(assets_path):
        for file in files:
            if file.lower().endswith(('.png', '.webp')): # Zpracuje PNG i už vytvořené WebP
                img_path = os.path.join(root, file)
                webp_path = os.path.splitext(img_path)[0] + '.webp'
                
                with Image.open(img_path) as img:
                    # Spočítáme poměr stran, aby se obrázek nedeformoval
                    if img.width > target_width:
                        w_percent = (target_width / float(img.width))
                        h_size = int((float(img.height) * float(w_percent)))
                        
                        # Změna velikosti s vysokou kvalitou (LANCZOS)
                        img = img.resize((target_width, h_size), Image.Resampling.LANCZOS)
                        print(f"Zmenšeno: {file} na {target_width}px šířky.")
                    
                    # Uložíme (přepíšeme) jako optimalizované WebP
                    img.save(webp_path, 'webp', quality=80)
