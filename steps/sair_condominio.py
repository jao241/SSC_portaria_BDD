from behave import given, when, then
from main import *

@given("um residente deseja sair do condominio")
def given_deseja_sair(context):
    assert True
    
@when("seus dados forem removidos da lista de pessoas no condominio")
def then_remover_da_lista(context):
    context.pessoa_saiu = sair_condominio(context.lista_pessoas_condominio)
    
    assert True

@then("o residente sairá do condomínio")
def then_residente_liberado(context):
    assert context.pessoa_saiu is True
    
@given("uma pessoa autorizada deseja sair do condominio")
def given_deseja_sair(context):
    assert True
    
@then("a pessoa autorizada sairá do condomínio")
def then_pessoa_autorizada_liberada(context):
    assert context.pessoa_saiu is True
    