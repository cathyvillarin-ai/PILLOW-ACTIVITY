from PIL import Image, ImageDraw, ImageFont

# Load image
img = Image.open("meme_pic5.jpg")

# Resize image
base_width = 900
wpercent = (base_width / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((base_width, hsize))

W, H = img.size

# Add white padding at top and bottom
padding = 100  # space for text
new_img = Image.new("RGB", (W, H + 2 * padding), "white")
new_img.paste(img, (0, padding))

draw = ImageDraw.Draw(new_img)

#draw outlined meme text
def draw_text_with_outline(text, position, font, draw, stroke_width=3):
    x, y = position
    draw.text((x, y), text, font=font, fill="white",
              stroke_width=stroke_width, stroke_fill="black", anchor="ms")


try:
    font = ImageFont.truetype("impact.ttf", 40)
except:
    font = ImageFont.load_default()

# Top text
top_text = "When they say ‘just enjoy the intramurals’"
draw_text_with_outline(top_text, (W/2, 50), font, draw)

# Bottom text
bottom_text = "but you’re already stressed like it’s the championship"
draw_text_with_outline(bottom_text, (W/2, H + padding + 40), font, draw)

# Save and show
output_file = "BSCS3A_VillarinCathy_BTSMeme4.png"
new_img.save(output_file)
new_img.show()
