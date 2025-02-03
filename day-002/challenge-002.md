
## **📌 Desafio do Dia 02: Variáveis, Tipos de Dados e Operadores**

### **✅ Objetivo**

Criar e manipular variáveis em Python, explorando diferentes tipos de dados e realizando operações aritméticas básicas.

### **🚀 Instruções**

1. Crie pelo menos **uma variável de cada tipo** (inteiro, float, string e booleano).
2. Realize operações matemáticas com números inteiros e floats.
3. Concatene e manipule strings.
4. Use variáveis booleanas para expressões condicionais.

---

## **📚 Breve Aula: Variáveis, Tipos de Dados e Operadores em Python**

### 🔹 **1. O que são Variáveis?**

Uma **variável** é um nome que armazena um valor. No Python, você não precisa declarar o tipo da variável explicitamente, pois o interpretador detecta automaticamente.

📌 **Exemplo de Declaração de Variáveis:**

```python
idade = 25  # Inteiro (int)
altura = 1.75  # Float (ponto flutuante)
nome = "Italo"  # String (texto)
is_estudante = True  # Booleano (True ou False)
```

> 📝 Python é  **case-sensitive** , ou seja, `Nome` e `nome` são variáveis diferentes.

---

### 🔹 **2. Tipos de Dados em Python**

Os principais tipos de dados básicos são:

* **Inteiros (`int`)** → números inteiros (ex: 10, -5, 42)
* **Flutuantes (`float`)** → números com casas decimais (ex: 3.14, -0.5, 1.0)
* **Strings (`str`)** → texto delimitado por aspas simples ou duplas (ex: "Python", 'Desafio')
* **Booleanos (`bool`)** → valores lógicos `True` ou `False`

📌 **Exemplo de cada tipo:**

```python
numero_inteiro = 10  # int
numero_decimal = 3.14  # float
texto = "Olá, Mundo!"  # str
status = False  # bool
```

---

### 🔹 **3. Operadores Matemáticos em Python**

Python permite realizar operações matemáticas de forma intuitiva. Os operadores principais são:

| Operador | Descrição                 | Exemplo              |
| -------- | --------------------------- | -------------------- |
| `+`    | Adição                    | `10 + 5 → 15`     |
| `-`    | Subtração                 | `10 - 5 → 5`      |
| `*`    | Multiplicação             | `10 * 5 → 50`     |
| `/`    | Divisão                    | `10 / 3 → 3.3333` |
| `//`   | Divisão Inteira            | `10 // 3 → 3`     |
| `%`    | Módulo (resto da divisão) | `10 % 3 → 1`      |
| `**`   | Exponenciação             | `2 ** 3 → 8`      |

📌 **Exemplo prático:**

```python
a = 10
b = 3

soma = a + b  # 13
subtracao = a - b  # 7
multiplicacao = a * b  # 30
divisao = a / b  # 3.3333
divisao_inteira = a // b  # 3
resto = a % b  # 1
potencia = a ** b  # 1000

print(f"Soma: {soma}, Potência: {potencia}")
```

---

### 🔹 **4. Manipulação de Strings**

Podemos concatenar (juntar) strings usando `+` e repetir strings usando `*`.

📌 **Exemplo de manipulação de strings:**

```python
nome = "Python"
versao = "3.10"
mensagem = nome + " versão " + versao
print(mensagem)  # Python versão 3.10

# Repetindo strings
print("=" * 20)  # ====================
```

Podemos acessar caracteres dentro da string usando índices (`[]`):

```python
texto = "Desafio"
print(texto[0])  # D (primeira letra)
print(texto[-1])  # o (última letra)
print(texto[0:3])  # Des (fatiamento)
```

---

### 🔹 **5. Booleanos e Expressões Lógicas**

Os valores `True` e `False` são fundamentais para tomadas de decisão.

📌 **Exemplo de expressões booleanas:**

```python
idade = 18
maior_de_idade = idade >= 18  # True
print(maior_de_idade)
```

---

## **💡 Dicas Extras**

✅ **Boas práticas:**

* Use **nomes descritivos** para variáveis (`idade` em vez de `x`).
* **Evite nomes reservados** do Python (ex: `print`, `sum`, `list`).
* **Use f-strings** para formatar strings:
  ```python
  nome = "Italo"
  idade = 28
  print(f"Meu nome é {nome} e tenho {idade} anos.")
  ```

---

## **🎯 Desafio Prático**

Agora que você aprendeu os conceitos principais, resolva os desafios abaixo:

1️⃣ **Crie um programa que declare quatro variáveis:**

* `idade` (int)
* `altura` (float)
* `nome` (string)
* `eh_programador` (bool)

2️⃣ **Exiba na tela o seguinte texto formatado usando f-strings:**

```
Meu nome é <nome>, tenho <idade> anos e <altura>m de altura.
Sou programador? <eh_programador>
```

3️⃣ **Realize operações matemáticas e imprima os resultados:**

* Soma de dois números inteiros.
* Multiplicação de um inteiro por um float.
* O resultado da divisão inteira entre dois números.
* O quadrado de um número usando `**`.

4️⃣ **Manipulação de strings:**

* Crie uma string `frase = "Aprendendo Python no desafio de 100 dias!"`.
* Extraia a palavra **"Python"** usando fatiamento (`[]`).
* Transforme toda a string em maiúsculas usando `.upper()`.
* Substitua "Python" por "Machine Learning" usando `.replace()`.

📌 **Exemplo de Saída Esperada**

```
Meu nome é Italo, tenho 28 anos e 1.75m de altura.
Sou programador? True
Resultado da soma: 15
Resultado da multiplicação: 37.5
Divisão inteira: 3
Quadrado do número: 49
Palavra extraída: Python
Frase em maiúsculas: APRENDENDO PYTHON NO DESAFIO DE 100 DIAS!
Frase modificada: Aprendendo Machine Learning no desafio de 100 dias!
```

---

## **🚀 Bônus (Desafio Extra)**

* Peça ao usuário para inserir seu nome, idade e altura e exiba uma mensagem personalizada com esses valores.
* Teste o uso do operador `%` para verificar se um número é par ou ímpar.

---

## **🔎 Conclusão**

Hoje você aprendeu:
✅ O que são variáveis e como usá-las

✅ Os tipos básicos de dados do Python

✅ Operações matemáticas fundamentais

✅ Como manipular strings e trabalhar com expressões booleanas

Agora, pratique os desafios e compartilhe seu código! 🚀
