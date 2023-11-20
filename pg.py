from PIL import Image
text_to_encrypt=input("enter the secret message:")
passcode=input('enter the password :')

def process_text(image, text, passcode, mode='encrypt'):
    pixels = list(image.getdata())
    processed_pixels = []

    text_index = 0
    passcode_index = 0

    for pixel in pixels:
        red = pixel[0]
        if mode == 'encrypt':
            code = ord(text[text_index])
            text_index = (text_index + 1) % len(text)
        else:
            code = ord(passcode[passcode_index % len(passcode)])
            passcode_index = (passcode_index + 1) % len(passcode)

        red ^= code

        processed_pixel = (red, pixel[1], pixel[2])
        processed_pixels.append(processed_pixel)

    processed_image = Image.new('RGB', image.size)
    processed_image.putdata(processed_pixels)

    return processed_image

def main():
    image_path = r"C:\Users\TQ28\Desktop\Internship project\dog.png"
    image = Image.open(image_path)

    # text_to_encrypt = "Hello, this is a secret message."
    # passcode ="hello"

    encrypted_image = process_text(image, text_to_encrypt, passcode)
    encrypted_image.save(r"C:\Users\TQ28\Desktop\Internship project\dogy.png")

    entered_passcode = input("Enter the passcode: ")

    press=input('enter 1 to reveal text ')
    a=int(press)
    if a==1:
        print("This is your secret code"+" "+text_to_encrypt)
    else:
        print("ok your Message is hidden")
    print("wait for the encrypted image.....")        
     
 
  

    if entered_passcode == passcode:
        decrypted_image = process_text(encrypted_image, "", passcode, mode='decrypt')
        decrypted_image.show()
      
        
        
    else:
        print("Incorrect passcode. Decryption failed.")
        
      

if __name__ == "__main__":
    main()


