# Sistema Bancário em Python

## Descrição

Este é um projeto simples de sistema bancário desenvolvido em Python como parte do curso da DIO (Digital Innovation One). O sistema permite realizar operações bancárias básicas através de um interface de linha de comando, incluindo gerenciamento de usuários e contas.

## Funcionalidades

- **Depósito**: Permite depositar valores na conta, atualizando o saldo e o extrato.
- **Saque**: Realiza saques com validações de saldo, limite por saque (R$ 500) e limite de saques diários (3 saques).
- **Extrato**: Exibe o histórico de movimentações e o saldo atual.
- **Novo Usuário**: Cadastra novos usuários com CPF, nome, data de nascimento e endereço.
- **Nova Conta**: Cria contas bancárias vinculadas a usuários existentes.
- **Listar Contas**: Exibe todas as contas cadastradas com informações do titular.
- **Consulta de Limites**: Mostra o limite por saque e o número de saques restantes.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Biblioteca Padrão**: Utiliza `textwrap` para formatação de texto no menu.

## Pré-requisitos

- Python 3.6 ou superior instalado no sistema.

## Como Executar

1. Clone o repositório ou baixe os arquivos.
2. Navegue até o diretório do projeto.
3. Execute o comando:

   ```bash
   python sistema_bancario.py
   ```

4. Siga as instruções no menu interativo.

## Estrutura do Projeto

- `sistema_bancario.py`: Arquivo principal com a lógica do sistema bancário.
- `README.md`: Este arquivo de documentação.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests no repositório.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

## Tecnologias
- Python

## Como executar
```bash
python sistema_bancario.py
