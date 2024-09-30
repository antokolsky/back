from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from landing.models import ActivityType, Respondent, LandingProject


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


class LandingProjectSerializer(ModelSerializer):
    class Meta:
        model = LandingProject
        fields = '__all__'
