while True:
    try:
      entrada = input()
      if entrada == 'esquerda':
        print('ingles')
      elif entrada == 'direita':
        print('frances')
      elif entrada == 'nenhuma':
        print('portugues')
      elif entrada == 'ambas':
        print('caiu')
    except EOFError:
        break