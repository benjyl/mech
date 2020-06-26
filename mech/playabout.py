def factorial(x: int) -> int:
    """[summary]

    Args:
        x (int): [description]

    Returns:
        int: [description]
    """
    return x * factorial(x - 1) if x > 1 else 1
