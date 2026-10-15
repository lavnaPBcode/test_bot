from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)


completion = client.chat.completions.create(
  model="poolside/laguna-xs-2.1",
  messages=[{"role":"user","content":"Which number is larger, 9.11 or 9.8?"}],
  temperature=1,
  top_p=0.95,
  max_tokens=8192,
  
  stream=False
)

print(completion.choices[0].message.content)