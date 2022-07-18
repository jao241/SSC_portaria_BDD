import face_recognition
import json 
import random

ARQUIVO_CONFIGURACAO = 'configuracao.json'

LISTA_FOTOS = [
    "BD/faces/Caco Ciocler.jpg",
    "BD/faces/Debora Bloch.jpg",
    "BD/faces/Emilio Zurita.jpg",
    "BD/faces/Luciano Huck.jpg",
    "BD/faces/Luciano Szafir.jpg",
    "BD/faces/Marcos Mion.jpg",
    "BD/faces/Mateus Solano.jpg"
]

TIMEOUT_INTERVALO = 1
PROBABILIDADE_DE_SAIR = 4

def configuracao_inicial():
    with open(ARQUIVO_CONFIGURACAO, "r") as arquivo_configuracao: configuracao = json.load(arquivo_configuracao)
    foto_selecionada_aleatoriamente = None
    pessoa_reconhecida = False
    pessoa_dados = {}
    lista_pessoas_condominio = []
    
    return configuracao, foto_selecionada_aleatoriamente, pessoa_reconhecida, pessoa_dados, lista_pessoas_condominio
    
# Será um gerador de evento.
def selecionar_pessoa(foto_selecionada):
    foto_selecionada_aleatoriamente = foto_selecionada
    return foto_selecionada_aleatoriamente

# Será um gerador de evento.
def configurar_reconhecedor_face(foto_visitante):
    foto_selecionada = face_recognition.load_image_file(foto_visitante)
    foto_original_criptografada = face_recognition.face_encodings(foto_selecionada)[0]
        
    return foto_original_criptografada

def reconhecer_face(foto, foto_criptografada):

    e_igual = False    
    try:
        foto_selecionada = face_recognition.load_image_file(foto)
        foto_selecionada_criptografada = face_recognition.face_encodings(foto_selecionada)[0]
        
        e_igual = face_recognition.compare_faces([foto_criptografada], foto_selecionada_criptografada)
    except:
        pass
    
    return e_igual

# Será um gerador de evento.
def verifica_na_lista(foto_criptografada):
    pessoa_reconhecida = False
    
    for foto in LISTA_FOTOS:
        if reconhecer_face(foto, foto_criptografada):
            pessoa_reconhecida = True
            
    return pessoa_reconhecida

# Será um gerador de evento.
def realizar_verificacao_entrada(pessoa_reconhecida, configuracao, foto_selecionada_aleatoriamente):
    pessoa_dados = {} 
    
    if pessoa_reconhecida:
        for pessoa in configuracao["pessoas"]:
            if pessoa["foto"] == foto_selecionada_aleatoriamente:
                pessoa_dados = pessoa
    
    return pessoa_dados        

# Será um gerador de evento.
def verifica_residente(env):
    global pessoa_dados
    
    while True:
        if pessoa_dados["residente"] == True:
                print(f"Bem vindo de volta, residente {pessoa_dados['nome']}\n")
                lista_pessoas_condominio.append(pessoa_dados)
        else:
            print("Você não é um residente do condomínio, verificando autorização de entrada!\n")
            
        yield env.timeout(TIMEOUT_INTERVALO)
  
# Será um gerador de evento.
def verifica_autorizacao(env):
    global pessoa_dados
    
    while True:
        if pessoa_dados["residente"] == False:
            if pessoa_dados["entrada_autorizada"] == True:
                    print(f"Visitante {pessoa_dados['nome']} possui autorização, por favor entre!\n")
                    lista_pessoas_condominio.append(pessoa_dados)
            else:
                print(f"Visitante {pessoa_dados['nome']} não possui autorização de entrada!\n")
        yield env.timeout(TIMEOUT_INTERVALO)

# Será um gerador de evento.    
def sair_condominio(env):
    global lista_pessoas_condominio
    
    while True:
        alguem_vai_sair = random.randint(1, 10) <= PROBABILIDADE_DE_SAIR
        if lista_pessoas_condominio:
            if alguem_vai_sair:
                pessoa_a_remover = random.choice(lista_pessoas_condominio)
                lista_pessoas_condominio.remove(pessoa_a_remover)
                print(f'{pessoa_a_remover["nome"]} saiu do condomínio.\n')

        yield env.timeout(TIMEOUT_INTERVALO)
