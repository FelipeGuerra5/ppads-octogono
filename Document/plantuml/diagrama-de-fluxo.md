### Fazer Login - ( CDU001 )
```plantuml
@startuml
hide footbox
actor Usuario
boundary "__userBoundary__" as ub
control "__userValidation__" as uv
control "__dataValidation__" as dv
entity "__studentsCatalog__" as sc

Usuario -> ub : 1. O usuário insere o Login e Senha e aperta no botão de LogIn
activate ub
ub -> uv : 2. O sistema envia os dados para o servidor
activate uv
uv -> uv : 3. O servidor a compara a senha enviada com a senha existente no DB
uv -> ub : 4. Retorna a permissão de login
deactivate uv
deactivate ub
@enduml
```

### Escolher Classe - ( CDU002 )
```plantuml
@startuml
hide footbox
actor Usuario
boundary "__userBoundary__" as ub
control "__userValidation__" as uv
control "__dataValidation__" as dv
entity "__studentsCatalog__" as sc

Usuario -> ub : 1. O usuário clica no botão correspondente a classe à qual irá lessionar
activate ub
ub -> uv : 2. O Sistema envia o ID e token de acesso ao Servidor
activate uv
uv -> uv : 3. O servidor Valida o token de acesso
uv -> sc : 4. O Servidor resgata os dados de DataBase
activate sc
sc -> uv
deactivate sc
uv -> ub : 5. O servidor responde com os dados da classe selecionada
ub -> ub : 6. O front-end exibe os dados em tela
deactivate uv
activate ub
deactivate ub
@enduml
```

### Escolher ação para classe - ( CDU003 )
```plantuml
@startuml
hide footbox
actor Usuario
boundary "__userBoundary__" as ub
control "__userValidation__" as uv
control "__dataValidation__" as dv
entity "__studentsCatalog__" as sc

Usuario -> ub : 1. O usuário escolhe opção que irá lessionar
activate ub
ub -> uv : 2. O ID da opção e o token de acesso são enviados ao Servidor
activate uv
uv -> uv : 3. O Servidor Valida o token de acesso
uv -> uv : 4. O Servidor verifica o privilégio do usuário
uv -> sc : 5. O Servidor resgata os dados do DataBase
activate sc
sc -> uv : 6. O DataBase restorna os dados solicitados
deactivate sc
uv -> ub : 7. O Servidor retorna os dados para a pagina selecionada de acordo com o privilégio
deactivate uv
ub -> ub : 8. O front-end exibe os dados em tela
activate ub
deactivate ub
@enduml
```

### Fazer Chamada ou Registro de faltas - ( CDU004 )
```plantuml
@startuml
hide footbox
actor Usuario
boundary "__userBoundary__" as ub
control "__userValidation__" as uv
control "__dataValidation__" as dv
entity "__studentsCatalog__" as sc

Usuario -> ub : 1. O usuário clica em cada um dos botões que representam os alunos para a determinada Sala de Aula
activate ub
ub -> ub : 2. O front-end fornece feedback dos dados selecionados e os armazena
Usuario -> ub : 3. Usuario finaliza chamada
ub -> uv : 4. O sistema envia um o token de Acesso juntamente com um Objeto contendo os alunos e seus status
activate uv
uv -> uv : 5. O servidor valida o token de Acesso
uv -> dv : 6. Os dados vão para validação
deactivate uv
activate dv 
dv -> dv : 7. O Servidor valida os Dados
dv -> sc : 8. O servidor adiciona os dados ao DataBase
activate sc
sc -> dv : 9. O servidor retorna a resposta de sucesso
deactivate sc
dv -> ub : 10. Confirmação é retornada ao client
deactivate dv
ub -> ub : 11. front-end disponibiliza infomação de sucesso
activate ub
deactivate ub
@enduml
```

### Observar Estatisticas ou Relatórios de faltas - ( CDU005 )
```plantuml
@startuml
hide footbox
actor Usuario
boundary "__userBoundary__" as ub
control "__userValidation__" as uv
control "__dataValidation__" as dv
entity "__studentsCatalog__" as sc

Usuario -> ub : 1. O Usuário pode seleciona um filtro para os dados
activate ub
ub -> ub: 2. disponibiliza dropbox
ub -> uv : 3. O sistema envia o token de acesso ao servidor
activate uv
ub -> ub : 3.1. O sistema (front-end) executa o filtro nos dados selecionados
uv -> uv : 4. O servidor valida o token de acesso
uv -> ub : 5. O servidor responde com sessão valida
ub -> ub : 5.1. O front-end responde com os dados filtrados
activate ub
deactivate ub
@enduml
```

### Observar Lista de Estudantes - ( CDU006 )
```plantuml
@startuml
hide footbox
actor Usuario
boundary "__userBoundary__" as ub
control "__userValidation__" as uv
control "__dataValidation__" as dv
entity "__studentsCatalog__" as sc

Usuario -> ub : 1. O usuário seleciona um estudante
activate ub
ub -> uv : 2. O sistema envia o ID do estudante e token de acesso ao Servidor
activate uv
uv -> uv : 3. O Servidor valida o Token de acesso
uv -> sc : 4. O servidor faz a requisição de dados ao DataBase
activate sc
sc -> uv : 5. DataBase retorna dados
deactivate sc
uv -> ub : 6. O servidor responde com os dados do aluno selecionado 
deactivate uv
ub -> ub : 7. Front-end disponibiliza os dados em tela
activate ub
deactivate ub
@enduml
```

### Observar Estudante - ( CDU007 )
```plantuml
@startuml
hide footbox
actor Usuario
boundary "__userBoundary__" as ub
control "__userValidation__" as uv
control "__dataValidation__" as dv
entity "__studentsCatalog__" as sc

Usuario -> ub : 1. O Usuário altera o mês do calendário.
activate ub
ub -> uv : 2. O sistema envia o mes requerido e o token de acesso ao Servidor
activate uv
uv -> uv : 3. O servidor Valida o token de acesso
uv -> sc : 4. o servidor faz requisição dos dados ao DataBase
activate sc
sc -> uv : 5. O DataBase retorna os dados
deactivate sc
uv -> ub : 6. O servidor retorna os dados para o mes solicitado
deactivate uv
ub -> ub : 7. Front-end disponibiliza os dados em tela
activate ub
deactivate ub

@enduml
```

### Selecionar matéria - ( CDU008 )
```plantuml
@startuml
hide footbox
actor Usuario
boundary "__userBoundary__" as ub
control "__userValidation__" as uv
control "__dataValidation__" as dv
entity "__studentsCatalog__" as sc

Usuario -> ub : 1. O Usuário (Pai) seleciona a matéria da qual deseja vizualizar dados
activate ub
ub -> uv : 2. O sistema envia o ID da materia juntamente com token de acesso ao Servidor
activate uv
uv -> uv : 3. O Servidor Valida o token de acesso
uv -> sc : 4. O servidor faz requisição dos dados dos aluno para a matéria
activate sc
sc -> uv : 5. DataBase retorna os dados do aluno para a matéria
deactivate sc
uv -> ub : 6. O servidor retorna os dados do aluno para a matéria
deactivate uv
ub -> ub : 7. Front-end disponibiliza os dados em tela
activate ub
deactivate ub
@enduml
```
