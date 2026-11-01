import os
import anthropic
from dotenv import load_dotenv
load_dotenv()
base_url="https://openrouter.ai/api"

client = anthropic.Anthropic(
    base_url=base_url,
    api_key=os.environ.get("OPENROUTER_API_KEY"),
)

response = client.messages.create(
    model='openrouter/free',
    max_tokens=1024,
    messages=[{"role": "user", "content": "What is a neural network in one sentence?"}]
)
print(f"Used model: {response.model}")
for block in response.content:
    if block.type == "thinking":
        print("[thinking]", block.thinking)
    elif block.type == "text":
        print(block.text)