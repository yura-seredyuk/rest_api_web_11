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
        text_pattern_en = re.compile('^[A-Za-z]+$')
        text_pattern_ua = re.compile('^[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ]+$')
        if 'apartaments' in attrs and attrs['apartaments'] <= 0:
            message = 'cannote be less or equal zero'
            self.raize_error(attrs, 'apartaments', message)
        if 'country' in attrs:
            if len(attrs['country']) < 3:
                message = 'must consists with more than 2 characters'
                self.raize_error(attrs, 'country', message)  
            elif not re.search(text_pattern_en, attrs['country']) and\
                not re.search(text_pattern_ua, attrs['country']):
                message = 'can consists only ua or en characters'
                self.raize_error(attrs, 'country', message)

    def raize_error(self, attrs, validated_field, message):
        message = self.message + f"The '{validated_field}' field {message}."
        self.validated_field = validated_field
        self.validated_data = attrs[validated_field]
        raise serializers.ValidationError(message, code=validated_field)
    
    def __repr__(self):
        return f'<{self.__class__.__name__}({self.validated_field}={self.validated_data})>'