import qrcode
from PIL import Image

def create_qr_with_logo(data, logo_path, output_filename):
    # Generate QR Code
    qr = qrcode.QRCode(
        version=4,  # Adjust size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction to allow for logos
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create the QR code image
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # Open the logo image
    logo = Image.open(logo_path)

    # Resize the logo to fit in the QR code
    logo_size = (qr_img.size[0] // 5, qr_img.size[1] // 5)  # Scale logo size
    logo = logo.resize(logo_size, Image.LANCZOS)

    # Calculate position to paste the logo
    logo_pos = (
        (qr_img.size[0] - logo.size[0]) // 2,
        (qr_img.size[1] - logo.size[1]) // 2,
    )

    # Paste the logo onto the QR code
    qr_img.paste(logo, logo_pos, mask=logo)

    # Save the QR code with logo
    qr_img.save(output_filename)

    print(f"QR Code saved as {output_filename}")
    qr_img.show()


# Credly QR Code with Logo
create_qr_with_logo(
    data="https://your-credly-profile-url.com",  # Replace with your Credly URL
    logo_path="credly_logo.png",  # Replace with your Credly logo file name
    output_filename="credly_qrcode_with_logo.png",
)
