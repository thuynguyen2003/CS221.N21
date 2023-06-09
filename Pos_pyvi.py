from pyvi import ViTokenizer, ViPosTagger

def token(sentences):
    return ViTokenizer.tokenize(sentences)


def Pos(sentences):
    token_result = []
    for sen in sentences:
        token_result.append(token(sen))
    pos_sentences = []
    tag_types = {}
    for sentence in token_result:
        #print(1, sentence)
        words = []
        tagged_sentence = ViPosTagger.postagging(sentence.replace('\n', ''))
        for i in range(len(tagged_sentence[0])):
            tag = tagged_sentence[1][i].replace('C', 'Cc').replace('S', 'C').replace('F', 'CH')
            words.append(tagged_sentence[0][i] + '/' + tag)
            if tag in tag_types: tag_types[tag] += 1
            else: tag_types[tag] = 1
        pos_sentences.append(' '.join(words))
    result = ""
    for i in pos_sentences:
        result += i +'\n'
    return result
