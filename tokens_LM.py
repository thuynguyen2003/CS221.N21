import string

# đường dẫn tới file câu.txt
path = "sources/sentences.txt"
# dọc file cau.txt dưới dạng một list python
with open(path, mode="r", encoding="utf-8-sig") as f:
    data = f.read().split('\n')
data_sentences = []
for i in data:
    sen = i[0].lower() + i[1:]
    data_sentences.append(sen)



# đường dẫn tới file câu.txt
path = "sources/Viet74K.txt"
# dọc file Viet74K.txt dưới dạng một list python
with open(path, mode="r", encoding="utf-8-sig") as f:
  data_wordlist = f.read().split('\n')

# Tách từ bộ data_wordlist thành các gói bi_gram, tri_gram, quad_gram
bi_gram = [] 
tri_gram = []
quad_gram = []
for i in data_wordlist:
  if(len(i.split()) == 2):
    bi_gram.append(i)
  elif(len(i.split()) == 3):
    tri_gram.append(i)
  elif(len(i.split()) == 4):
    quad_gram.append(i)
   
# Tổng hợp các gram trong N_gram
N_gram = []
N_gram.append(bi_gram)
N_gram.append(tri_gram)
N_gram.append(quad_gram) 


def sentence_preprocess(data):
    # chuyển thành in thường
    data_sentences = []
    for i in data:
        sen = i[0].lower() + i[1:]
        data_sentences.append(sen)
    
    list_sentences = [];
    punc =  '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~“?”'
    number = "0123456789"
    point_num = ',./'          
    # Tách các tiếng và dấu câu thành các token riêng       
    for i in data_sentences:      
        x = len(i);
        j = 0;
        while j < x:
            if i[j] == '%':
                if j == 0 or (i[j-1] not in number):
                    i = i[:j] + ' ' + i[j:]
                    i = i[:j+2] + ' ' + i[j+2:]
                    x = x+2;
                    j = j+2;
            elif i[j] in punc:
                if (i[j] not in point_num) or j == 0 or j == x-1 or (i[j-1] not in number) or (i[j+1] not in number):
                    i = i[:j] + ' ' + i[j:]
                    i = i[:j+2] + ' ' + i[j+2:]
                    x = x+2;
                    j = j+2;     
            j = j+1;
        list_sentences.append(i.strip().split())
    return list_sentences
    
def check_word(n_gram, word):
  for i in n_gram:
    if word == i:
      return True
  return False

def LongestMatching(sen_tokenized):
    result = []
    cur_sentence = []
    cur_word = ""
    candidate_N_gram = [0] * 4
    for i in range(len(sen_tokenized)):
        V = sen_tokenized[i].copy()
        while(len(V) > 0):
            V_temp = V.copy()
            cur_word = V_temp[0]
            V_temp.pop(0)
            count = 1
            for j in range(len(V_temp)):
                cur_word = cur_word + " " + V_temp[j]
                if (check_word(N_gram[j], cur_word) == True): 
                    count = count + j + 1;
                if(j == 2):
                    break;
            cur_word = V.copy()[0]
            V.pop(0)
            for i in range(1, count):
                cur_word = cur_word + "_" + V.copy()[0]
                V.pop(0)
            cur_sentence.append(cur_word)
        result.append(cur_sentence)
        cur_sentence = []
    return result

def Token(sentence, type="single"):
    sen_tokenized = sentence_preprocess(sentence)
    result = LongestMatching(sen_tokenized)
    output = ""
    for i in result:
        output = output + " ".join(i) + '\n'
    return output
    
# print(LM_Token(["Hôm nay tôi, quá là mệt mỏi"]))