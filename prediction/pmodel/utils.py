import math
import pandas as pd


def eval_probability(probability: str, param: dict[str, float]) -> float:
    return eval(probability, {"__builtins__": None}, param)


def prob_pres_get_actual(n: int, num_drawn: int, draw_pile: dict[int, float], tot_cards: int) -> float:
    prob = 0
    for (nlib, p) in draw_pile.items():
        if nlib > tot_cards:
            break
        nfas = tot_cards - nlib
        # math.comb(n, k) returns 0 if f > n, so no need to worry about that case
        prob += p * math.comb(nlib, n) * math.comb(nfas, num_drawn - n) / math.comb(tot_cards, num_drawn)
    return prob
