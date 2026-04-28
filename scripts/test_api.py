from litellm import get_supported_openai_params

response = get_supported_openai_params(model="openai/sonnet-4.6-asia")

print(response) # ["max_tokens", "tools", "tool_choice", "stream"]