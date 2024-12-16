import time
import requests
import json
import passwords
import questions


# Define the headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {passwords.OPENAI_API_KEY}",
}

for question in questions.batch_context:
    # Construct the data payload
    few_shot_example = questions.context_head + question + questions.context_tail
    data = {
        "model": "gpt-4",
        "messages": [{"role": "user", "content": few_shot_example}],
    }
    # Execute the POST request
    response = requests.post(
        passwords.OPENAI_ADDRESS, headers=headers, data=json.dumps(data)
    )
    print("########################################################################")
    # Print the response (optional)
    response_json = response.json()
    message_content = response_json["choices"][0]["message"]["content"]
    candidates_count = len(response_json["choices"])
    model_used = response_json["model"]
    print("********************************")
    print("Generation finished! Here is the response:")
    print("********************************")
    print(message_content)
    print("********************************")
    print("********* Response Ends ********")
    print("########################################################################")
    print("### Using {}".format(model_used))
    print("### There are {} candidate responses.".format(candidates_count))
    import save_content

    comment = "'''Question: " + question + "'''\n"
    save_content.save(message_content, comment)
    time.sleep(5)  # Sleep for 5 seconds between each question
