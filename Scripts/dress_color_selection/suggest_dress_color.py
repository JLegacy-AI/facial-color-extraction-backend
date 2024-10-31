def suggest_dress_color(skin_tone, eye_color, hair_color):
    # Define the seasonal palettes with corresponding hex codes for each color
    color_codes = {
        "Apple Mint": "#A8E6CF",
        "Flamingo": "#FF6F61",
        "Corn Yellow": "#F2D34E",
        "Warm Gray": "#A89F91",
        "Pitch Melba": "#EAB8A1",
        "Apricot": "#FDD9A3",
        "Light Hyacinth": "#A6C8E0",
        "Aquamarine": "#7FFFD4",
        "Light Aqua": "#A3D9D3",
        "Purple": "#800080",
        "Watermelon": "#FF3B3F",
        "Violet": "#8A2BE2",
        "Living Coral": "#FF6F61",
        "Harvest Gold": "#DAA520",
        "Yellow Ochre": "#C8A20B",
        "Blue Jewel": "#007B99",
        "Shocking Pink": "#FF6F92",
        "Dutch Blue": "#1E90FF",
        "Leaf": "#A8D85A",
        "Lime": "#A8D600",
        "Kelly Green": "#4FCF65",
        "Tan": "#D2B48C",
        "Golden Cinnamon": "#C49A6A",
        "Mallard": "#3C8A8D",
        "Bright Coral": "#FF6F61",
        "Lobelia": "#A24C9D",
        "Red Coral": "#FF4040",
        "Cashmere Rose": "#D6B1C1",
        "Pink Ice": "#F2B2D4",
        "Wisteria": "#B9A0D6",
        "Iced Aqua": "#A7D3DB",
        "Pastel Jade": "#A8E1D8",
        "Primrose": "#F5E24E",
        "Cornflower": "#6495ED",
        "Soft Teal": "#A4D6D6",
        "Pink Peacock": "#D5006D",
        "Damson": "#6C4F94",
        "Soft Orchid": "#D7B2E6",
        "Light Gray": "#A8A8A8",
        "Mushroom": "#BDAF9A",
        "Duck Egg": "#A7D3E0",
        "Marine Teal": "#007A7A",
        "Silver Birch": "#B7C9C3",
        "Sultry Navy": "#2C3E50",
        "Lilac Gray": "#C8B7D3",
        "Lavender Violet": "#E1C6E0",
        "Fuchsia Rose": "#D1006C",
        "Dusty Mulberry": "#A86E8D",
        "Rose Taupe": "#B69F8B",
        "Smoked Grape": "#6F4C7A",
        "Sea Foam": "#A8E1D3",
        "Soft Spruce": "#B7C9B7",
        "Bubble Gum": "#FF6F81",
        "Bluebell": "#A6C8E0",
        "Dove Grape": "#AFA9C9",
        "Periwinkle": "#8C99E0",
        "Deep Teal": "#004B4D",
        "Soft Cream": "#F5E4C2",
        "Rich Navy": "#001F3F",
        "Burnt Chestnut": "#7B4B3A",
        "Forest Green": "#228B22",
        "Aubergine": "#5B3F5D",
        "Deep Olive": "#4A4E0D",
        "Cassis": "#5E3A5D",
        "Rich Merlot": "#7D3C3C",
        "Java": "#4B3D3A",
        "Cream Antique Gold": "#E6D9A8",
        "Soft Caramel": "#D29F6C",
        "Maroon Navy": "#4E2C2D",
        "Latte": "#C6B29A",
        "Flint": "#A7A8AA",
        "Peacock": "#007B7F",
        "Musk Rose": "#D16D85",
        "Antique Teal": "#5B7F7A",
        "Truffle": "#B3AFA1",
        "Kingfisher": "#00A3E0",
        "Shaded Spruce": "#005C5E",
        "Turtle Green": "#4B8C57",
        "Ginger": "#D1771C",
        "Moss": "#8A9A5B",
        "Honey": "#D6A04D",
        "Saffron": "#F5C42C",
        "Indian Ochre": "#C57C2B",
        "Russet": "#7C4A3A",
        "Roomba Red": "#A61A34",
        "Deep Claret": "#7E2A2C",
        "Mulberry": "#9B5A9C",
        "Blackberry": "#6E4B8A",
        "True Blue": "#0072B8",
        "Arapaua Blue": "#3E5B93",
        "Midnight Gray": "#2F2A2B",
        "Elm": "#6B4F3B",
        "Deep Forest": "#3B5A2A",
        "Blue-Red": "#FF003C",
        "Cerise": "#D7006D",
        "Icy Blue": "#A6D7E0",
        "Chinese Blue": "#1C86EE",
        "Dark Emerald": "#005B5D",
        "Silver Gray": "#C0C0C0",
        "French Gray": "#B1B3B3",
        "Victoria Blue": "#2A9DCE",
        "Blue Violet": "#8A2BE2",
        "Bright Amethyst": "#9B59B6",
        "Azure Blue": "#007FFF",
        "Merlot": "#7B2A3D",
        "Ice Pink": "#F4C9D6",
        "Bright Emerald": "#00B140",
        "Hot Pink": "#FF69B4",
        "Sapphire": "#0F52BA",
        "Vivid Red": "#FF3C30",
        "Cobalt": "#0047AB"
    }

    # Define the seasonal palettes
    seasons = {
        'Light Spring': {
            'Skin': ['Fair', 'Medium', 'Tan'],
            'Hair': ['Blonde'],
            'Eyes': ['Blue Gray', 'Brown Gray', 'Green Gray', 'Hazel'],
            'Colors': ["Apple Mint", "Flamingo", "Corn Yellow", "Warm Gray", "Pitch Melba", "Apricot", "Light Hyacinth", "Aquamarine", "Light Aqua"]
        },
        'Bright Spring': {
            'Skin': ['Medium', 'Tan', 'Caramel', 'Chestnut'],
            'Hair': ['Blonde', 'Brunette'],
            'Eyes': ['Blue', 'Brown', 'Green'],
            'Colors': ["Purple", "Watermelon", "Violet", "Living Coral", "Harvest Gold", "Yellow Ochre", "Blue Jewel", "Shocking Pink", "Dutch Blue", "Leaf"]
        },
        'Warm Spring': {
            'Skin': ['Medium', 'Tan', 'Caramel'],
            'Hair': ['Redhead'],
            'Eyes': ['Blue', 'Green', 'Hazel'],
            'Colors': ["Lime", "Yellow Ochre", "Kelly Green", "Tan", "Sea Spray", "Golden Cinnamon", "Mallard", "Bright Coral", "Lobelia", "Red Coral"]
        },
        'Light Summer': {
            'Skin': ['Porcelain', 'Fair', 'Light Fair', 'Beige'],
            'Hair': ['Blonde'],
            'Eyes': ['Blue', 'Blue Gray', 'Green Gray'],
            'Colors': ["Cashmere Rose", "Pink Ice", "Wisteria", "Iced Aqua", "Pastel Jade", "Primrose", "Cornflower", "Soft Teal", "Pink Peacock", "Mallard"]
        },
        'Muted Summer': {
            'Skin': ['Beige', 'Olive', 'Medium', 'Tan'],
            'Hair': ['Brunette'],
            'Eyes': ['Blue Gray', 'Brown Gray', 'Green Gray'],
            'Colors': ["Damson", "Soft Orchid", "Light Gray", "Mushroom", "Duck Egg", "Marine Teal", "Silver Birch", "Sultry Navy", "Lilac Gray", "Lavender Violet"]
        },
        'Cool Summer': {
            'Skin': ['Rosy Ivory', 'Light Beige', 'Medium Beige', 'Cool Olive', 'Cool Cacao', 'Porcelain', 'Ivory', 'Olive'],
            'Hair': ['Brunette'],
            'Eyes': ['Gray', 'Blue', 'Green', 'Muted Brown'],
            'Colors': ["Fuchsia Rose", "Dusty Mulberry", "Rose Taupe", "Smoked Grape", "Sea Foam", "Soft Spruce", "Bubble Gum", "Bluebell", "Dove Grape", "Periwinkle"]
        },
        'Dark Autumn': {
            'Skin': ['Caramel', 'Chestnut', 'Deep', 'Olive', 'Medium'],
            'Hair': ['Brunette'],
            'Eyes': ['Dark Brown', 'Dark Green', 'Dark Hazel', 'Deep Espresso'],
            'Colors': ["Deep Teal", "Soft Cream", "Rich Navy", "Burnt Chestnut", "Forest Green", "Aubergine", "Deep Olive", "Cassis", "Rich Merlot", "Java"]
        },
        'Muted Autumn': {
            'Skin': ['Beige', 'Olive', 'Tan'],
            'Hair': ['Blonde'],
            'Eyes': ['Hazel', 'Green Gray', 'Blue Gray'],
            'Colors': ["Cream Antique Gold", "Soft Caramel", "Maroon Navy", "Latte", "Flint", "Peacock", "Musk Rose", "Antique Teal", "Truffle"]
        },
        'Warm Autumn': {
            'Skin': ['Medium', 'Tan', 'Caramel', 'Chestnut'],
            'Hair': ['Redhead'],
            'Eyes': ['Hazel'],
            'Colors': ["Kingfisher", "Shaded Spruce", "Turtle Green", "Ginger", "Moss", "Honey", "Saffron", "Indian Ochre", "Chestnut", "Russet"]
        },
        'Dark Winter': {
            'Skin': ['Cool Tan', 'Ebony', 'Dark', 'Olive'],
            'Hair': ['Brunette'],
            'Eyes': ['Brown Black'],
            'Colors': ["Roomba Red", "Deep Claret", "Mulberry", "Blackberry", "Rich Navy", "True Blue", "Arapaua Blue", "Midnight Gray", "Elm", "Deep Forest"]
        },
        'Bright Winter': {
            'Skin': ['Medium', 'Fair', 'Beige', 'Tan', 'Deep'],
            'Hair': ['Brunette'],
            'Eyes': ['Green', 'Hazel', 'Blue Gray', 'Brown Gray'],
            'Colors': ["Bright Amethyst", "Purple", "Azure Blue", "Merlot", "Ice Pink", "Bright Emerald", "Hot Pink", "Sapphire", "Vivid Red", "Cobalt"]
        },
        'Cool Winter': {
            'Skin': ['Medium', 'Fair', 'Beige', 'Tan', 'Deep'],
            'Hair': ['Brunette'],
            'Eyes': ['Green', 'Hazel', 'Blue Gray', 'Brown Gray'],
            'Colors': ["Blue-Red", "Cerise", "Icy Blue", "Chinese Blue", "Violet", "Dark Emerald", "Silver Gray", "French Gray", "Victoria Blue", "Blue Violet"]
        }
    }

   # Fallback color suggestions based on eye color
    eye_color_fallback = {
        "Blue Gray": ["Aquamarine", "Light Hyacinth", "Sapphire"],
        "Brown Gray": ["Warm Gray", "Cashmere Rose", "Periwinkle"],
        "Green Gray": ["Apple Mint", "Kelly Green", "Bright Coral"],
        "Hazel": ["Pitch Melba", "Apricot", "Violet"],
        "Blue": ["Azure Blue", "Sea Foam", "Periwinkle"],
        "Green": ["Lime", "Kelly Green", "Sapphire"],
        "Brown": ["Golden Cinnamon", "Tan", "Roomba Red"]
    }

    # Fallback color suggestions based on skin tone
    skin_tone_fallback = {
        "Fair": ["Warm Gray", "Cashmere Rose", "Periwinkle"],
        "Medium": ["Corn Yellow", "Kelly Green", "Bright Coral"],
        "Tan": ["Apple Mint", "Flamingo", "Pitch Melba"],
        "Olive": ["Aquamarine", "Light Aqua", "Violet"],
        "Porcelain": ["Light Hyacinth", "Sea Foam", "Azure Blue"],
        "Ivory": ["Apricot", "Soft Cream", "Sapphire"],
        "Beige": ["Golden Cinnamon", "Mallard", "Tan"]
    }

    # Fallback color suggestions based on hair color
    hair_color_fallback = {
        "Blonde": ["Apple Mint", "Flamingo", "Aquamarine"],
        "Brunette": ["Cashmere Rose", "Pink Ice", "Wisteria"],
        "Redhead": ["Kelly Green", "Bright Coral", "Violet"],
        "Black": ["Deep Claret", "Rich Navy", "Roomba Red"],
        "Gray": ["Warm Gray", "Silver", "Soft Cream"]
    }

 # Try to find a match in seasons first
    for season, details in seasons.items():
        if skin_tone in details['Skin'] and hair_color in details['Hair'] and eye_color in details['Eyes']:
            return [f"{color}:{color_codes[color]}" for color in details['Colors']]

# If not found, prioritize based on the richness of the color suggestions for each attribute
    matched_colors = []
    if not matched_colors:  # If seasons are omitted or no match found
        matched_colors.extend(eye_color_fallback.get(eye_color, []))
    if not matched_colors:
        matched_colors.extend(skin_tone_fallback.get(skin_tone, []))
    if not matched_colors:
        matched_colors.extend(hair_color_fallback.get(hair_color, []))

    # Remove duplicates and provide recommendations
    unique_colors = list(set(matched_colors))  # Remove duplicates
    if not unique_colors:
        return ["No colors found. Please adjust input values."]
    return [f"{color}:{color_codes.get(color, '#FFFFFF')}" for color in unique_colors]



