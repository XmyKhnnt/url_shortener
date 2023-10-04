from rest_framework import serializers
from .models import Link
import random
import string

class LinkSerializer(serializers.ModelSerializer):
    """
    Serializer for the Link model.
    """

    class Meta:
        model = Link
        fields = ['links']

    def generate_shorten_prefix(self):
        """
        Generates a random and unique shorten_prefix with a maximum length of 5 characters.

        Returns:
            str: A unique shorten_prefix.
        """
        while True:
            shorten_prefix = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
            if not Link.objects.filter(shorten_prefix=shorten_prefix).exists():
                return shorten_prefix

    def create(self, validated_data):
        """
        Custom create method for the Link serializer.
        Generates a unique shorten_prefix before creating a new link.

        Args:
            validated_data (dict): Validated data containing link information.

        Returns:
            Link: The created Link object.
        """
        validated_data['shorten_prefix'] = self.generate_shorten_prefix()
        link = Link.objects.create(**validated_data)
        return link
