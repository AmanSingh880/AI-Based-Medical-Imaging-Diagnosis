def read_image_path():
    try:

        with open("image_path.txt", "r") as file:
            image_path = file.read()
        print(f"Image path read from 'image_path.txt': {image_path}")
        return image_path
    except FileNotFoundError:
        print("File 'image_path.txt' not found.")
        return None

read_image_path()
