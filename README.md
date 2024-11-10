## Instruções para Replicar

1. Clone este repositorio localmente.
   ```
   git clone https://github.com/AertySantos/llIni.git
   cd llmIni
   ```
2. Crie um ambiente virtual com conda e ative-o. Primeiro, certifique-se de ter o conda instalado. Em seguida, execute o seguinte comando:
   ```
   conda create -n llms python=3.11 -y
   conda activate llms
   ```

3. Execute o seguinte comando no terminal para instalar os pacotes Python necessários:
   ```
   pip install -r requirements.txt
   ```
## Testes iniciais

Este exemplo demonstra como utilizar o modelo Llama2 13B. O mesmo processo pode ser adaptado para outros modelos com configurações semelhantes. Os testes foram realizados tanto em CPU quanto em GPU para comparar o desempenho. **Nota:** Certifique-se de baixar o modelo e salvá-lo na pasta `models`.

## Instruções de Execução

### 1. Execução do Llama2 via CPU
Para rodar o modelo em CPU, utilize o comando abaixo no terminal:

```bash
python3 chat_cpu.py
```

### 2. Execução do Llama2 via GPU
Para rodar o modelo em GPU, utilize o seguinte comando:

```bash
python3 chat_gpu.py
```

## Comparação de Desempenho: CPU vs. GPU

O desempenho do Llama2 13B foi consideravelmente superior em GPU em comparação com CPU. Em tarefas de geração de texto, o processamento na GPU foi até **10 vezes mais rápido** que na CPU. Isso faz da GPU a opção ideal para tarefas que exigem alta velocidade, especialmente em casos de geração de texto em tempo real.

---
## Atividade
O modelo Llama 2, especialmente nas versões de 7B e 13B, geralmente requer uma GPU com pelo menos 4GB de memória e um mínimo de 16GB de RAM para funcionamento eficiente em configurações locais. 
