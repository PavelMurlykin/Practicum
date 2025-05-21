class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet_len = len(alphabet)

    def cipher(self, original_text, shift):
        result = []
        for letter in original_text:
            if self.alphabet.find(letter.lower()) == -1:
                result.append(letter)
            else:
                result.append(self.alphabet[(self.alphabet.find(
                    letter.lower()) + shift) % self.alphabet_len])
        return ''.join(result)

    def decipher(self, cipher_text, shift):
        result = []
        for letter in cipher_text:
            if self.alphabet.find(letter.lower()) == -1:
                result.append(letter)
            else:
                result.append(self.alphabet[(self.alphabet.find(
                    letter.lower()) - shift) % self.alphabet_len])
        return ''.join(result)

    def process_text(self, text, shift, is_encrypt):
        result = []

        if not is_encrypt:
            shift = -shift

        for letter in text:
            if self.alphabet.find(letter.lower()) == -1:
                result.append(letter)
            else:
                result.append(self.alphabet[(self.alphabet.find(
                    letter.lower()) + shift) % self.alphabet_len])
        return ''.join(result)


cipher_master = CipherMaster()

print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))

print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))
