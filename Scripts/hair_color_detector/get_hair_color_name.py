import numpy as np

def get_hair_color(rgb_array):
    """Determine the closest hair color based on RGB ranges."""
    # Convert the numpy array to a tuple of integers
    rgb = tuple(rgb_array)

    hair_colors = {
        'Blonde': ((180, 160, 100), (255, 250, 220)),  # Broader range for various blonde shades
        'Brunette': ((20, 12, 10), (160, 100, 60)),    # Expanded to cover very dark brown to medium brown
        'Redhead': ((60, 20, 10), (220, 180, 100))     # Broader range to include deep red, auburn, and strawberry blonde
    }

    # Determine if the RGB values fall within any of the defined ranges
    for color, (low, high) in hair_colors.items():
        if all(low[i] <= rgb[i] <= high[i] for i in range(3)):
            return color

    # Covering all cases by a broader category if none match exactly
    return 'Unknown'