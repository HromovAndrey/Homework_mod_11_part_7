# Завдання 3
#  Завдання для функторів. Створіть клас TextModifier,
# який може здійснювати різні операції над текстом:
# • Операція перетворення тексту у верхній регістр.
# • Операція перетворення тексту у нижній регістр.
# • Операція видалення пробілів у тексті.
# • Операція шифрування тексту за допомогою зсуву
# вліво на задану кількість символів.

class TextModifier:
    def __init__(self, text):
        self.text = text

    def to_upper(self):
        self.text = self.text.upper()

    def to_lower(self):
        self.text = self.text.lower()

    def remove_spaces(self):
        self.text = self.text.replace(" ", "")

    def encrypt(self, shift):
        encrypted_text = ""
        for char in self.text:
            if char.isalpha():
                shifted_char = chr(((ord(char) - 97 + shift) % 26) + 97) if char.islower() else chr(((ord(char) - 65 + shift) % 26) + 65)
                encrypted_text += shifted_char
            else:
                encrypted_text += char
        self.text = encrypted_text


modifier = TextModifier("Hello, World!")

modifier.to_upper()
print("Text in uppercase:", modifier.text)

modifier.to_lower()
print("Text in lowercase:", modifier.text)

modifier.remove_spaces()
print("Text without spaces:", modifier.text)

modifier.encrypt(3)
print("Encrypted text:", modifier.text)
