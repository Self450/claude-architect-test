def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number.

    Args:
        n: Non-negative integer index into the Fibonacci sequence,
           where fibonacci(0) == 0 and fibonacci(1) == 1.

    Returns:
        The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
