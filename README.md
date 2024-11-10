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
Foram realizados testes com os modelos Llama2 de tamanhos 7B, 13B e 70B. 
Os testes foram realizados primeiro em CPU e depois em GPU.
É necessario baixar o modelo para pasta models.

Os modelos Llama2 foram eficientes e escaláveis em CPU. No entanto, ainda havia espaço para melhorias no desempenho de tarefas de geração de texto.
1. Execute o seguinte comando no terminal para executar o Llama2 via Cpu:
   ```
   python3 chat_cpu.py
   ```
O desempenho dos modelos Llama2 foi significativamente melhorado em GPU. As tarefas de geração de texto foram executadas até 10 vezes mais rápido em GPU do que em CPU.

2. Execute o seguinte comando no terminal para executar o Llama2 via Gpu:
   ```
   python3 chat_gpu.py
   ```
## Atividade
O modelo Llama 2, especialmente nas versões de 7B e 13B, geralmente requer uma GPU com pelo menos 4GB de memória e um mínimo de 16GB de RAM para funcionamento eficiente em configurações locais. 
