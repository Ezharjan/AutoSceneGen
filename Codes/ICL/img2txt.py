import PIL.Image
import questions
question_selected = questions.context_img

################################################################################################
import passwords as passwords
import google.generativeai as genai
genai.configure(api_key=passwords.GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro-vision')
img = PIL.Image.open('./img.jpg') # TODO: Change THIS LINE TO YOUR OWN DIRECTORY
# response = model.generate_content(img) # only provide image prompt
response = model.generate_content([question_selected, img], stream=True)
response.resolve()
print(question_selected)
print("Response Starts:")
print("********************************")
print(response.text)
print("********************************")
print("********* Response Ends ********")
print("### See if it was blocked due to saftey concerns regarding the prompt:")
print(response.prompt_feedback)
print("### View the response candidates:")
print(response.candidates)
################################################################################################

'''
Output:
This is a scenario of car accident, please generate a report on this accident. The template is: `Time:xxx; Location:xxx; Event:xxx; Severity:xxx.`
Response Starts:
********************************
 **Time:** 2023-03-08 10:30:00

**Location:** Intersection of Main Street and Elm Street

**Event:** A white semi-truck and a gray car collided at the intersection of Main Street and Elm Street. The semi-truck was traveling north on Main Street when it collided with the car, which was traveling east on Elm Street. The car was pinned underneath the semi-truck.

**Severity:** The driver of the car was killed in the accident. The driver of the semi-truck was not injured.
********************************
********* Response Ends ********
### See if it was blocked due to saftey concerns regarding the prompt:
safety_ratings {
  category: HARM_CATEGORY_SEXUALLY_EXPLICIT
  probability: NEGLIGIBLE
}
safety_ratings {
  category: HARM_CATEGORY_HATE_SPEECH
  probability: NEGLIGIBLE
}
safety_ratings {
  category: HARM_CATEGORY_HARASSMENT
  probability: NEGLIGIBLE
}
safety_ratings {
  category: HARM_CATEGORY_DANGEROUS_CONTENT
  probability: NEGLIGIBLE
}

### View the response candidates:
[index: 0
content {
  parts {
    text: " **Time:** 2023-03-08 10:30:00\n\n**Location:** Intersection of Main Street and Elm Street\n\n**Event:** A white semi-truck and a gray car collided at the intersection of Main Street and Elm Street. The semi-truck was traveling north on Main Street when it collided with the car, which was traveling east on Elm Street. The car was pinned underneath the semi-truck.\n\n**Severity:** The driver of the car was killed in the accident. The driver of the semi-truck was not injured."
  }
  role: "model"
}
finish_reason: STOP
safety_ratings {
  category: HARM_CATEGORY_SEXUALLY_EXPLICIT
  probability: NEGLIGIBLE
}
safety_ratings {
  category: HARM_CATEGORY_HATE_SPEECH
  probability: NEGLIGIBLE
}
safety_ratings {
  category: HARM_CATEGORY_HARASSMENT
  probability: NEGLIGIBLE
}
safety_ratings {
  category: HARM_CATEGORY_DANGEROUS_CONTENT
  probability: NEGLIGIBLE
}
citation_metadata {
}
]

'''