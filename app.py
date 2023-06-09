import gradio as gr
import tokens_LM
import Pos_pyvi
import warnings
warnings.filterwarnings('ignore')


# funntion related token
def filter_token(choice):
    if choice == "Một câu":
        return [gr.update(visible=True), gr.update(visible=False)]
    else:
        return [gr.update(visible=False), gr.update(visible=True)]
    
def token_single_sentence(sentence):
    sentences = sentence.split('\n')
    return tokens_LM.Token(sentences)

def token_multi_sentence(file):
    with open(file.name, "r", encoding="utf-8-sig") as f:
      content = f.read()
    sentences = content.split("\n")
    result = tokens_LM.Token(sentences)
    with open("file_result.txt", "w", encoding="utf-8-sig") as f:
         f.write(result)
    return result, "file_result.txt"

# interface tab tách từ
input_token_single_sentence = gr.Interface(
    fn = token_single_sentence,
    inputs = gr.Textbox(label = "Câu: "),
    outputs = gr.Textbox(label="Kết quả: "), 
    allow_flagging="never"   ,
    #button = gr.Submit("Tách")
)
input_token_multi_sentence = gr.Interface(
    token_multi_sentence,
    inputs = gr.File(file_types = [".txt"]),
    outputs = [gr.Textbox(label = "Kết quả", lines = 6), gr.File(file_types = [".txt"], label = "Kết quả")],
    allow_flagging="never"   
    #button = gr.Button("Tách")
)


# funcntion related Pos
def filter_Pos(choice):
    if choice == "Một câu":
        return [gr.update(visible=True), gr.update(visible=False)]
    else:
        return [gr.update(visible=False), gr.update(visible=True)]
def Pos_single_sentence(sentence):
    sentences = sentence.split('\n')
    return Pos_pyvi.Pos(sentences)

def Pos_multi_sentence(file):
    with open(file.name, "r", encoding="utf-8-sig") as f:
      content = f.read()
    sentences = content.split("\n")
    result = Pos_pyvi.Pos(sentences)
    with open("file_result.txt", "w", encoding="utf-8-sig") as f:
         f.write(result)
    return result, "file_result.txt"

# interface tab gán nhãn
input_Pos_single_sentence = gr.Interface(
    Pos_single_sentence,
    inputs = gr.Textbox(label = "Câu: "),
    outputs = gr.Textbox(label="Kết quả: "),   
    allow_flagging="never"    
)
input_Pos_multi_sentence = gr.Interface(
    Pos_multi_sentence,
    inputs = gr.File(file_types = [".txt"]),
    outputs = [gr.Textbox(label = "Kết quả", lines = 6), gr.File(file_types = [".txt"], label = "Kết quả")],
    allow_flagging="never"   
)
title="CS221 - Xử lý ngôn ngữ tự nhiên";
with gr.Blocks() as CS221:
    gr.Markdown(
    """
    # CS231 - Xử lý ngôn ngữ tự nhiên.
    #### Tách từ và gán nhãn từ loại Tiếng Việt
    """)
    with gr.Tab("Tách từ"):
        radio = gr.Radio(["Một câu", "Nhiều cầu"], value="Một câu", label = "Chọn số lượng câu muốn tách")         
        with gr.Row(visible=True) as mainA:
            with gr.Column(visible=True) as colA:
                with gr.Row(visible=True) as rowA:        
                    input_token_single_sentence.render()
                with gr.Row(visible=False) as rowB:
                    input_token_multi_sentence.render()      

        radio.change(filter_token, radio, [rowA, rowB])
            
    with gr.Tab("Gán nhãn"):
        radio = gr.Radio(["Một câu", "Nhiều cầu"], value="Một câu", label = "Chọn số lượng câu muốn gán nhãn")         
        with gr.Row(visible=True) as mainA:
            with gr.Column(visible=True) as colA:
                with gr.Row(visible=True) as rowA:        
                    input_Pos_single_sentence.render()
                with gr.Row(visible=False) as rowB:
                    input_Pos_multi_sentence.render()      

        radio.change(filter_Pos, radio, [rowA, rowB])

CS221.launch(share=True)