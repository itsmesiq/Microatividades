# Calculadora em Python

**Autor:** Ana Siqueira  
**Trabalho Prático:** DGT2817 LÓGICA, ALGORITMOS E
PROGRAMAÇÃO DE COMPUTADORES

---

## Sumário
1. [Introdução](#introdução)  
2. [Objetivo do projeto](#objetivo-do-projeto)  
3. [Funcionalidades](#funcionalidades)  
4. [Estrutura do código](#estrutura-do-código)  
5. [Instruções de uso](#instruções-de-uso)  
6. [Exemplo de execução](#exemplo-de-execução)  
7. [Considerações finais](#considerações-finais)  

---

## Introdução
Este projeto foi desenvolvido como trabalho prático do curso LÓGICA, ALGORITMOS E PROGRAMAÇÃO DE COMPUTADORES. Ele consiste em uma calculadora simples desenvolvida em Python. O programa permite realizar operações matemáticas básicas: adição, subtração, multiplicação e divisão, com tratamento de erros, como divisão por zero. Além disso, permite que o usuário realize múltiplas operações até decidir encerrar o programa.

---

## Objetivo do projeto
O objetivo do projeto é praticar o desenvolvimento de funções em Python, estruturas condicionais e laços de repetição, aplicando conceitos de programação modular e tratamento de erros.

---

## Funcionalidades
- Realizar adição, subtração, multiplicação e divisão.  
- Aceitar tanto sinais (`+`, `-`, `*`, `/`) quanto nomes das operações (`adicao`, `subtracao`, etc.).  
- Tratar divisão por zero, retornando uma mensagem de erro.  
- Permitir múltiplas operações em sequência até o usuário decidir sair.

---

## Estrutura do código
O código está estruturado em funções modulares, facilitando manutenção e expansão:

- `adicao(a, b)`: retorna a soma de `a` e `b`.  
- `subracao(a, b)`: retorna a subtração de `a` por `b`.  
- `multiplicacao(a, b)`: retorna a multiplicação de `a` e `b`.  
- `divisao(a, b)`: retorna a divisão de `a` por `b` ou uma mensagem de erro se `b = 0`.  
- `calculadora(num1, num2, operacao)`: identifica a operação desejada e chama a função correspondente.  
- Laço `while` principal: mantém o programa rodando até o usuário decidir sair.

---

## Instruções de uso
1. Abra o terminal ou prompt de comando.  
2. Navegue até a pasta onde o projeto está salvo.  
3. Execute o script Python:  
   ```bash
   python calculadora.py
   ```
4. Siga as instruções na tela:
   
   - Digite o primeiro número.  
   - Digite o segundo número.  
   - Digite a operação desejada (+, -, *, / ou o nome da operação).  
5. Para encerrar o programa, digite N quando perguntado se deseja continuar.

## Exemplo de execução
   ```bash
   Digite o primeiro número: 10  
   Digite o segundo número: 5  
   Digite a operação desejada (+, -, *, / ou nome): +  
   Resultado da operação: 15.0  
   Deseja continuar? (S/N): N
   ```
## Considerações finais
- Este projeto é uma aplicação educativa para praticar Python.  
- Pode ser expandido adicionando mais operações matemáticas, como potência ou raiz quadrada.  
- Excelente para estudo de funções, loops, tratamento de erros e boas práticas de programação modular.
