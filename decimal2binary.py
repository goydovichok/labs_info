def decimal2binary(x):
    return [int(bit) for bit in bin(x)[2:].zfill(8)]