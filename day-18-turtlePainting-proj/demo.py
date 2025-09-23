from turtle_painting import extract_colors, filter_background_colors, draw_dot_painting
import random

def demo_with_sample_colors():
    """Demo the painting with predefined colors if no image is available"""
    sample_colors = [
        (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
        (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85),
        (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36),
        (76, 40, 48)
    ]
    
    print("Using sample colors for demo...")
    filtered_colors = filter_background_colors(sample_colors)
    print(f"Using {len(filtered_colors)} colors")
    
    draw_dot_painting(filtered_colors)

if __name__ == "__main__":
    demo_with_sample_colors()