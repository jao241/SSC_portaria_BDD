from behave import then
from main import *

@then("uma pessoa autorizada é reconhecida")
def then_autorizacao_reconhecida(context):
    context.tem_autorizacao, context.lista_pessoas_condominio = verifica_autorizacao(context.pessoa_dados, context.lista_pessoas_condominio)

    assert context.tem_autorizacao is True


@then("uma pessoa autorizada não é reconhecida")
def then_autorizacao_reconhecida(context):
    context.tem_autorizacao, context.lista_pessoas_condominio = verifica_autorizacao(context.pessoa_dados, context.lista_pessoas_condominio)

    assert context.tem_autorizacao is False
