from transformers import AutoModelForCausalLM, AutoTokenizer  

tokenizer = AutoTokenizer.from_pretrained('../../../../data/models/llama-2-hf/llama-2-13b-chat-hf')  
model = AutoModelForCausalLM.from_pretrained('../../../../data/models/llama-2-hf/llama-2-13b-chat-hf')  

inputs = tokenizer("Qual a capital do Brasil ?", return_tensors="pt")  
outputs = model.generate(**inputs, max_length=20,eos_token_id=tokenizer.pad_token_id)  
print(tokenizer.decode(outputs[0]))