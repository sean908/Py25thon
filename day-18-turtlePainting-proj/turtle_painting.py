import turtle
import colorgram
import random

def extract_colors(image_path, num_colors=13):
    """Extract the most used colors from an image"""
    colors = colorgram.extract(image_path, num_colors)
    
    color_list = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        color_tuple = (r, g, b)
        color_list.append(color_tuple)
    
    return color_list

def filter_background_colors(colors):
    """Remove light/background colors that are likely white or very light"""
    filtered_colors = []
    for color in colors:
        r, g, b = color
        if r < 230 or g < 230 or b < 230:
            filtered_colors.append(color)
    return filtered_colors

def mix_colors(color1, color2):
    """Randomly mix two colors with a random ratio"""
    ratio = random.random()
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    
    mixed_r = int(r1 * ratio + r2 * (1 - ratio))
    mixed_g = int(g1 * ratio + g2 * (1 - ratio))
    mixed_b = int(b1 * ratio + b2 * (1 - ratio))
    
    return (mixed_r, mixed_g, mixed_b)

def draw_dot_painting(colors, rows=9, cols=9, dot_size=10, spacing=33):
    """Draw a grid of colored dots"""
    screen = turtle.Screen()
    screen.colormode(255)
    screen.setup(width=800, height=800)
    screen.bgcolor("white")
    
    painter = turtle.Turtle()
    painter.speed("fastest")
    painter.penup()
    painter.hideturtle()
    
    start_x = -(cols - 1) * spacing / 2
    start_y = (rows - 1) * spacing / 2
    
    for row in range(rows):
        for col in range(cols):
            color1 = random.choice(colors)
            color2 = random.choice(colors)
            mixed_color = mix_colors(color1, color2)
            
            x = start_x + col * spacing
            y = start_y - row * spacing
            
            painter.goto(x, y)
            painter.dot(dot_size, mixed_color)
    
    screen.exitonclick()

def main():
    image_path = "image.jpg"
    
    print("Extracting colors from image...")
    colors = extract_colors(image_path)
    print(f"Extracted {len(colors)} colors")
    
    print("Filtering background colors...")
    filtered_colors = filter_background_colors(colors)
    print(f"Using {len(filtered_colors)} colors after filtering")
    
    if len(filtered_colors) < 2:
        print("Not enough colors after filtering. Using all extracted colors.")
        filtered_colors = colors
    
    print("Creating dot painting...")
    draw_dot_painting(filtered_colors)

if __name__ == "__main__":
    main()