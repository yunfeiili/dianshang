from PIL import Image


def resize_image(input_image_path, output_image_path):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    aspect_ratio = width / height
    new_height = 1080*4
    new_width = int(round(new_height * aspect_ratio))
    resized_image = original_image.resize((new_width, new_height),Image.LANCZOS)
    resized_image.save(output_image_path)


input_image_path = f"G:/lyfceshishi/dianshang/xuexi/tupianjihe/output.png"
output_image_path = "/output1.png"

resize_image(input_image_path, output_image_path)