# # import modules
# import qrcode
# from PIL import Image
# from PIL import Image, ImageDraw

# # taking image which user wants
# # in the QR code center
# Logo_link = r"C:\Users\reddy\Desktop\INTEL UNNATI\PCSNs.jpg"
# logo = Image.open(Logo_link)
# # taking base width
# basewidth = 100

# # adjust image size
# wpercent = (basewidth/float(logo.size[0]))
# hsize = int((float(logo.size[1])*float(wpercent)))
# logo = logo.resize((basewidth, hsize , ), Image.LANCZOS)
# QRcode = qrcode.QRCode(
# 	error_correction=qrcode.constants.ERROR_CORRECT_H
# )
# # taking url or text
# url = r'https://www.youtube.com/channel/UC95BEdKoeLQjGlYLgcbET4Q'
# # adding URL or text to QRcode
# QRcode.add_data(url)
# # generating QR code
# QRcode.make()
# # taking color name from user
# QRcolor = 'yellow'
# logo_size=78
# # adding color to QR code
# QRimg = QRcode.make_image(
# 	fill_color=QRcolor, back_color="black").convert('RGB')
# # set size of QR code
# logo = logo.resize((logo_size, logo_size))

# # Create a circular mask
# mask = Image.new("L", (logo_size, logo_size), 0)
# draw = ImageDraw.Draw(mask)
# draw.ellipse((0, 0, logo_size, logo_size), fill=255)

# # Apply the circular mask to the logo
# logo = logo.convert("RGBA")
# logo.putalpha(mask)

# # Calculate position to paste the logo
# pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)

# # Paste the logo onto the QR code
# QRimg.paste(logo, pos, logo)

# # save the QR code generated
# QRimg.save('Xoce_QR.png')

# print('QR code generated!')





from PIL import Image, ImageDraw
import qrcode

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data('https://www.example.com')
qr.make(fit=True)

# Convert QR code to image
QRimg = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Load the logo image
logo = Image.open(r"C:\Users\reddy\Desktop\INTEL UNNATI\PCSNs.jpg")  # Replace with your logo file path

# Resize the logo to fit within the QR code
logo_size = 50  # Adjust the size as needed
logo = logo.resize((logo_size, logo_size))

# Create a circular mask for the logo
mask = Image.new("L", (logo_size, logo_size), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, logo_size, logo_size), fill=255)

# Apply the circular mask to the logo
logo = logo.convert("RGBA")
logo.putalpha(mask)

# Create a background circle slightly larger than the logo
background_circle_size = logo_size + 10  # Adjust size as needed
background_circle = Image.new("RGBA", (background_circle_size, background_circle_size), (255, 255, 255, 0))
draw = ImageDraw.Draw(background_circle)
draw.ellipse((0, 0, background_circle_size, background_circle_size), fill=(255, 255, 255, 255))

# Calculate positions to paste the background circle and logo
pos_bg = ((QRimg.size[0] - background_circle_size) // 2, (QRimg.size[1] - background_circle_size) // 2)
pos_logo = ((QRimg.size[0] - logo_size) // 2, (QRimg.size[1] - logo_size) // 2)

# Paste the background circle onto the QR code
QRimg.paste(background_circle, pos_bg, background_circle)

# Paste the logo onto the QR code
QRimg.paste(logo, pos_logo, logo)

# Save the result
QRimg.save('TS_color.png')

# Display the result
QRimg.show()





























