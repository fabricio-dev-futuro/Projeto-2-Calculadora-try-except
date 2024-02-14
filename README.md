# Projeto-2
 Calculadora com Tratamento de erros-e-Exceções

 Esse projeto simula uma calculadora de operações simples (soma, subtração, multiplicação e divisão), onde tive a preocupação de pôr varias condições para alertar digitação errada feita pelo usuário em qualquer fase de processo input.

 Descrevendo o Projeto:

 • O código inicia pedindo ao usuário que insita um número (utilizando o input com try). Qualquer coisa diferente de um número ele cai no except do código que lhe avisará que ele deve digitar um número.

 - Veja que para que isso dê certo foi necessário transformar o input para inteiro, que que o input obriginalmente são valores String

 • O mesmo processo é feito para a escolha do segundo número, usando try/except.

 • Na fase de escolha do operador pode escolhido digitando valores input correspondentes aos mostrados na mensagem.

 • Foi feito um bloco condicional com vários if  para informar, se for o caso, ao usuário de que ele não digitou valor igual ao das opções de operador matemárico permitidos.

 • A lógica também foi feita com ty/except

 • No try começo com um condicional if que trata de infromar, se acontecer, ao usuário de que operação de divisão com número zero não é permitida.

 • Ainda dentro do try, mas no condicional else, ocorre a lógica que faz os calculos.

 •  O except fica preparado com um erro específico, que acionado caso o usuário tenha digitado algo que não seja número nas escolhas dos números para o cálculo.
