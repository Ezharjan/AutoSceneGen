# Change you IP into the place where Gemini is available (eg. Miami) before running this script.
import os
import time
import PIL.Image
import questions
import passwords as passwords
import google.generativeai as genai

genai.configure(api_key=passwords.GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro-vision')
question_selected = questions.context_img

# Path to the folder containing the images
folder_path = './imgs/' # TODO: Change THIS LINE TO YOUR OWN DIRECTORY

# Iterate through all the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        # Open the image
        img_path = os.path.join(folder_path, filename)
        img = PIL.Image.open(img_path)

        # Generate the response
        response = model.generate_content(img) # only provide image prompt
        # response = model.generate_content([question_selected, img], stream=True)
        response.resolve()

        # Create the output file name
        output_filename = os.path.splitext(filename)[0] + 'NoTXT.txt'
        output_path = os.path.join(folder_path, output_filename)

        # Save the response text to the file
        with open(output_path, 'w') as file:
            file.write(response.text)

        # Print the information
        print(f"Generated text for {filename} saved to {output_filename}")

        # Print additional information if needed
        print(question_selected)
        print("Response Starts:")
        print("********************************")
        print(response.text)
        print("********************************")
        print("********* Response Ends ********")
        print("### See if it was blocked due to safety concerns regarding the prompt:")
        print(response.prompt_feedback)
        print("### View the response candidates:")
        print(response.candidates)
        print('\n')
        time.sleep(15) # in case the Google web server blocks too frequent requests
