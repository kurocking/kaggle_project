# https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/tree/main
# https://soroban.highreso.jp/article/article-062
# https://soroban.highreso.jp/article/article-064
# Translator
# https://note.com/python_lab/n/n13d16c29ccc1
# https://qiita.com/FKjujcc/items/c7e206bec306da891573
"""
from llama_cpp import Llama
llm = Llama(model_path="/Users/tomoking/llama.cpp/models/llama-2-7b-chat.Q4_K_M.gguf", chat_format="llama-2")

llm.create_chat_completion(
      messages = [
          {"role": "system", "content": "you are a master of meditation."},
          {
              "role": "user",
              "content": "Please tell me the points when meditating."
          }
      ]
)
"""

from llama_cpp import Llama

# LLamaモデルを初期化
model = Llama(model_path="/Users/tomoking/llama.cpp/models/llama-2-7b-chat.Q4_K_M.gguf")

print("LLamaチャットボットへようこそ！ 終了するには 'quit' と入力してください。")

while True:
    # ユーザー入力を受け取る
    user_input = input("あなた: ")

    # 終了コマンドをチェック
    if user_input.lower() == 'quit':
        print("チャットを終了します。ありがとうございました！")
        break

    # LLamaモデルで応答を生成
    response = model(f"Human: {user_input}\nAI:", max_tokens=1000, stop=["Human:", "\n"])

    # 応答を表示
    print("AI:", response['choices'][0]['text'].strip())