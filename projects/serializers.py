from rest_framework import serializers
from .models import Project, Style, Material


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id', 'name_ru', 'name_en', 'avatar', 'other_photos', 'style', 'material',
            'description_ru', 'description_en', 'prepayment', 'cost_of_project', 'total_cost',
            'address', 'created_at', 'updated_at', 'author_id', 'is_moderated'
        ]
        read_only_fields = [
            'name_en', 'description_en', 'prepayment', 'total_cost',
            'created_at', 'updated_at', 'author', 'is_moderated'
        ]


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'
