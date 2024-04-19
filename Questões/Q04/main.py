import math

try:
    area = float(input("Informe o tamanho da área a ser pintada em metros quadrados: "))
    cobertura_por_lata = 18 * 3  # 18 litros cobrem 54 metros quadrados
    quantidade_latas = math.ceil(area / cobertura_por_lata)
    preco_por_lata = 80.00
    preco_total = quantidade_latas * preco_por_lata

    print("\nQuantidade de latas necessárias:", quantidade_latas)
    print("Preço total: R$", preco_total)

except ValueError:
    print("Por favor, informe um valor numérico para a área.")