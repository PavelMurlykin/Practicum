import hashlib
import base64


class MarsURLEncoder:
    def __init__(self):
        self.storage = {}
        self.base_url = 'https://ma.rs/'

    def encode(self, long_url):
        hash_bytes = hashlib.sha256(long_url.encode()).digest()
        hash_value = base64.urlsafe_b64encode(hash_bytes)[:6].decode()

        self.storage[hash_value] = long_url

        return f'{self.base_url}{hash_value}'

    def decode(self, short_url):
        if not short_url.startswith(self.base_url):
            raise ValueError('Некорректная зашифрованная ссылка')

        hash_value = short_url[len(self.base_url):]

        if hash_value in self.storage:
            return self.storage[hash_value]
        else:
            raise KeyError('Ссылка не найдена в хранилище')


if __name__ == '__main__':
    encoder = MarsURLEncoder()

    long_url = 'https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html'
    short_url = encoder.encode(long_url)

    print(f'Зашифрованная (hashlib): {short_url}')
    print(f'Расшифрованная: {encoder.decode(short_url)}')
