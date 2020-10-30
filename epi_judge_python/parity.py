from test_framework import generic_test

# Brute force approach 
# def parity(x: int) -> int:
#     result = 0 
#     while x:
#         result ^= x & 1 
#         x >>= 1
#     return result 

# 1st Alternative approach 
# def parity(x: int) -> int:
#     result = 0
#     while x: 
#         result ^= 1 
#         x &= x - 1 #Drops the lowest set bit of x. 
#     return result 

# 2nd Alternative approach using XOR and Associativity 
def parity(x: int) -> int:
    x ^= x >> 32 
    x ^= x >> 16
    x ^= x >> 8 
    x ^= x >> 4 
    x ^= x >> 2 
    x ^= x >> 1 
    return x & 0x1 

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
