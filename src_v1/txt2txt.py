import questions
question_selected = questions.context

################################################################################################
import passwords as passwords
import google.generativeai as genai

genai.configure(api_key=passwords.GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content(question_selected)
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
import ICL.save_content as save_content

save_content.save(response.text)
