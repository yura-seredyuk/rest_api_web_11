import re
from rest_framework import serializers



class AddressValidator:
    message = "Validation error: "
    def __init__(self, message=None):
        self.validated_field = ''
        self.validated_data = None
        self.message = message or self.message

    def __call__(self, attrs):
        message = self.message
        zip_code_pattern = re.compile('^\d{4,}\-?\d{0,}$')
        house_num_pattern = re.compile('^\d{1,}[\-?||\s?||\/?]?[\d+]?[a-zA-Zа-щА-ЩЬьЮюЯяЇїІіЄєҐґ]*$')
        if 'apartaments' in attrs and attrs['apartaments'] <= 0:
            message = 'cannote be less or equal zero'
            self.raize_error(attrs, 'apartaments', message)
        if 'country' in attrs:
            self.name_validation(attrs, 'country')
        if 'street' in attrs:
            self.name_validation(attrs, 'street')
        if 'city' in attrs:
            self.name_validation(attrs, 'city')
        if 'zip_code' in attrs:
            if len(attrs['zip_code']) < 4:
                message = 'must consists with more than 4 characters'
                self.raize_error(attrs, 'zip_code', message)  
            elif not re.search(zip_code_pattern, attrs['zip_code']):
                message = 'can consists only digits or dash symbol'
                self.raize_error(attrs, 'zip_code', message)
        if 'house_num' in attrs:
            if not re.search(house_num_pattern, attrs['house_num']):
                message = 'data does not match the pattern'
                self.raize_error(attrs, 'house_num', message)

    def raize_error(self, attrs, validated_field, message):
        message = self.message + f"The '{validated_field}' field {message}."
        self.validated_field = validated_field
        self.validated_data = attrs[validated_field]
        raise serializers.ValidationError(message, code=validated_field)
    
    def name_validation(self, attrs, field):
        text_pattern_en = re.compile('^[A-Za-z]+$')
        text_pattern_ua = re.compile('^[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ]+$')

        if len(attrs[field]) < 3 and field != 'city':
            message = 'must consists with more than 2 characters'
            self.raize_error(attrs, field, message)  
        elif not re.search(text_pattern_en, attrs[field]) and\
            not re.search(text_pattern_ua, attrs[field]):
            message = 'can consists only ua or en characters'
            self.raize_error(attrs, field, message)

    def __repr__(self):
        return f'<{self.__class__.__name__}({self.validated_field}={self.validated_data})>'