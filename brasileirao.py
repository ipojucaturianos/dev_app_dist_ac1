import json
from pprint import pprint

def pega_dados():
    with open('ano2018.json') as f:
        dados2018 = json.load(f)
    return dados2018

'''
1 - grupo (OPE)
2 - data 25/02 até às 15h
3 - Colocar os nomes dos integrantes em ordem alfa
4 - Somente 1 aluno entrega
5 - Chamada vai ser pela entrega da AC1
6 - Somente o arquivo brasileirao.py


-------------> Equipe: Ipojucaturianos <--------------
Ellen Cristina Marques Carvalho    - RA: 1903635
Filipe Verrone de Lima             - RA: 1903580
Gustavo Yudi Nakajima Carvalho     - RA: 1903565
João Severino dos Santos Godoi     - RA: 1903601
Leonardo Ricardo Pomarino Vargas   - RA: 1903584
Marco Aguiar                       - RA: 1904248
Vinicius Tirelli Prestes Prudêncio - RA: 1903611


1. Crie uma função datas_de_jogo, que procura nos dados do 
brasileirão recebidas no parâmetro e devolve uma lista de todas 
as datas em que houve jogo.

As datas devem ter o mesmo formato que tinham nos dados do 
brasileirão.

Dica: busque em dados['fases'].

Observe que essa função (e todas as demais) recebem os dados dos
jogos num parâmetro chamado "dados". Essa variável contém todas 
as informações que foram lidas do arquivo JSON que acompanha 
essa atividade.
'''
def datas_de_jogo(dados):
    resposta = []
    for data in dados['fases']['2700']['jogos']['data']:
        resposta.append(data)
    return resposta

'''

2. Crie uma função data_de_um_jogo, que recebe a id numérica de 
um jogo e devolve a data em que ele ocorreu.

Se essa nao é uma id válida, você deve devolver a 
string 'não encontrado'.
Cuidado! Se você devolver uma string ligeiramente diferente, 
o teste vai falhar.

(você provavelmente vai querer testar sua função no braço e não
somente fazer os meus testes. Para isso, note que muitos números
nesse arquivo estão representados não como números, mas como 
strings)
'''
def data_de_um_jogo(dados, id_jogo):
    lista_datas = dados['fases']['2700']['jogos']['data']
    for data in lista_datas:
        if id_jogo in lista_datas[data]:
            return data
    return 'não encontrado'    

'''
3. Nos nossos dados, cada time tem um id, uma identificação 
numérica. (você pode consultar as identificações numéricas 
em dados['equipes']).

A próxima função recebe a id numérica de um jogo, e devolve as
ids numéricas dos dois times envolvidos.

Vou deixar um código pra você lembrar como retornar duas ids em
um único return.

def ids_dos_times_de_um_jogo(dados, id_jogo):
    time1 = 12
    time2 = 13
    return time1, time2 # Assim, retornamos as duas respostas 
    em um único return.
'''
def ids_dos_times_de_um_jogo(dados, id_jogo):
    time1 = dados['fases']['2700']['jogos']['id'][id_jogo]['time1']
    time2 = dados['fases']['2700']['jogos']['id'][id_jogo]['time2']
    return time1, time2

'''
4. A próxima função recebe a id_numerica de um time e deve 
retornar o seu 'nome-comum'.
'''
def nome_do_time(dados,id_time):
    return dados['equipes'][id_time]['nome-comum']

'''
5. A próxima função "cruza" as duas anteriores. Recebe uma id 
de um jogo e retorna os "nome-comum" dos dois times.
'''
def nomes_dos_times_de_um_jogo(dados, id_jogo):
    time1, time2 = ids_dos_times_de_um_jogo(dados, id_jogo)
    nome_time1 = nome_do_time(dados, time1)
    nome_time2 = nome_do_time(dados, time2)
    return nome_time1, nome_time2

'''
6. Façamos agora a busca "ao contrário". Conhecendo
o nome-comum de um time, queremos saber a sua id.

Se o nome comum não existir, retorne 'não encontrado'.
'''
def id_do_time(dados, nome_time):
    for time in dados['equipes']:
        if dados['equipes'][time]['nome-comum'] == nome_time:
            return dados['equipes'][time]['id']
    return 'não encontrado'

'''
7. Queremos procurar por 'Fla' e achar o Flamengo. 
Ou por 'Paulo' e achar o São Paulo.

Nessa busca, você recebe um nome, e verifica os campos
'nome-comum', 'nome-slug', 'sigla' e 'nome',
tomando o cuidado de aceitar times se a string
buscada aparece dentro do nome (A string "Paulo"
aparece dentro de "São Paulo").

Sua resposta deve ser uma lista de ids de times que "batem"
com a pesquisa (e pode ser vazia, se não achar ninguém).
'''
def busca_imprecisa_por_nome_de_time(dados,nome_time):
    query = []
    for time in dados['equipes']:
        if (
            nome_time in dados['equipes'][time]['nome-comum']
            or nome_time in dados['equipes'][time]['nome-slug']
            or nome_time in dados['equipes'][time]['sigla']
        ):
            query.append(time)
    return query

'''
8. Agora, a ideia é receber a id de um time e retornar as
ids de todos os jogos em que ele participou.
'''
def ids_de_jogos_de_um_time(dados,time_id):
    id_jogos = []
    for jogo in dados['fases']['2700']['jogos']['id']:
        if (
            dados['fases']['2700']['jogos']['id'][jogo]['time1'] == time_id
            or dados['fases']['2700']['jogos']['id'][jogo]['time2'] == time_id
        ):
            id_jogos.append(jogo)
    return id_jogos

