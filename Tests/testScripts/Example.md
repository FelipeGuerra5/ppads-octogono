Cada script teste deve ter as seguintes informações:


# Identificação única
“TST-001 Saque bem-sucedido”

# Caso de uso em que se baseia
“UC-001 Realizar saque em dinheiro”

# Cenário
“Fluxo principal”

# Preparação (descrição da condição do sistema no início do teste)
“Cliente ‘Pedro Silva’, de CPF 111122222, deve estar cadastrado no
sistema e deve ter uma conta número 00222-33, com senha 123456 e saldo
inicial de R$ 1000,00.”

# Passos para execução do teste
“(1) Entrar no campo ‘número da conta’ o valor 00222-33. (2)
Entrar no campo ‘senha’ o valor 123456. (3) Selecionar a operação de saque.
(4) Entrar no campo ‘quantia’ o valor de R$ 350,00.”

# Resultado esperado
“O sistema deve apresentar a mensagem ‘Saque efetuado com
sucesso!’, a gaveta de dinheiro deve abrir com a quantia de R$ 350,00 e o
saldo atual mostrado na tela deve apresentar o valor de R$ 650,00.”

# Resultado do teste (para ser preenchido após a execução do teste)
Valores possíveis: NÃO EXECUTADO, SUCESSO, FALHA, CANCELADO.

# Descrição do resultado obtido (para ser preenchido, caso o teste não tenha
sucesso)

# Data da última execução do teste
Note que, para cada caso de uso, será necessário escrever vários scripts de
teste (pelo menos um para cada cenário). Em alguns casos, pode ser necessário
escrever mais de um script para cenário (para poder executar um teste, para cada
partição de valores e para cada valor-limite).
Os scripts de teste podem ser agrupados em casos de testes.
Cada caso de testes deve ter as seguintes informações:

Identificação única
“TC-001 Testes de realizar saque em dinheiro”

Lista dos scripts de teste deste caso
7 AULA 4 - Prática profissional em análise e desenvolvimento de sistemas
“TST-001 Saque bem-sucedido; TST-002 Tentativa de saque acima do valor limite; TST-003 Tentativa de saque de valor superior ao saldo.”