from app.app.serializers import RecipeSerializer, IngredientSerializer
from app.app.models import Recipe, Ingredient
from rest_framework import viewsets, mixins


class RecipeViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""

    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

    def get_queryset(self):
        """Retrieve all recipes"""
        queryset = self.queryset
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__contains=name)
        return self.queryset

    def perform_create(self, serializer):
        """Create a recipe"""
        serializer.save()


class IngredientViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Manage ingredients in the database"""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save()
