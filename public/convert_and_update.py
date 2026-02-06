import os
import re
from PIL import Image

# 1. KONVERZE OBRÁZKŮ
def convert_images():
    assets_path = './assets'
    for root, dirs, files in os.walk(assets_path):
        for file in files:
            if file.lower().endswith('.png'):
                png_path = os.path.join(root, file)
                webp_path = os.path.splitext(png_path)[0] + '.webp'
                
                with Image.open(png_path) as img:
                    img.save(webp_path, 'webp', quality=85)
                    print(f"Konvertováno: {png_path} -> {webp_path}")
                
                # Volitelné: os.remove(png_path) # Pokud chceš smazat původní PNG, odkomentuj toto

# 2. PŘEPSÁNÍ URL V HTML SOUBORECH
def update_html_files():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Najde všechny .png v uvozovkách uvnitř assets a změní je na .webp
        new_content = re.sub(r'(assets/.*?\.)png', r'\1webp', content)
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
            print(f"Aktualizovány odkazy v: {html_file}")

if __name__ == "__main__":
    convert_images()
    update_html_files()
    print("\nHOTOVO! Všechny obrázky jsou ve WebP a HTML soubory odkazují na nové verze.")
