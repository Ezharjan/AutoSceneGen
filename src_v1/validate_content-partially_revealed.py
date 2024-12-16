import requests
import json
import passwords

def extract_code(content):
    start = content.find("```python")
    end = content.find("```", start + len("```python"))    
    if start != -1 and end != -1:
        code = content[start + len("```python"):end].strip()
        return code
    return "WARN: NO CODE CONTENT DETECTED!"

def validate_by_words(content):
    result = extract_code(content)
    return result and result or "No code detected!"


def validate_by_ai(content):
    validation_prompt = (
        "For the following content, clean it, remove all the descriptions and leave only the executable code without any unimportant comments or markdown quotes like '```' or '```python', only leave pure code: "
        + content
    )
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {passwords.OPENAI_API_KEY}",
    }
    data = {
        "model": "gpt-4",
        "messages": [{"role": "user", "content": validation_prompt}],
    }
    response = requests.post(
        passwords.OPENAI_ADDRESS,
        headers=headers,
        data=json.dumps(data),
    )
    response_json = response.json()
    message_content = response_json["choices"][0]["message"]["content"]
    candidates_count = len(response_json["choices"])
    model_used = response_json["model"]
    # print(message_content)
    print(">>> Content validated!")
    return message_content

def validate(content):
    return validate_by_words(content)