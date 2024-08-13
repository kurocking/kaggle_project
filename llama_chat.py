from translate import Translator
#from googletrans import Translator
from llama_cpp import Llama


def translator(in_lang, out_lang, text):
    translator = Translator(from_lang=in_lang, to_lang=out_lang)
    translated_text = translator.translate(text)
    return translated_text

def make_model():
    llm = Llama(model_path="/Users/tomoking/llama.cpp/models/llama-2-7b-chat.Q4_K_M.gguf")
    return llm

def chat(llm):
    model = llm
    print("LLamaチャットボットへようこそ！ 終了するには 'quit' と入力してください。")
    while True:
        # ユーザー入力を受け取る
        user_input = input("あなた: ")
        # 終了コマンドをチェック
        if user_input.lower() == 'quit':
            print("チャットを終了します。ありがとうございました！")
            break
        user_input = translator("ja", "en", user_input)

        # LLamaモデルで応答を生成
        response = model(f"Human: {user_input}\nAI:", max_tokens=1000, stop=["Human:", "\n"])
        response_ja = translator("en", "ja", response['choices'][0]['text'].strip())
        print("AI: " + response_ja)
        # 応答を表示
        # print("AI:", response['choices'][0]['text'].strip())



def main():
    llm = make_model()
    chat(llm)


if __name__ == "__main__":
    main()