'''
9. Usando as ids dos jogos em que um time participou, podemos 
descobrir em que dias ele jogou.

Note que essa função recebe o nome-comum do time, não a sua id.

Ela retorna uma lista das datas em que o time jogou.
'''
def datas_de_jogos_de_um_time(dados, nome_time):
    datas_jogos = []
    time_id = id_do_time(dados, nome_time)
    ids_jogos = ids_de_jogos_de_um_time(dados, time_id)
    for id_jogo in ids_jogos:
        datas_jogos.append(
            dados['fases']['2700']['jogos']['id'][id_jogo]['data']
        )
    return datas_jogos

'''
10. A próxima função recebe apenas o dicionário dos dados do 
brasileirão.
Ela devolve um dicionário, com quantos gols cada time fez.
'''
def dicionario_de_gols(dados):
    dictionary = {}
    for equipe in dados['equipes']:
        jogos = ids_de_jogos_de_um_time(dados, equipe)
        gols = 0
        for jogo in jogos:
            placar = 'placar1' if dados['fases']['2700']['jogos']['id'][jogo]['time1'] == equipe else 'placar2'
            gols += int(dados['fases']['2700']['jogos']['id'][jogo][placar])
        dictionary[equipe] = gols
    return dictionary

'''
11. A próxima função recebe apenas o dicionário dos dados do 
brasileirão.
Ela devolve a id do time que fez mais gols no campeonato.
'''
def time_que_fez_mais_gols(dados):
    dicionario_gols = dicionario_de_gols(dados)
    maior = list(dicionario_gols.keys())[0]
    for time in dicionario_gols:
        if dicionario_gols[maior] < dicionario_gols[time]:
            maior = time
    return maior

'''
12. A próxima função recebe apenas o dicionário dos dados do 
brasileirão. Ela devolve um dicionário. Esse dicionário conta, 
para cada estádio, quantas vezes ocorreu um jogo nele.

Ou seja, as chaves são ids de estádios e os valores associados,
o número de vezes que um jogo ocorreu no estádio.
'''
def dicionario_id_estadio_e_nro_jogos(dados):
    ocorre = {}
    for jogo in dados['fases']['2700']['jogos']['id']:
        id_estadio = dados['fases']['2700']['jogos']['id'][jogo]['estadio_id']
        if id_estadio in ocorre:
            ocorre[id_estadio] += 1
        else:
            ocorre[id_estadio] = 1
    return ocorre

'''
13. A próxima função recebe apenas o dicionário dos dados do 
brasileirão. Ela retorna o número de times que o brasileirão 
qualifica para a libertadores.Ou seja, devolve quantos times 
são classificados para a libertadores (consultando
o dicionário de faixas).

Note que esse número está nos dados recebidos no parâmetro e 
você deve pegar esse número daí. Não basta retornar o valor 
correto, tem que acessar os dados fornecidos.
'''
def qtos_libertadores(dados):
    qualificados = 0
    melhor_ponto, pior_ponto = (
        dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa']
    ).split('-')
    melhor_ponto, pior_ponto = int(melhor_ponto), int(pior_ponto)
    for time in range(melhor_ponto - 1, pior_ponto):
        qualificados += 1
    return qualificados

'''
14. A próxima função recebe um valor com qtos times devem aparecer
na lista, e retorna esta lista, contendo as ids dos times melhor 
classificados.
'''
def ids_dos_melhor_classificados(dados, numero):
    melhor_classificados = []
    for classificacao in range(numero):
        melhor_classificados.append(
            dados['fases']['2700']['classificacao']['grupo']['Único'][classificacao]
        )
    return melhor_classificados

'''
15. A próxima função usa as duas anteriores para retornar uma 
lista de todos os times classificados para a libertadores em
virtude do campeonato brasileiro.

Lembre-se de consultar a estrutura, tanto para obter a 
classificação, quanto para obter o número correto de times 
a retornar.

A função só recebe os dados do brasileirão.
'''
def classificados_libertadores(dados):
    melhor_ponto, pior_ponto = (
        dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa']
    ).split('-')
    pior_ponto = int(pior_ponto)
    classificados = ids_dos_melhor_classificados(dados, pior_ponto)
    return classificados

'''
16. Da mesma forma que podemos obter a informação dos times 
classificados para a libertadores, também podemos obter os 
times na zona de rebaixamento.

A próxima função recebe apenas o dicionário de dados do 
brasileirão, e retorna uma lista com as ids dos times rebaixados.

Consulte a zona de rebaixamento do dicionário de dados, não deixe
ela chumbada da função.
'''
def rebaixados(dados):
    times_rebaixados = []
    melhor_ponto, pior_ponto = (
        dados['fases']['2700']['faixas-classificacao']['classifica3']['faixa']
    ).split('-')
    melhor_ponto, pior_ponto = int(melhor_ponto), int(pior_ponto)
    for classificacao in range(melhor_ponto - 1, pior_ponto):
        times_rebaixados.append(
            dados['fases']['2700']['classificacao']['grupo']['Único'][classificacao]
        )
    return times_rebaixados

'''
17. A próxima função recebe (além do dicionario de dados 
do brasileirão) uma id de time.

Ela retorna a classificação desse time no campeonato.

Se a id nao for válida, ela retorna a string 'não encontrado'.
'''
def classificacao_do_time_por_id(dados, time_id):
    if time_id not in dados['equipes']:
        return 'não encontrado'
    for posicao in range(
        len(dados['fases']['2700']['classificacao']['grupo']['Único'])
    ):
        if time_id == dados['fases']['2700']['classificacao']['grupo']['Único'][posicao]:
            nro_classificacao = posicao + 1
            break
    return nro_classificacao
