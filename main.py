def generate_first_number_of_value(value):
    znaleziona = False
    i = 2
    while not (znaleziona):
        pierwsza = True
        for n in range(2, i):
            if i % n == 0:
                pierwsza = False
                break
        if nwd(value, i) == 1:
            znaleziona = True
        else:
            i += 1
    return i


def nwd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_d(phi, e):
    d = 1
    while (e * d) % phi != 1:
        d += 1
    return d


def RSA_encrypton(message, e, n):
    cipher = message**e % n
    return cipher


def RSA_decrypton(cipher, d, n):
    message = cipher**d % n
    return message


def RSA_main():
    p = 1013
    q = 1009
    n = p * q
    phi = (p - 1) * (q - 1)
    e = generate_first_number_of_value(phi)
    message = list(bytearray("for"))
    cipher = []
    print "Klucz publiczny:", e, ",", n
    d = generate_d(phi, e)
    print "Klucz prywatny:", d, ",", n
    print "Message:", message
    for i in range(len(message)):
        cipher.append(int(RSA_encrypton(message[i], e, n)))
    print "Cipher:", cipher
    plaintext = []
    for i in range(len(cipher)):
        plaintext.append(int(RSA_decrypton(cipher[i], d, n)))
    print "Plaintext:", plaintext
    print str(bytearray(plaintext))



RSA_main()
