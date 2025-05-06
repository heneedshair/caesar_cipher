class CaesarCipherModel:
    def __init__(self):
        self.shift = 3
        self.direction = 'вправо'

    def set_parameters(self, shift: int, direction: str):
        self.shift = shift
        self.direction = direction

    def _shift_char(self, char: str, shift: int) -> str:
        if char.isalpha() and char.isascii():
            base = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - base + shift) % 26 + base)
        return char

    def encrypt(self, text: str) -> str:
        shift = self.shift if self.direction == 'вправо' else -self.shift
        return ''.join(self._shift_char(c, shift) for c in text)

    def decrypt(self, text: str) -> str:
        shift = -self.shift if self.direction == 'вправо' else self.shift
        return ''.join(self._shift_char(c, shift) for c in text)
