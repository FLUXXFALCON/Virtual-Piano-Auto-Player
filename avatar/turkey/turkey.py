from PIL import Image, ImageDraw
import math

def create_turkey_flag_tshirt():
    # Roblox R6 torso boyutları (585x559)
    width = 585
    height = 559
    
    # Yeni resim oluştur (kırmızı arka plan)
    turkey_red = (227, 10, 23)  # Türk bayrağının kırmızısı
    image = Image.new('RGB', (width, height), turkey_red)
    draw = ImageDraw.Draw(image)
    
    # Ay ve yıldız için beyaz renk
    white_color = (255, 255, 255)
    
    # Ay ve yıldızın konumları (bayrak ortasında)
    center_x = width // 2 - 50  # Biraz sola kaydır
    center_y = height // 2
    
    # Ay çiz (hilal)
    moon_radius = 80
    moon_inner_radius = 65
    
    # Dış daire (büyük ay)
    moon_outer_left = center_x - moon_radius
    moon_outer_top = center_y - moon_radius
    moon_outer_right = center_x + moon_radius
    moon_outer_bottom = center_y + moon_radius
    
    # İç daire (ayın iç kısmı - kırmızı)
    moon_inner_x = center_x + 15  # Biraz sağa kaydır
    moon_inner_left = moon_inner_x - moon_inner_radius
    moon_inner_top = center_y - moon_inner_radius
    moon_inner_right = moon_inner_x + moon_inner_radius
    moon_inner_bottom = center_y + moon_inner_radius
    
    # Ayı çiz
    draw.ellipse([moon_outer_left, moon_outer_top, moon_outer_right, moon_outer_bottom], fill=white_color)
    draw.ellipse([moon_inner_left, moon_inner_top, moon_inner_right, moon_inner_bottom], fill=turkey_red)
    
    # Yıldız çiz (5 köşeli)
    star_center_x = center_x + 120  # Daha sağa kaydır
    star_center_y = center_y
    star_radius = 35
    
    # 5 köşeli yıldızın köşe koordinatları
    star_points = []
    for i in range(10):  # 5 dış + 5 iç köşe
        angle = i * math.pi / 5 - math.pi / 2  # -90 derece başlangıç
        if i % 2 == 0:  # Dış köşeler
            radius = star_radius
        else:  # İç köşeler
            radius = star_radius * 0.4
        
        x = star_center_x + radius * math.cos(angle)
        y = star_center_y + radius * math.sin(angle)
        star_points.append((x, y))
    
    # Yıldızı çiz
    draw.polygon(star_points, fill=white_color)
    
    # Resmi kaydet
    image.save('turkiye_bayragi_roblox_tshirt.jpg', 'JPEG', quality=95)
    print("Türkiye bayrağı Roblox t-shirt tasarımı oluşturuldu!")
    print("Dosya adı: turkiye_bayragi_roblox_tshirt.jpg")
    print(f"Boyutlar: {width}x{height} piksel")

# Fonksiyonu çalıştır
if __name__ == "__main__":
    create_turkey_flag_tshirt()