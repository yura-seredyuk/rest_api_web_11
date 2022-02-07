
from rest_framework import serializers


class AddressValidator:
    message = "Validation error: "
    def __init__(self, message=None):
        self.validated_field = ''
        self.validated_data = None
        self.message = message or self.message

    def __call__(self, attrs):
        message = self.message
        if 'apartaments' in attrs and attrs['apartaments'] <= 0:
            message = 'cannote be less or equal zero'
            self.raize_error(attrs, 'apartaments', message)

    def raize_error(self, attrs, validated_field, message):
        message = self.message + f'The {validated_field} field message.'
        self.validated_field = validated_field
        self.validated_data = attrs[validated_field]
        raise serializers.ValidationError(message, code=validated_field)
    
    def __repr__(self):
        return f'<{self.__class__.__name__}({self.validated_field}={self.validated_data})>'