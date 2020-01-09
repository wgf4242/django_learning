from rest_framework import serializers

from apps.mdself.models import Category


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


# class CategorySerializer(serializers.ModelSerializer):
#     parentCategory = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), allow_empty=True, allow_null=True)
#
#     class Meta:
#         model = Category
#         fields = ('parentCategory', 'name', 'description', 'subcategories')
#
#         def get_related_field(self, model_field):
#             # Handles initializing the `subcategories` field
#             return CategorySerializer()

class CategorySerializer(serializers.ModelSerializer):
    # subcategories = RecursiveField(many=True)

    class Meta:
        model = Category
        fields = '__all__'
        # fields = ('parentCategory', 'name', 'description', 'subcategories')

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['subcategories'] = CategorySerializer(many=True)
        return fields

# CategorySerializer._declared_fields['subcategories'] = CategorySerializer()
