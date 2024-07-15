import random
temas = {
    "Animais": ["cachorro", "gato", "elefante", "girafa", "leao","Tigre","Ovelha","Urso","Barata","Passarinho","Baleia","Anta","tatu","Tartaruga","Formiga","Peixe","Esquilo"],
    "Frutas": ["pera", "banana", "laranja", "uva", "abacaxi","Maca"],
    "Países": ["Brasil", "Argentina", "Canada", "Japao", "Alemanha","Italia","Noruega","Chile","Colombia","AfricaDoSul","Finlandia","Dinamarca"],
    "Cores": ["vermelho", "azul", "verde", "amarelo", "preto","lilas","cinza"],
    "Profissões": ["medico", "engenheiro", "professor", "advogado", "bombeiro","Desenvolvedor","Arquiteto","Juiz","Mae","Motorista","barbeiro"],
    "Esportes": ["futebol", "basquete", "tenis", "natacao", "volei","PingPong","Judo"],
    "Objetos": ["cadeira", "mesa", "computador", "telefone", "livro","Garrafa","Radio","Mochila"],
    "Filmes": ["Titanic", "Avatar", "Inception", "Gladiador", "Matrix","VelosesEFuriosos","Batman","Carrinhos","OPoderosoChefinho"],
    "Músicas": ["Imagine", "Thriller", "Bohemian Rhapsody","BomdadeDeDeus","OEncontro", "HeyJude", "Hallelujah"],
    "Cidades": ["RioDeJaneiro","SaoPaulo","Ceara","Bahia","Paris", "Londres", "NovaYork", "Toquio", "Sydney"]
}

tema = random.choice(list(temas.keys()))
palavra = random.choice(temas[tema]).lower()
print(f'O tema da rodada é: {tema}')

palavraSetada = palavra.strip()
palavraSetada = set(palavra)

resposta = []
erros = []
view = []
for i in palavra:
    view.append("_")
print(view)

while sorted(palavraSetada) != sorted(resposta):
    view = []
    letra = input(f'\nEscolha uma letra: ').strip().lower()
    if len(letra) > 1:
        print("escolha uma letra de cada vez")
        continue
    if not letra:
        print("Entrada vazia não é permitida. Tente novamente.")
        continue
    if letra in resposta or letra in erros:
        print("Letra já informada, tente uma diferente")
    else:
        if letra in palavra:
            resposta.append(letra)
            for i in palavra:
                if i in resposta:
                    view.append(i)
                else:
                    view.append("_")
            print(f'O tema da rodada é: {tema}')
            print(view)
        else:
            erros.append(letra)
            print(f'letras erradas {erros}')
            for i in palavra:
                if i in resposta:
                    view.append(i)
                else:
                    view.append("_")
            print(f'O tema da rodada é: {tema}')
            print(view)

print(f'Resposta certa: {palavra}')