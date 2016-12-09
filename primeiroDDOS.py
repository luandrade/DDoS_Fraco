import urllib.request
while True:
     pagina = urllib.request.urlopen('http://testeaquiderrubarsite.blogspot.com.br/')
     texto = pagina.read().decode('utf8')
     dolar = texto[25:51]
     hoje = texto[11:12]
     print('atacando...')



