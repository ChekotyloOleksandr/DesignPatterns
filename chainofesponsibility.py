import re
import luhn


class Validator:
    def __init__(self, successor=None):
        self.successor = successor

    def validate(self, input_data):
        if self.successor:
            return self.successor.validate(input_data)
        return False


class CardNumberValidator(Validator):
    def validate(self, input_data):
        if re.match(r"^[0-9]{16}$", input_data) and luhn.verify(input_data):
            return True
        else:
            return super().validate(input_data)


class CardExpirationValidator(Validator):
    def validate(self, input_data):
        if re.match(r"^(0[1-9]|1[0-2])\/([0-9]{2})$", input_data):
            return True
        else:
            return super().validate(input_data)


class CardCVVValidator(Validator):
    def validate(self, input_data):
        if re.match(r"^[0-9]{3}$", input_data):
            return True
        else:
            return super().validate(input_data)


if __name__ == '__main__':
    card_cvv_validator = CardCVVValidator(CardExpirationValidator(CardNumberValidator()))
    if card_cvv_validator.validate("4111111111111111") and card_cvv_validator.validate(
            "12/23") and card_cvv_validator.validate("123"):
        print('Valid')
    # print(card_cvv_validator.validate("4111111111111111"))
    # print(card_cvv_validator.validate("12/23"))
    # print(card_cvv_validator.validate("123"))
