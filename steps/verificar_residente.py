from behave import given, when, then
from main import *

@given("que uma pessoa foi reconhecida")
def given_pessoa_reconhecida(context):
    assert context.pessoa_reconhecida is True

@when("seus dados forem retornados da base de dados")
def when_verifica_dados(context):
    context.pessoa_dados = realizar_verificacao_entrada(context.pessoa_reconhecida, context.configuracao, context.foto_selecionada_aleatoriamente)
    
    assert True    

@then("verifica-se se é um residente do condomínio")
def then_retorna_dados(context):
    pass