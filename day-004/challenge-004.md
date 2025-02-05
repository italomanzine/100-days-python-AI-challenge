## **📌 Desafio do Dia 04: Estruturas de Controle - Condicionais**

### **✅ Objetivo**

Criar um programa que receba um número do usuário e utilize estruturas condicionais (`if`, `elif` e `else`) para determinar se o número é  **positivo** , **negativo** ou  **zero** .

---

## **🚀 Instruções do Desafio**

1. **Entrada de Dados:**
   * Peça ao usuário para digitar um número (lembre-se de converter a entrada para um tipo numérico, como `int` ou `float`).
2. **Estruturas Condicionais:**
   * Utilize a estrutura `if` para verificar se o número é maior que zero (positivo).
   * Use `elif` para verificar se o número é menor que zero (negativo).
   * Por fim, use `else` para o caso em que o número é exatamente zero.
3. **Saída de Dados:**
   * Exiba uma mensagem informando se o número é positivo, negativo ou zero.

---

## **📚 Breve Aula: Estruturas Condicionais em Python**

### 🔹 **1. Introdução às Condicionais**

Em Python, as estruturas condicionais permitem que o programa tome decisões com base em certas condições. A sintaxe básica é:

```python
if condição:
    # bloco de código executado se a condição for verdadeira
elif outra_condição:
    # bloco executado se a primeira condição for falsa e essa for verdadeira
else:
    # bloco executado se nenhuma das condições anteriores for verdadeira
```

### 🔹 **2. Exemplo Prático: Verificando se um Número é Positivo, Negativo ou Zero**

Vamos ver um exemplo simples:

```python
# Recebendo o número do usuário e convertendo para float
numero = float(input("Digite um número: "))

# Verificando se o número é positivo, negativo ou zero
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
```

#### **Explicação:**

* **Entrada de Dados:**

  Usamos `input()` para receber o valor digitado pelo usuário e convertemos para `float` para permitir tanto inteiros quanto decimais.
* **Condição `if`:**

  Verificamos se o número é maior que zero. Se for verdadeiro, o programa executa o bloco logo abaixo e ignora os demais.
* **Condição `elif`:**

  Se a condição anterior for falsa, checamos se o número é menor que zero. Se sim, esse bloco é executado.
* **Condição `else`:**

  Caso nenhuma das condições anteriores seja satisfeita (ou seja, o número é exatamente zero), o bloco `else` é executado.

### 🔹 **3. Dicas para Trabalhar com Condicionais**

* **Indentação:**

  Em Python, a indentação define o bloco de código. Certifique-se de que todas as linhas dentro de um bloco condicional estejam alinhadas corretamente.
* **Clareza na Condição:**

  Use condições claras e, se necessário, comente o código para explicar a lógica.
* **Testes:**

  Teste seu programa com diferentes entradas (números positivos, negativos e zero) para garantir que todas as condições estejam funcionando conforme esperado.
* **Conversão de Tipos:**

  Lembre-se de converter a entrada do usuário para o tipo numérico adequado, pois `input()` retorna sempre uma string.

---

## **🎯 Desafio Prático**

1. **Peça ao usuário que insira um número:**
   * Exemplo: "Digite um número: "
2. **Verifique e exiba:**
   * Se o número for maior que zero, exiba: "O número é positivo."
   * Se o número for menor que zero, exiba: "O número é negativo."
   * Se o número for zero, exiba: "O número é zero."
3. **(Bônus) Extendendo o Desafio:**
   * Peça ao usuário que insira outro número e, em seguida, utilize condicionais para comparar os dois números, exibindo qual deles é maior ou se são iguais.

---

## **💡 Dicas Extras**

* **Teste seu código com casos variados:**

  Experimente com valores como `10`, `-3.5`, `0` e veja se o programa responde corretamente a cada situação.
* **Comentários:**

  Adicione comentários explicativos em seu código para ajudar na compreensão, especialmente se você voltar a ele mais tarde.
* **Formatando a saída:**

  Use f-strings para exibir mensagens mais informativas, como:

  ```python
  print(f"Você digitou o número {numero}, que é {'positivo' if numero > 0 else 'negativo' if numero < 0 else 'zero'}.")
  ```

---

## **🔎 Conclusão**

Hoje você aprendeu:

* **Como receber e converter dados de entrada com `input()`**
* **Como usar estruturas condicionais (`if`, `elif` e `else`) para tomar decisões**
* **A importância de testar seu código com diferentes cenários**

Pratique escrevendo e executando esse desafio, e explore variações para solidificar o seu entendimento sobre as estruturas de controle. Boa prática e continue evoluindo no seu caminho para dominar Python e suas aplicações em IA e Machine Learning!
