import spacy
from bs4 import BeautifulSoup
import urlopen
import requests
import re


def relationship(urlWiki,nlp):
    '''Funcion que obtiene el nombre de las personas relacionadas con la persona que se le pasa como parametro en wikipedia'''
    response = requests.get(urlWiki)
    soup = BeautifulSoup(response.text, "lxml")
    links = (
        soup
        .find("div", {"id":"bodyContent"})
        .findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
    )
    links = [x["href"] for x in links]

    links = [x.split('/')[-1].replace('_',' ') for x in links if x.startswith("/wiki/")]
    string_link = ', '.join(links)
    doc = nlp(string_link)
    lista = list(dict.fromkeys([ent.text for ent in doc.ents if ent.label_ == 'PERSON']))
    lista_final = [nombre for nombre in lista if nombre not in urlWiki.split('/')[-1].replace('_',' ')] #Se filtra el link para obtener solo el nombre
    lista_final = [nombre for nombre in lista_final if not any(char.isdigit() for char in nombre)]
    
    return lista_final



def enlaces(persona1, persona2,nlp):
    '''Funcion que obtiene la relacion entre dos personas en wikipedia'''

    n_busquedas = 50
    url_wiki = 'https://en.wikipedia.org/wiki/'
    persona2 = persona2.split('/')[-1].replace('_',' ')
    lista_inicio = relationship(persona1,nlp)
    lista_adyacencia = [persona1.split('/')[-1].replace('_',' ')]
    dic_personas = dict()
    if persona2 in lista_inicio:
        lista_adyacencia.append(persona2)
        return lista_adyacencia
    while(n_busquedas > 0):
        for persona in lista_inicio:
            n_busquedas -= 1
            print('Buscando enlaces de: ', persona)
            dic_personas[persona] = relationship(url_wiki+persona.replace(' ','_'),nlp)
            print('Enlaces encontrados: ', dic_personas[persona])
            if persona2 in dic_personas[persona]:
                lista_adyacencia.append(persona)
                lista_adyacencia.append(persona2)
                return lista_adyacencia            
    
    return 'No se encontro la relacion'


def imprimir():
    '''Funcion que imprime la relacion entre dos personas'''
    nlp = spacy.load('en_core_web_trf')
    lista = enlaces("https://en.wikipedia.org/wiki/Barack_Obama", "https://en.wikipedia.org/wiki/Melania_Trump",nlp)
    if lista == 'No se encontro la relacion':
        print(lista)

    else:
        print('La relacion es: ')
        for i in range(len(lista)-1):
            print(lista[i], '->', lista[i+1])
        print('La longitud de la relacion es: ', len(lista))


imprimir()

