import stone
import argparse

def detect_eye_color(image_path):

    # process the image
    result = stone.process(image_path,   return_report_image=True)
    first_dominant_color = result['faces'][0]['dominant_colors'][0]['color']

    return first_dominant_color


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect eye color from an image.")
    parser.add_argument("image_path", type=str, help="Path to the image file.")
    args = parser.parse_args()

    result = detect_eye_color(args.image_path)
    print(result)

