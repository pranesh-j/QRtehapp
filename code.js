// JavaScript code for interactivity and functionality of the website
const generateQR = () => {
  // Get the wallet address from the input field
  const address = document.getElementById("address").value;

  // Use the qrcode library to generate the QR code
  const qr = qrcode.QRCode(
    version=1,
    errorCorrection=qrcode.constants.ERROR_CORRECT_L,
    boxSize=10,
    border=4,
  );

  // Check if the entered address is a valid Ethereum wallet address
  const isAddressValid = w3.isAddress(address);

  if (isAddressValid) {
    // Add the address to the QR code and generate the image
    qr.addData(address);
    qr.make();
    const img = qr.makeImage(fillColor="#716b94", backColor="black");

    // Create an image element to display the QR code
    const imgElement = document.createElement("img");
    imgElement.src = img;
    imgElement.alt = "QR Code for Ethereum Wallet Address";

    // Add the image to the QR code div
    const qrCodeDiv = document.getElementById("qr-code");
    qrCodeDiv.innerHTML = "";
    qrCodeDiv.appendChild(imgElement);
  } else {
    // Show an error message if the entered address is not valid
    alert("Please enter a valid Ethereum wallet address!");
  }
};
