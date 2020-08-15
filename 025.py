# PROGRAMA PARA FACILITAR ESTUDO DE CADEIA DE TEXTOS

frase = 'Curso em Vídeo Python'
print('\nfrase = Curso em Vídeo Python')

# FATIAMENTO
print('\n< FATIAMENTO >')
print('frase[9] =', frase[9])
print('frase[9:13] =', frase[9:13])
print('frase[9:21] =', frase[9:21])
print('frase[9:21:2] =', frase[9:21:2])
print('frase[:5] =', frase[:5])
print('frase[15:] =', frase[15:])
print('frase[9::3] =', frase[9::3])

# ANÁLISE
print('\n< ANÁLISE >')
print('len(frase) =', len(frase))
print('frase.count(o) =', frase.count('o'))
print('frase.count(o, 0, 13) =', frase.count('o', 0,13))
print('frase.find(deo) =', frase.find('deo'))
print('frase.find(Android) =', frase.find('Android'))
print('Curso in frase =', 'Curso' in frase)

# DIVISÃO
print('\n< DIVISÃO >')
print('frase.split() =', frase.split())

# JUNÇÃO
print('\n< JUNÇÃO >')
print('-.join(frase) =', '-'.join(frase))

# TRANSFORMAÇÃO
print('\n< TRANSFORMAÇÃO >')
print('frase.replace(Python, Android) -> TRANSFROMARÁ A str. Python em Android'), frase.replace('Python', 'Android')
print('frase.upper() =', frase.upper())
print('frase.lower() =', frase.lower())
print('frase.capitalize() =', frase.capitalize())
print('frase.title() =', frase.title())
print('frase.strip() =', frase.strip())
print('frase.rstrip() =', frase.rstrip())
print('frase.lstrip() =', frase.lstrip())