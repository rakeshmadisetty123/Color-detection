from PIL import Image, ImageDraw
import pandas as pd

img_path = r'/Users/sairakesh/Downloads/Color-Detection-OpenCV-main/colorpic.jpg'
img = Image.open(img_path)

# declaring global variables (are used later on)
clicked = False
r = g = b = x_pos = y_pos = 0

# Reading csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

# function to calculate minimum distance from all colors and get the most matching color
def get_color_name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

# function to get x,y coordinates of mouse double click
def draw_function(event, x, y, flags, param):
    global b, g, r, x_pos, y_pos, clicked
    if event == cv2.EVENT_LBUTTONDBLCLK:
        clicked = True
        x_pos = x
        y_pos = y
        r, g, b = img.getpixel((x, y))

img.show()
img_draw = ImageDraw.Draw(img)

while True:
    if clicked:
        # Drawing rectangle
        img_draw.rectangle([(20, 20), (750, 60)], fill=(r, g, b))

        # Creating text string to display( Color name and RGB values )
        text = get_color_name(r, g, b) + f' R={r} G={g} B={b}'

        # Drawing text
        img_draw.text((50, 50), text, fill=(255, 255, 255), font=None)

        # For very light colours we will display text in black colour
        if r + g + b >= 600:
            img_draw.text((50, 50), text, fill=(0, 0, 0), font=None)

        clicked = False

    img.show()
    # You might need to adjust the duration parameter based on your preferences
    img.show()
    if cv2.waitKey(20) & 0xFF == 27:
        break
