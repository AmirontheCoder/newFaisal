import openai

openai.api_key = "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"

prompt1 = str(input("ASk me >> "))

model_engine = "text-davinci-003"
prompt = prompt1
temperature = 0.7
max_tokens = 2000

completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
    n=1,
    stop = None,
)

response = completion.choices[0].text
print(response)