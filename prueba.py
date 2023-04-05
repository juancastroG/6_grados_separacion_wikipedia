lista = ['Barack','Obama']
urlWiki = 'https://en.wikipedia.org/wiki/Barack_Obama'


print([nombre for nombre in lista if nombre not in urlWiki.split('/')[-1].replace('_',' ')])