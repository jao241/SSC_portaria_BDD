Feature: reconhecer uma pessoa pela foto

Scenario: Uma pessoa chega a portaria e deve ser reconhecida por uma camera

Given que o ambiente de reconhecimento foi preparado com sucesso 
When a foto /home/joao/Documentos/dev-projects/Back-projects/SSC_Portaria_BDD/BD/faces/Luciano Szafir.jpg de um(a) pessoa for capturada
Then a pessoa deve ser reconhecida com base em fotos no banco de dados