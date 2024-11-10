from llama_cpp import Llama
import os

model_path = "../../../../home/aerty/trabalho/llamawiki/models/llama-2-13b-chat.Q4_K_S.gguf"

# Definir para usar a GPU 2
os.environ["CUDA_VISIBLE_DEVICES"] = "2"

lcpp_llm = Llama(
    model_path=model_path,
    n_threads=2,
    n_batch=512,
    n_gpu_layers=-1,
    )

prompt = "Qual a capital do Brasil ?"
prompt_template=f'''SISTEMA: Você é um assistente útil, respeitoso e honesto. Sempre responda da forma mais útil possível.

USUARIO: {prompt}

ASSISTENTE:
'''

response = lcpp_llm(
    prompt=prompt_template,
    max_tokens=30,
    temperature=0.5,
    top_p=0.95,
    repeat_penalty=1.2,
    top_k=50,
    echo=True
    )

print(response["choices"][0]["text"])