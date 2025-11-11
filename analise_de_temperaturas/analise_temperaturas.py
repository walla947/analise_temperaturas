def validar_e_obter_temperatura(nome_mes, temp_minima=-60.0, temp_maxima=50.0):
    while True:
        try:
            entrada = input(f"Digite a temperatura máxima de {nome_mes} em Celsius: ")

            entrada = entrada.replace(',', '.')

            temperatura = float(entrada)

            if temp_minima <= temperatura <= temp_maxima:
                return temperatura
            else:
                print(
                    f"\n[ERRO] Temperatura de {temperatura}°C é inválida. O valor deve estar entre {temp_minima}°C e {temp_maxima}°C.")
                print("Por favor, digite novamente.\n")

        except ValueError:
            print("\n[ERRO] Entrada inválida. Por favor, digite um número (ex: 34.3 ou 25).\n")


def executar_analise():
    NOMES_MESES = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]

    temperaturas = []
    total_temperaturas = 0.0
    contagem_meses_escaldantes = 0
    temp_maxima_anual = None
    temp_minima_anual = None
    indice_mes_mais_quente = -1
    indice_mes_menos_quente = -1


    print("Análise de Dados Meteorológicos Anuais (2021)")
    print("Temperaturas máximas devem estar entre -60°C e 50°C.")


    for i in range(12):
        numero_mes = i + 1
        nome_mes = NOMES_MESES[i]

        print(f"\nMês {numero_mes}/12: {nome_mes}")

        temp_max_mes = validar_e_obter_temperatura(nome_mes)

        temperaturas.append(temp_max_mes)

        total_temperaturas += temp_max_mes

        if temp_max_mes > 33.0:
            contagem_meses_escaldantes += 1

        if temp_maxima_anual is None or temp_max_mes > temp_maxima_anual:
            temp_maxima_anual = temp_max_mes
            indice_mes_mais_quente = i

        if temp_minima_anual is None or temp_max_mes < temp_minima_anual:
            temp_minima_anual = temp_max_mes
            indice_mes_menos_quente = i

    print("")
    print("Resultados da Análise Anual:")
    print("----------------------------")
    print("")

    media_maxima_anual = total_temperaturas / 12
    print(f"Temperatura Média Máxima Anual: {media_maxima_anual:.2f} °C")

    print(f"Quantidade de Meses Escaldantes (> 33°C): {contagem_meses_escaldantes}")

    if indice_mes_mais_quente != -1:
        mes_mais_quente = NOMES_MESES[indice_mes_mais_quente]
        print(f"Mês Mais Escaldante (Máx: {temp_maxima_anual:.1f}°C): {mes_mais_quente}")

    if indice_mes_menos_quente != -1:
        mes_menos_quente = NOMES_MESES[indice_mes_menos_quente]
        print(f"Mês Menos Quente (Mín: {temp_minima_anual:.1f}°C): {mes_menos_quente}")




if __name__ == "__main__":
    executar_analise()