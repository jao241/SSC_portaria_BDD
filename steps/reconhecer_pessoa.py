from behave import given, when, then
from main import *

@given("que o ambiente de reconhecimento foi preparado com sucesso")
def given_prepara_ambiente_reconhecimento(context):
    context.configuracao, context.foto_selecionada_aleatoriamente, context.pessoa_reconhecida, context.pessoa_dados, context.lista_pessoas_condominio = configuracao_inicial()
    
    assert context.configuracao != None
    
@when("a foto {foto_visitante} de um(a) pessoa for capturada")
def when_foto_capturada(context, foto_visitante):
    context.foto_selecionada_aleatoriamente = selecionar_pessoa(foto_visitante)
    foto_criptografada = configurar_reconhecedor_face(context.foto_selecionada_aleatoriamente)
    context.pessoa_reconhecida = verifica_na_lista(foto_criptografada)
    
    assert True
    
@then("a pessoa deve ser reconhecida com base em fotos no banco de dados")
def then_pessoa_reconhecida(context):  
    assert context.pessoa_reconhecida is True