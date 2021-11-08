import sys
import nltk
nltk.download("omw")
nltk.download("wordnet")
from nltk.corpus import wordnet as wn

def list_data(listaEntrada):
    lista = []
    for dado in listaEntrada:
        for i in dado.lemma_names('por'):
            lista.append(i)
    return lista


def search_wordnet(palavra):
    resultadoPesquisa = {"searched-word":palavra,"synonyms": None, "hypernyms": None, "hyponyms": None}
    synset = wn.synsets(palavra, lang='por')

    resultadoPesquisa["synonyms"] = synset[0].lemma_names('por')
    resultadoPesquisa["hypernyms"] = list_data(synset[0].hypernyms())
    resultadoPesquisa["hyponyms"] = list_data(synset[0].hyponyms())

    print(resultadoPesquisa)


if __name__ == "__main__":
    palavraParaAnalisar = sys.argv[1]
    search_wordnet(palavraParaAnalisar)