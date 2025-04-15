# AFND com Rastro (AFND_com_rastro)

Este repositório contém uma implementação em Python de um **Autômato Finito Não Determinístico (AFND)** com suporte a **ε-transições** e **rastreamento dos caminhos** percorridos para aceitação de cadeias.

## 💡 Descrição

A função `AFND_com_rastro` simula um AFND com ε-transições, retornando se uma cadeia é aceita e exibindo o caminho percorrido até um estado final (caso haja). A implementação utiliza o conceito de **fecho-ε** para explorar todos os caminhos possíveis.

## 🧠 Lógica da Função

1. Calcula o fecho-ε para os estados iniciais.
2. Para cada símbolo da cadeia, expande os caminhos possíveis a partir dos estados atuais.
3. Após o processamento da cadeia, verifica se algum estado atual é final.
4. Caso sim, exibe o caminho percorrido (com transições e ε-movimentos).

## 🧪 Exemplo de Máquina

A máquina reconhece cadeias que:
- **(Caminho 1)** possuem número ímpar de `'a'`
- **(Caminho 2)** possuem número ímpar de símbolos
- **(Caminho 3)** contêm a substring `"aaa"`

## 🔢 Testes Realizados

```python
AFND_com_rastro(M, "ababab")       # Caminho 1 – número ímpar de 'a'
AFND_com_rastro(M, "babab")        # Caminho 2 – número ímpar de símbolos
AFND_com_rastro(M, "baaabbabab")   # Caminho 3 – contém substring "aaa"
```

## 📁 Estrutura do AFND

- `Q`: conjunto de estados
- `Σ`: alfabeto de entrada
- `δ`: função de transição (incluindo transições ε)
- `q0`: estado inicial
- `F`: conjunto de estados finais

## 📜 Licença

Este código é parte de um estudo acadêmico e pode ser usado livremente para fins educacionais.

---
Desenvolvido durante estudos de Teoria da Computação 📚
