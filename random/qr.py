
import pyqrcode
import qrcode
from PIL import Image


def generate_qr_with_logo(text, logo_path, output_path):
    logo = Image.open(logo_path)

    # taking base width
    basewidth = 100

    # adjust image size
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    QRcode.add_data(text)

    # generating QR code
    QRcode.make()

    # taking color name from user
    QRcolor = 'Green'

    # adding color to QR code
    QRimg = QRcode.make_image(
        fill_color=QRcolor, back_color="white").convert('RGB')

    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
           (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)

    # save the QR code generated
    QRimg.save(output_path)


# Example usage:
data_to_encode = "https://google.com"
# Replace with the actual path to your logo image
logo_path = "/Users/mac/Desktop/google.png"
# Replace with the desired filename for the final QR code
output_qr_with_logo_path = "output_qr_with_logo.png"

generate_qr_with_logo(data_to_encode, logo_path, output_qr_with_logo_path)
