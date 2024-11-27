def minion_game(s: str) -> str:
    vowels = "AEIOU"
    stuart_score = 0
    kevin_score = 0
    n = len(s)

    for i in range(n):
        if s[i] in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i

    if stuart_score > kevin_score:
        return f"Stuart {stuart_score}"
    elif kevin_score > stuart_score:
        return f"Kevin {kevin_score}"
    else:
        return "Draw"
    pass

#juhu