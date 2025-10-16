def koordinates(pos):
    # Преобразуем число 1-9 в координаты на доске
    # Позиции:
    # 1 2 3
    # 4 5 6
    # 7 8 9
    if pos < 1 or pos > 9:
        return None
    row = (pos - 1) // 3
    col = (pos - 1) % 3
    return row, col