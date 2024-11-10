from llama_cpp import Llama
import xml.etree.ElementTree as ET
import os

model_path = "../../../../home/aerty/trabalho/llamawiki/models/llama-2-13b-chat.Q4_K_S.gguf"

# Definir para usar a GPU 2
os.environ["CUDA_VISIBLE_DEVICES"] = "2"


def extract_xml(xml_path):
    # Carrega o XML
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    extracted_text = ""
    
    # Itera sobre todas as tags e extrai o texto
    for elem in root.iter():
        if elem.text:
            extracted_text += elem.text.strip() + " "
    
    return extracted_text.strip()

BODY = extract_xml('exemplo.xml')

lcpp_llm = Llama(
    model_path=model_path,
    n_batch=512,
    n_ctx=4096,
    n_gpu_layers=-1,
    )


prompt_template=f'''<s>[INST] <<SYS>> 
	Você é um especialista em codificação que se especializa em XML. 
	Quando eu descrever um componente de um site que quero construir, 
    sem informações especificas do exemplo e sem informações ficticias
	retorne o XML correspondente. Não forneça uma explicação para este código.
    <</SYS>> 
    Com base no documento, crie um novo xml do tipo <ead>, conforme as instruções abaixo e o exemplos anteriores com as especificidades das instruções, preencha o máximo de campos possíveis baseado nas instruções, sem informações fictícias:
    Nível 0 contém o Nó Raiz Institution
    Nível 1 contém o Nó Other docs e nó Newspaper
    Nível 2 contém os Nós filhos de Newspaper (Folio_1, Folio_2)
    Nível 3 Folio 1 contém os nós filhos (A, B) 
    Nível 3 Folio 2 contém o nó filho (Z)
    documento: {BODY} 
    [/INST]
'''

response = lcpp_llm(
    prompt=prompt_template,
    max_tokens=2000,
    temperature=0.5,
    top_p=0.95,
    repeat_penalty=1.2,
    top_k=50,
    echo=False
    )

print(response["choices"][0]["text"])