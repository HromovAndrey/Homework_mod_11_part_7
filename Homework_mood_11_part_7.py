# Завдання 3
#  Завдання для функторів. Створіть клас TextModifier,
# який може здійснювати різні операції над текстом:
# • Операція перетворення тексту у верхній регістр.
# • Операція перетворення тексту у нижній регістр.
# • Операція видалення пробілів у тексті.
# • Операція шифрування тексту за допомогою зсуву
# вліво на задану кількість символів.
#
# class TextModifier:
#     def __init__(self, text):
#         self.text = text
#
#     def to_upper(self):
#         self.text = self.text.upper()
#
#     def to_lower(self):
#         self.text = self.text.lower()
#
#     def remove_spaces(self):
#         self.text = self.text.replace(" ", "")
#
#     def encrypt(self, shift):
#         encrypted_text = ""
#         for char in self.text:
#             if char.isalpha():
#                 shifted_char = chr(((ord(char) - 97 + shift) % 26) + 97) if char.islower() else chr(((ord(char) - 65 + shift) % 26) + 65)
#                 encrypted_text += shifted_char
#             else:
#                 encrypted_text += char
#         self.text = encrypted_text
#
#
# modifier = TextModifier("Hello, World!")
#
# modifier.to_upper()
# print("Text in uppercase:", modifier.text)
#
# modifier.to_lower()
# print("Text in lowercase:", modifier.text)
#
# modifier.remove_spaces()
# print("Text without spaces:", modifier.text)
#
# modifier.encrypt(3)
# print("Encrypted text:", modifier.text
#
#
# class MyDescriptor:
#    def __get__(self, instance, owner):
#        print("Getting the attribute")
#        print(self)
#        print(instance)
#        print(owner)
#
#    def __set__(self, instance, value):
#        print("Setting the attribute")
#        print(self)
#
# class MyClass:
#    attr = MyDescriptor()
#
# obj = MyClass()
# obj.attr
# class MyDescriptor:
#     def __get__(self, amount):
#         self._amount = amount
#
#     def __set__(self, instance, owner):
#         return self._amount
#
#
# class  FinancialData:
#     amount = MyDescriptor(10)
#
# obj = FinancialData()
# print(obj.amount)



# class Positive:
#     def __init__(self, instange, value):
#         print(instange, value)
#
#     def __set__(self, instange):
#        if instange < 0:
#          raise ValueError()
#        amount = instange
#
# class Order:
#     product = "milk"
#     amount = Positive
# order = Order()
# print(order.amount)
#
#
# class Positive:
#     def __get__(self, instange, owner):
#         return instange._amount
#
#     def __set__(self, instange, value):
#         if value < 0:
#             raise ValueError()
#         instange._amount = value
#
# class Order:
#     product = "milk"
#     amount  = Positive
#
#
# order = Order()
# order.amount = -3
# print(order.__set__._amount)


class Order:
    product = "Milk"
    amount = 0

    def set_amount(self, value):
        if value < 0:
            raise ValueError()
        self._amount = value

order = Order()
order.set_amount(10)
print(order.set_amount, order.product)

