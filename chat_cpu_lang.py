import sys
from langchain.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

MODEL_PATH = "../../../../home/aerty/trabalho/llamawiki/models/llama-2-13b-chat.Q4_K_S.gguf"

# criar a função que carrega a llama

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

llm = LlamaCpp(
    model_path=MODEL_PATH,
    temperature=0.7,
    max_tokens=2000,
    top_p=1,
    callback_manager=callback_manager,
    verbose=True,  # Verbose is required to pass to the callback manager
)

while True:
    query = input(f"Input Prompt: ")
    if query == 'exit':

        print('Exiting')
        sys.exit()

    llm(query)