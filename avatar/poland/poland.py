from PIL import Image, ImageDraw

def create_poland_flag_shirt():
    # Roblox R6 shirt template boyutları (128x128)
    width = 128
    height = 128
    
    # Yeni resim oluştur (şeffaf arka plan)
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Polonya bayrağının renkleri
    white_color = (255, 255, 255, 255)
    red_color = (220, 20, 60, 255)  # Polonya bayrağının kırmızısı
    
    # R6 Shirt Template koordinatları:
    # Front torso: (32, 20) to (52, 32)
    # Back torso: (52, 20) to (72, 32)
    # Left arm: (32, 48) to (36, 60)
    # Right arm: (44, 48) to (48, 60)
    
    # FRONT TORSO (32,20 - 52,32)
    front_width = 20
    front_height = 12
    front_half = front_height // 2
    
    # Ön taraf - üst yarı beyaz, alt yarı kırmızı
    draw.rectangle([32, 20, 52, 20 + front_half], fill=white_color)
    draw.rectangle([32, 20 + front_half, 52, 32], fill=red_color)
    
    # BACK TORSO (52,20 - 72,32) 
    back_width = 20
    back_height = 12
    back_half = back_height // 2
    
    # Arka taraf - üst yarı beyaz, alt yarı kırmızı
    draw.rectangle([52, 20, 72, 20 + back_half], fill=white_color)
    draw.rectangle([52, 20 + back_half, 72, 32], fill=red_color)
    
    # LEFT ARM (32,48 - 36,60)
    draw.rectangle([32, 48, 36, 54], fill=white_color)
    draw.rectangle([32, 54, 36, 60], fill=red_color)
    
    # RIGHT ARM (44,48 - 48,60) 
    draw.rectangle([44, 48, 48, 54], fill=white_color)
    draw.rectangle([44, 54, 48, 60], fill=red_color)
    
    # PNG olarak kaydet (şeffaflık için)
    image.save('polonya_bayragi_roblox_shirt.png', 'PNG')
    print("Polonya bayrağı Roblox shirt tasarımı oluşturuldu!")
    print("Dosya adı: polonya_bayragi_roblox_shirt.png")
    print(f"Boyutlar: {width}x{height} piksel")
    print("Ön ve arka torso + kollar dahil!")

# Fonksiyonu çalıştır
if __name__ == "__main__":
    create_poland_flag_shirt()