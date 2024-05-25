import os
from openai import AzureOpenAI

def get_azure_openai_response(prompt):
    client = AzureOpenAI(
        azure_endpoint="https://smartmoneyai.openai.azure.com/",
        api_key="ca49bfed37b54f439deae2ef7c75bb63",
        api_version="2024-02-01"
    )

    response = client.chat.completions.create(
        model="Test",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

# Example usage
prompt = "Does Azure OpenAI support customer managed keys?"
response = get_azure_openai_response(prompt)
print(response)
