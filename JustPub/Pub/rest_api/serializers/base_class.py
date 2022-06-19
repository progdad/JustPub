from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer


class BaseSerializerClass(ModelSerializer):
    @staticmethod
    def validate_name(name):
        if not name.replace(" ", "").replace("-", "").isalnum():
            raise ValidationError(
                "'name' field may contain only letters, numbers, dashes and spaces. Change it, please !"
            )
        return name
