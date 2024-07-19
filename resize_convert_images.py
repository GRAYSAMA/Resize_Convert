from PIL import Image
import os

def resize_and_convert(image_path, output_path, size=(400, 267)):
    with Image.open(image_path) as img:
        img = img.resize(size)
        img.save(output_path, 'webp')
    print(f"Processed {image_path} to {output_path}")

def process_images(input_dir, output_dir, size=(400, 267)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('png', 'jpg', 'jpeg')):
            image_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.webp')
            resize_and_convert(image_path, output_path, size)

# Example usage
input_directory = r'C:\Users\GRACE\Desktop\IRES'
output_directory = r'C:\Users\GRACE\Desktop\IRES WEBP'
process_images(input_directory, output_directory)
