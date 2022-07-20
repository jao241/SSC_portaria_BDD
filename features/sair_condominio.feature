Feature: realiza o processo de saida de uma pessoa do condomínio

Scenario: Um residente deseja sair do condomínio

Given que o ambiente de reconhecimento foi preparado com sucesso 
When a foto /home/joao/Documentos/dev-projects/Back-projects/SSC_Portaria_BDD/BD/faces/Luciano Szafir.jpg de um(a) pessoa for capturada
Then a pessoa deve ser reconhecida com base em fotos no banco de dados

Given que uma pessoa foi reconhecida
When seus dados forem retornados da base de dados
Then um residente é reconhecido

Given um residente deseja sair do condominio
When seus dados forem removidos da lista de pessoas no condominio
Then o residente sairá do condomínio

Scenario: Uma pessoa autorizada deseja sair do condomínio

Given que o ambiente de reconhecimento foi preparado com sucesso 
When a foto /home/joao/Documentos/dev-projects/Back-projects/SSC_Portaria_BDD/BD/faces/Marcos Mion.jpg de um(a) pessoa for capturada
Then a pessoa deve ser reconhecida com base em fotos no banco de dados

Given que uma pessoa foi reconhecida
When seus dados forem retornados da base de dados
Then uma pessoa autorizada é reconhecida

Given uma pessoa autorizada deseja sair do condominio
When seus dados forem removidos da lista de pessoas no condominio
Then a pessoa autorizada sairá do condomínio