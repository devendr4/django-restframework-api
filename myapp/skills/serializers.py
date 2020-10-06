from rest_framework import serializers
from skills.models import Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'date_added', 'knowledge', 'skill_type']
