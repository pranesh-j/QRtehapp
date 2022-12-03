import tkinter as tk
from PIL import Image, ImageTk
import qrcode
from web3 import Web3  # To interact with Ethereum blockchain using the web3.py library

# With Infura, we have instant access to the Ethereum network via the HTTP and WebSocket protocols.

infura_url = ("https://mainnet.infura.io/v3/8471a36e96334a3c918afd7107692b11")
w3 = Web3(Web3.HTTPProvider(infura_url))

def generate_qr_code():
  address = entry.get()

  qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=4,
  )
  #Now To generate QR code specific to Ethereum wallet address

  is_address_valid = w3.isAddress(address)

  if is_address_valid == True:

      qr.add_data(address)
      qr.make(fit=True)
      img = qr.make_image(fill_color="#716b94", back_color="black")
      img.save("QReth.png")
      print("Grats your QReth created")

      # Open the generated QR code image and display it in the label
      qr_img = Image.open("QReth.png")
      qr_img = qr_img.resize((250, 250), Image.ANTIALIAS)
      qr_img = ImageTk.PhotoImage(qr_img)
      qr_label.config(image=qr_img)
      qr_label.image = qr_img

  else:
      print(
          "Enter *Only* Ethereum wallet address! Ex: 0xF9e82768a7ED3f08b27EF11083B3BCF0A7E8A69e "
      )

# Create the main window
root = tk.Tk()
root.title("QReth App")

# Load the background image
bg_image = Image.open("bg.jpg")
bg_image = bg_image.resize((500, 500), Image.ANTIALIAS)
bg_image = ImageTk.PhotoImage(bg_image)

# Create a label for the background image
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label and text entry for the wallet address
label = tk.Label(root, text="Enter Ethereum wallet address:", font=("Verdana", 16), bg="#fafafa")
label.pack()

entry = tk.Entry(root, font=("Verdana", 16), bg="#fafafa")
entry.pack()

# Create a button to generate the QR code
button = tk.Button(root, text="Generate QR Code", font=("Verdana", 16), command=generate_qr_code)
button.pack()

# Create a label to display the generated QR code
qr_label = tk.Label(root)
qr_label.pack()

root.mainloop()
