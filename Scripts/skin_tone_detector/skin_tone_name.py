import re

def hex_to_rgb(hex_code):

    # Remove the '#' if it's there
    hex_code = hex_code.lstrip('#')

    # Use this if the upgrade warning for skin-classifier comes otherwise comment
    hex_code = hex_code[-6:]
    
    # Convert hex to RGB
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

def get_skin_tone_name(hex_code):
    rgb = hex_to_rgb(hex_code)
    if not rgb:
        return "Invalid color code"
    
    r, g, b = rgb

    # Define skin tone ranges
    if 240 <= r <= 255 and 215 <= g <= 235 and 200 <= b <= 220:
        return "Porcelain"
    if 235 <= r <= 250 and 215 <= g <= 235 and 180 <= b <= 200:
        return "Ivory"
    if 230 <= r <= 245 and 200 <= g <= 220 and 170 <= b <= 190:
        return "Fair"
    if 225 <= r <= 245 and 195 <= g <= 215 and 180 <= b <= 200:
        return "Light Fair"
    if 215 <= r <= 235 and 165 <= g <= 185 and 140 <= b <= 160:
        return "Beige"
    if 200 <= r <= 220 and 150 <= g <= 170 and 120 <= b <= 140:
        return "Olive"
    if 180 <= r <= 210 and 140 <= g <= 160 and 110 <= b <= 130:
        return "Medium"
    if 170 <= r <= 190 and 120 <= g <= 140 and 100 <= b <= 120:
        return "Tan"
    if 140 <= r <= 170 and 90 <= g <= 120 and 70 <= b <= 90:
        return "Caramel"
    if 130 <= r <= 150 and 80 <= g <= 100 and 60 <= b <= 80:
        return "Chestnut"
    if 100 <= r <= 120 and 50 <= g <= 80 and 40 <= b <= 60:
        return "Dark"
    if 80 <= r <= 100 and 40 <= g <= 60 and 30 <= b <= 50:
        return "Deep"
    if 50 <= r <= 80 and 30 <= g <= 50 and 20 <= b <= 40:
        return "Ebony"
    
    return "Unknown skin tone"


# Example usage:
if __name__ == "__main__":
    color_code = "#EFD0BF"
    skin_tone = get_skin_tone_name(color_code)
    print(f"Color Code: {color_code} - Skin Tone: {skin_tone}")