

# 两数相除

def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    positive = (dividend < 0) == (divisor < 0)
    if dividend < 0:
        dividend = ~dividend + 1
    if divisor < 0:
        divisor = ~divisor + 1

    dpower = divisor
    power = 1
    while dpower < dividend:
        dpower <<= 1
        power <<= 1
    if dpower > dividend:
        dpower >>= 1
        power >>= 1

    decomposed = dpower
    fraction = power
    while power:
        dpower >>= 1
        power >>= 1
        if dpower + decomposed <= dividend:
            decomposed += dpower
            fraction += power
        if decomposed == dividend:
            break
    if not positive:
        fraction = ~fraction + 1
    MAX = 0x7FFFFFFF  #7 = 0111 首位符号位，表示最大的int整数
    MIN = -0x80000000 # 最小的int整数
    MASK = 0xFFFFFFFF
    FILL = ~MASK
    return min(MAX, max(fraction, MIN))
