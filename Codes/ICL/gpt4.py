import requests
import json
import passwords
import questions

# Define the headers and data
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {passwords.OPENAI_API_KEY}",
}

# question = questions.context # for common use
question = questions.context_head + questions.context + questions.context_tail # for few-shot learning
print(question)
data = {"model": "gpt-4", "messages": [{"role": "user", "content": question}]} 

# Execute the POST request
response = requests.post(
    passwords.OPENAI_ADDRESS, headers=headers, data=json.dumps(data)
)

print("########################################################################")
# Print the response (optional)
# print(response.text) # this will print the whole response as is shown with the structure below
response_json = response.json()
message_content = response_json["choices"][0]["message"]["content"]
candidates_count = len(response_json["choices"])
model_used = response_json["model"]
print("********************************")
print("Here is the response:")
print("********************************")
print(message_content)
print("********************************")
print("********* Response Ends ********")
print("########################################################################")
print("### Using {}".format(model_used))
print("### There are {} candidate response.".format(candidates_count))
import save_content
comment = "'''Question: " + questions.context + "'''\n"
save_content.save(message_content, comment)
"""
Whole Response Structure:
{
    "object": "chat.completion.chunk",
    "model": "gpt-4",
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "message": {
                "content": "CONTENT_WITH_SLASHES",
                "role": "assistant"
            }
        }
    ],
    "created": 123456789456,
    "id": "xxx",
    "usage": {
        "completion_tokens": 123,
        "prompt_tokens": 1234,
        "total_tokens": 5678
    }
}
"""