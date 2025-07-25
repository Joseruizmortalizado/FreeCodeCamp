def arithmetic_arranger(problems, display_result=False):
    # Validar el número de problemas
    if len(problems) > 5:
        return "Error: Too many problems."

    # Inicializar listas para cada línea del resultado
    top_row = []
    bottom_row = []
    separators = []
    results = []

    for prob in problems:
        # Separar operandos y operador
        try:
            left, op, right = prob.split()
        except ValueError:
            return "Error: Each problem must have two operands and one operator."

        # Validaciones
        if op not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if not (left.isdigit() and right.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determinar el ancho necesario (longitud del número más largo + 2)
        width = max(len(left), len(right)) + 2

        # Formatear cada parte del problema
        top_row.append(left.rjust(width))
        bottom_row.append(op + right.rjust(width - 1))
        separators.append('-' * width)

        # Si se debe mostrar el resultado, calcularlo
        if display_result:
            if op == '+':
                res = int(left) + int(right)
            else:
                res = int(left) - int(right)
            results.append(str(res).rjust(width))

    # Combinar las líneas con 4 espacios de separación
    arranged = '    '.join(top_row) + '\n' + \
               '    '.join(bottom_row) + '\n' + \
               '    '.join(separators)

    if display_result:
        arranged += '\n' + '    '.join(results)

    return arranged
