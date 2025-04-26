# import pandas as pd
# import pywhatkit as kit
# import time

# # Load Excel File
# # Ensure numbers are read as strings
# df = pd.read_excel("Contacts.xlsx", dtype={'Phone Number': str})

# # Iterate Over Each Contact
# for index, row in df.iterrows():
#     name = row["Name"]
#     phone_number = str(row["Phone Number"])  # Convert number to string
#     message = row["Message"]

#     # Ensure the phone number starts with a '+'
#     if not phone_number.startswith("+"):
#         print(f"Skipping {name} - Invalid phone number format: {phone_number}")
#         continue

#     print(f"Sending message to {name} ({phone_number})...")

#     # Send WhatsApp Message
#     kit.sendwhatmsg_instantly(phone_number, message,
#                               wait_time=15, tab_close=True)

#     # Wait to Avoid Spam Detection
#     time.sleep(5)  # Adjust as needed

# print("All messages sent successfully!")

import pywhatkit as kit
import time
import pandas as pd

# Load Excel File (Make sure 'Phone Number', 'Message', and 'Image_Path' columns exist)
df = pd.read_excel("Contacts.xlsx", dtype={'Phone Number': str})

# Iterate Over Each Contact
for index, row in df.iterrows():
    name = row["Name"]
    phone_number = str(row["Phone Number"])  # Convert number to string
    message = row["Message"]
    image_path = row["Image_Path"]  # Path to the image

    # Ensure the phone number starts with '+'
    if not phone_number.startswith("+"):
        print(f"Skipping {name} - Invalid phone number format: {phone_number}")
        continue

    print(f"Sending image to {name} ({phone_number})...")

    # Send WhatsApp Image with Message
    kit.sendwhats_image(
        receiver=phone_number,
        img_path=image_path,
        caption=message,
        wait_time=15  # Delay before sending
    )

    # Wait to Avoid Spam Detection
    time.sleep(20)  # Adjust delay as needed

print("All messages sent successfully!")
