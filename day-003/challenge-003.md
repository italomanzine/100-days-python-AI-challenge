# **📌 Desafio do Dia 03: Entrada e Saída de Dados**

## **✅ Objetivo**

Criar um programa que receba **dados do usuário** e exiba mensagens personalizadas, explorando diferentes tipos de entrada e saída.

---

# **📚 Breve Aula: Entrada e Saída de Dados em Python**

### 🔹 **1. O que é Entrada e Saída de Dados?**

* **Entrada de dados (Input)** : O programa recebe informações do usuário via teclado.
* **Saída de dados (Output)** : O programa exibe informações na tela.

📌 **Exemplo simples de entrada e saída:**

```python
nome = input("Digite seu nome: ")  # Entrada
print(f"Olá, {nome}! Bem-vindo ao desafio de Python.")  # Saída
```

> 📝 `input()` sempre retorna um  **texto (string)** , independentemente do que o usuário digitar.

---

### 🔹 **2. Entrada de Dados com `input()`**

A função `input()` recebe um  **texto digitado pelo usuário** . Exemplo:

```python
cidade = input("Digite a cidade onde você mora: ")
print(f"Você mora em {cidade}!")
```

📌 **Entrada numérica: Convertendo para `int` e `float`**
Como `input()` sempre retorna uma  **string** , precisamos converter para números caso necessário:

```python
idade = int(input("Digite sua idade: "))  # Converte para inteiro
altura = float(input("Digite sua altura em metros: "))  # Converte para float
print(f"Idade: {idade}, Altura: {altura}m")
```

Se o usuário digitar um valor que não pode ser convertido (ex: "abc" para um número), o programa dará erro.

---

### 🔹 **3. Saída de Dados com `print()`**

A função `print()` exibe informações no terminal.

📌 **Concatenando strings e variáveis no `print()`**

```python
nome = "Italo"
idade = 28
print("Meu nome é " + nome + " e tenho " + str(idade) + " anos.")
```

🔹 Melhor forma: **Usando f-strings** (Python 3.6+)

```python
print(f"Meu nome é {nome} e tenho {idade} anos.")
```

🔹 Outra alternativa: **Método `.format()`**

```python
print("Meu nome é {} e tenho {} anos.".format(nome, idade))
```

---

### 🔹 **4. Lidando com Vários Inputs de uma Vez**

Você pode pedir **vários valores** separados por espaço usando `split()`:

```python
nome, idade = input("Digite seu nome e idade separados por espaço: ").split()
print(f"Seu nome é {nome} e você tem {idade} anos.")
```

> 📝 `split()` separa a string em uma  **lista de palavras** , e podemos armazenar cada valor em variáveis.

Se for um número:

```python
a, b = map(int, input("Digite dois números: ").split())
soma = a + b
print(f"A soma de {a} e {b} é {soma}")
```

---

## **🎯 Desafio Prático**

Agora que você aprendeu a trabalhar com  **entrada e saída** , implemente os desafios abaixo:

### **✅ Parte 1: Entrada e Saída Simples**

1. Peça para o usuário  **digitar seu nome, idade e cidade** .
2. Exiba uma mensagem personalizada, como:
   ```
   Olá, João! Você tem 25 anos e mora em São Paulo.
   ```

### **✅ Parte 2: Operações Matemáticas**

1. Peça dois números ao usuário.
2. Realize as operações  **soma, subtração, multiplicação e divisão** .
3. Exiba os resultados.

📌 **Saída esperada**

```
Digite dois números: 10 5
Soma: 15
Subtração: 5
Multiplicação: 50
Divisão: 2.0
```

### **✅ Parte 3: Classificação**

1. Peça ao usuário sua idade.
2. Classifique se ele é  **criança (0-12 anos), adolescente (13-17), adulto (18-59) ou idoso (60+)** .

📌 **Exemplo de Saída**

```
Digite sua idade: 20
Você é um adulto.
```

---

## **🚀 Bônus (Desafio Extra)**

* Pergunte ao usuário a **temperatura em Celsius** e converta para Fahrenheit usando:
  ```
  Fahrenheit = Celsius × 1.8 + 32
  ```
* Crie um **sistema de cadastro** que peça nome, email e telefone e exiba um resumo.

---

## **💡 Dicas Extras**

✅ **Evite erros com `try-except`**

```python
try:
    idade = int(input("Digite sua idade: "))
    print(f"Sua idade é {idade}.")
except ValueError:
    print("Erro! Digite um número inteiro válido.")
```

✅ **Use `end=` e `sep=` no `print()`**

```python
print("Python", "é", "incrível", sep=" - ")  # Saída: Python - é - incrível
print("FIM", end="!!!\n")  # Adiciona "!!!" ao final da linha
```

---

## **🔎 Conclusão**

🎯 Hoje você aprendeu:
✅ Como usar `input()` para entrada de dados

✅ Como usar `print()` para exibir informações

✅ Como converter tipos de dados (`int`, `float`)

✅ Como lidar com múltiplas entradas e formatação de saída

Agora, pratique os desafios e compartilhe seu código! 🚀
