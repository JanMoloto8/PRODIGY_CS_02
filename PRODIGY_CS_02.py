from PIL import Image # type: ignore
import math

def encrypt(input_path, output_path):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size
    
    for i in range(width):
        for j in range(height):
            pixel = pixels[i, j]
            if len(pixel) == 3:  # RGB image
                r, g, b = pixel
                encrypted_pixel = (b,g,r)  # Swap red and blue channels
            elif len(pixel) == 4:  # RGBA image
                r, g, b, a = pixel
                encrypted_pixel = (b, g, r, a)  # Swap red and blue channels, keep alpha unchanged
                
            pixels[i, j] = encrypted_pixel
    
    img.save(output_path)
    print('Image encrypted successfully')

def decrypt(input_path, output_path):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size
    for i in range(width):
        for j in range(height):
            pixel = pixels[i, j]
            if len(pixel) == 3:  # RGB image
                r, g, b = pixel
             
                decrypted_pixel = (b, g, r)  # Swap back red and blue channels
            elif len(pixel) == 4:  # RGBA image
                r, g, b, a = pixel
                decrypted_pixel = (b, g, r, a)  # Swap back red and blue channels, keep alpha unchanged
            
            pixels[i, j] = decrypted_pixel
    
    img.save(output_path)
    print('Image decrypted successfully')


input_image = r"C:\Users\janmo\Desktop\Tasks_prodigy\Original.jpg"
encrypted_image = r"C:\Users\janmo\Desktop\Tasks_prodigy\encrypted.png"
decrypted_image = r"C:\Users\janmo\Desktop\Tasks_prodigy\decrypted.png"

# Encrypt the image
encrypt(input_image, encrypted_image)
# Decrypt the image
decrypt(encrypted_image, decrypted_image)
