def fair_sharer(values, num_iterations, share=0.1):
    """
    Runs num_iterations.
    In each iteration the highest value in "values" gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neighbor of the rightmost field.

    Examples:
        fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
        fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]

    Args:
        values: 1D array of values (list or numpy array)
        num_iterations: number of iterations (int)
        share: fraction given to each neighbor (float)

    Returns:
        values_new: updated list (same type-like: list)
    """

    # Kopie, damit input nicht verändert wird
    values_new = list(values)

    for _ in range(num_iterations):
        # 1) max_val und index der größten Zahl finden
        max_val = max(values_new)
        idx = values_new.index(max_val)

        # 2) Indizes der Nachbarn bestimmen (Ring: links/rechts mit wrap-around)
        left_idx = (idx - 1) % len(values_new)
        right_idx = (idx + 1) % len(values_new)

        # 3) Betrag berechnen, der an jeden Nachbarn geht
        amount = int(max_val * share)

        # 4) Betrag zu den Nachbarn addieren
        values_new[left_idx] += amount
        values_new[right_idx] += amount

        # 5) Wert bei idx anpassen (er gibt zwei mal amount ab)
        values_new[idx] -= 2 * amount

    return values_new

print(fair_sharer([0, 1000, 800, 0], 1))
print(fair_sharer([0, 1000, 800, 0], 2))

