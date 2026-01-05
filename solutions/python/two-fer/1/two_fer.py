def two_fer(name=None):
    if name is None:
        return "One for you, one for me."
    else:
        return f"One for {name}, one for me."