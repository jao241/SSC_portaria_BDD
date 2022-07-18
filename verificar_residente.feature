Feature: busca os dados presentes no banco de dados da pessoa reconhecida

Scenario: Após o reconhecimento da face busca-se os dados no banco de dados relacionado a pessoa  

Given que o ambiente de reconhecimento foi preparado com sucesso 
When a foto /home/joao/Documentos/dev-projects/Back-projects/SSC_Portaria_BDD/BD/faces/Luciano Szafir.jpg de um(a) pessoa for capturada
Then a pessoa deve ser reconhecida com base em fotos no banco de dados

Given que uma pessoa foi reconhecida
When seus dados forem retornados da base de dados
Then verifica-se se é um residente do condomínio