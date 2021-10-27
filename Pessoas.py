
pessoas = [
    ('Lisboa', 'LIS'),
    ('Madri', 'MAD'),
    ('PARIS', 'CDG'),
    ('BRUXELAS', 'BRU'),
    ('LONDRES', 'LHR'),
]

destino = 'FCO'

voos = {}

for linha in open('./flights.txt'):
    origem, destino, saida, chegada, preco = linha.split(',')
    voos.setdefault((origem, destino), [])
    voos[(origem, destino)].append((saida, chegada, int(preco)))

