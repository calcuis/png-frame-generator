from PIL import Image, ImageDraw

def generate_png(file_path):
    image = Image.new("RGBA", (48, 48), (0, 0, 0, 0))
    
    draw = ImageDraw.Draw(image)
    draw.rectangle([(10, 10), (38, 38)], fill=(168, 168, 168, 255))
    image.save(file_path)

file_path = "output.png"

generate_png(file_path)

print(f"PNG file generated at: {file_path}")
