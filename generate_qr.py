import qrcode
import os

# Адрес сайта
BASE_URL = "https://thorfinnkarlsefn1.github.io/projectmuseum/"

# Создал папку для QR-кодов
os.makedirs('static/qr', exist_ok=True)

# ID - шники экспонатов
exhibit_ids = [1, 2, 3]

for exp_id in exhibit_ids:
    url = f"{BASE_URL}/exhibit_{exp_id}.html"
    
    # Создаём QR-код
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=7,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Сохраняем как картинку
    img = qr.make_image(fill_color="black", back_color="white")
    filename = f'static/qr/exp_{exp_id}.png'
    img.save(filename)
    print(f" QR-код для экспоната {exp_id} сохранён: {filename}")

print("\n🎉 Готово! Распечатай QR-коды из папки static/qr/")