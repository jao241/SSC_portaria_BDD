Feature: busca os dados presentes no banco de dados da pessoa reconhecida e verifica se possui autorização ou não

Scenario: Após o reconhecimento da face busca-se os dados no banco de dados relacionado a pessoa e reconhece a mesma como uma pessoa autorizada

Given que o ambiente de reconhecimento foi preparado com sucesso 
When a foto /home/joaovitor/Documentos/vs_code/pessoal/SSC_portaria_BDD/BD/faces/Marcos Mion.jpg de um(a) pessoa for capturada
Then a pessoa deve ser reconhecida com base em fotos no banco de dados

Given que uma pessoa foi reconhecida
When seus dados forem retornados da base de dados
Then uma pessoa autorizada é reconhecida

Scenario: Após o reconhecimento da face busca-se os dados no banco de dados relacionado a pessoa e não reconhece a mesma como uma pessoa autorizada

Given que o ambiente de reconhecimento foi preparado com sucesso 
When a foto /home/joaovitor/Documentos/vs_code/pessoal/SSC_portaria_BDD/BD/faces/Luciano Szafir.jpg de um(a) pessoa for capturada
Then a pessoa deve ser reconhecida com base em fotos no banco de dados

Given que uma pessoa foi reconhecida
When seus dados forem retornados da base de dados
Then uma pessoa autorizada não é reconhecida
