import math
import pyprimes
import random


def generate_keypair():
    primes =list(pyprimes.nprimes(10000))
    first_index = random.randrange(0, len(primes))
    second_index = random.randrange(0, len(primes))
    if second_index == first_index:
        second_index = second_index + 1
    p = primes[first_index]
    q = primes[second_index]
    K = p * q
    e = 65537
    print(p)
    print(q)
    phi = (p-1) * (q-1)
    k = inverse(e, phi)

    print(k)
    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, K), (k, K))

def encrypt(key, message):
    e,K = key
    result = []
    for char in message:
        char_encrypted = pow(ord(char), e, K)
        result.append(char_encrypted)
    return result


def decrypt(key, message):
    k, K = key
    result = ''
    for char in message:
        char_decrypted = chr(pow(char, k, K))
        result = result + str(char_decrypted)
    return result


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def inverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m
