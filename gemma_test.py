

"""
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "google/gemma-2b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

input_text = "Hello, how are you?"
input_ids = tokenizer.encode(input_text, return_tensors="pt")
output = model.generate(input_ids, max_length=50)

print(tokenizer.decode(output[0]))
"""
from transformers import AutoTokenizer, AutoModelForCausalLM

model_path = "/Users/tomoking/Downloads/gemma-keras-gemma_1.1_instruct_2b_en-v3"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

input_text = "Hello, how are you?"
input_ids = tokenizer.encode(input_text, return_tensors="pt")
output = model.generate(input_ids, max_length=50)

print(tokenizer.decode(output[0]))