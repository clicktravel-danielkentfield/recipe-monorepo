from rest_framework import serializers
from app.core.models import Ingredient, Recipe


class IngredientSerializer(serializers.Serializer):
    """Serializer for ingredients"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)


class RecipeSerializer(serializers.Serializer):
    """Serializer for recipe objects"""

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.name
    )

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'description', 'ingredients')
        read_only_fields = ('id',)

