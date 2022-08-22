valor = float(input('Inserir um valor: '))
valorDesconto = valor * 0.9
valorParcelado = valor/3
comissaoVista = valorDesconto * 0.05
comissaoParcelado = valor * 0.05
print(f'Valor à vista: {valorDesconto:.2f}\nValor da parcela (3x): {valorParcelado:.2f}')
print(f'Comissão à vista: {comissaoVista:.2f}\nComissão parcelado: {comissaoParcelado:.2f}')
