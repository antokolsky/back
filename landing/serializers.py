from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
    SerializerMethodField
)

from landing.models import (
    ActivityType,
    LandingProject,
    ProjectImage,
    Respondent,
    SculptureOrder
)


class ActivityTypeSerializer(ModelSerializer):
    class Meta:
        model = ActivityType
        fields = '__all__'


class RespondentReadSerializer(ModelSerializer):
    activity_type = PrimaryKeyRelatedField(
        source='activity_type.name', read_only=True
    )

    class Meta:
        model = Respondent
        fields = '__all__'


class RespondentWriteSerializer(ModelSerializer):

    class Meta:
        model = Respondent
        fields = '__all__'


class ProjectImageSerializer(ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = '__all__'


class LandingProjectSerializer(ModelSerializer):
    images = SerializerMethodField()

    def get_images(self, obj):
        return ProjectImageSerializer(
            ProjectImage.objects.filter(project_id=obj.id), many=True
        ).data

    class Meta:
        model = LandingProject
        fields = (
            'author_name',
            'title',
            'dimension_height',
            'dimension_width',
            'dimension_depth',
            'cost',
            'rating',
            'images',
        )


class SculptureOrderSerializer(ModelSerializer):
    class Meta:
        model = SculptureOrder
        fields = '__all__'
