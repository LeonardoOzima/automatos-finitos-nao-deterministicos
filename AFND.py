def AFND_com_rastro(M, cadeia):
    (Q, Sigma, delta, q0, F) = M

    def epsilon_fecho(estados_com_caminho):
        resultado = set()
        pilha = list(estados_com_caminho)
        while pilha:
            (estado, caminho) = pilha.pop()
            resultado.add((estado, caminho))
            for prox in delta.get((estado, ''), []):
                novo_caminho = caminho + (f"ε→{prox}",)
                if (prox, novo_caminho) not in resultado:
                    pilha.append((prox, novo_caminho))
        return resultado

    print(f"\n Testando cadeia: '{cadeia}'")

    estados_atuais = epsilon_fecho({(q0, (q0,))})

    for simbolo in cadeia:
        proximos_estados = set()
        for (estado, caminho) in estados_atuais:
            for prox in delta.get((estado, simbolo), []):
                novos = epsilon_fecho({(prox, caminho + (f"{simbolo}→{prox}",))})
                proximos_estados.update(novos)
        estados_atuais = proximos_estados

    for (estado, caminho) in estados_atuais:
        if estado in F:
            print(" Caminho aceito:")
            for passo in caminho:
                print(" ", passo)
            return True
    print(" Cadeia rejeitada.")
    return False



Q = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8'}
Sigma = {'a', 'b'}
delta = {
    # Transições ε a partir de q0 para os três caminhos
    ('q0', ''): ['q1', 'q3', 'q5'],

    # Caminho 1 – número ímpar de 'a'
    ('q1', 'a'): ['q2'],
    ('q1', 'b'): ['q1'],
    ('q2', 'a'): ['q1'],
    ('q2', 'b'): ['q2'],

    # Caminho 2 – número ímpar de símbolos
    ('q3', 'a'): ['q4'],
    ('q3', 'b'): ['q4'],
    ('q4', 'a'): ['q3'],
    ('q4', 'b'): ['q3'],

    # Caminho 3 – contém substring 'aaa'
    ('q5', 'a'): ['q5', 'q6'],
    ('q5', 'b'): ['q5'],
    ('q6', 'a'): ['q7'],
    ('q7', 'a'): ['q8'],
    ('q8', 'a'): ['q8'],
    ('q8', 'b'): ['q8'],
}

q0 = 'q0'
F = {'q2', 'q4', 'q8'}

M = (Q, Sigma, delta, q0, F)

cadeia1 = "ababab"        # Caminho 1 → número ímpar de 'a'
cadeia2 = "babab"      # Caminho 2 → número ímpar de símbolos
cadeia3 = "baaabbabab"     # Caminho 3 → contém substring "aaa"

AFND_com_rastro(M, cadeia1)
AFND_com_rastro(M, cadeia2)
AFND_com_rastro(M, cadeia3)
