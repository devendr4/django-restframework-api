from django.db import models


class Skill(models.Model):
    LANGUAGE = 'LNG'
    FRAMEWORK = 'FRM'
    DATABASE = 'DB'
    SKILL_TYPES = (
        (FRAMEWORK, 'Framework'),
        (LANGUAGE, 'Language'),
        (DATABASE, 'Database'))
    KNOWLEDGE = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    name = models.CharField(max_length=15, blank=False, default='')
    date_added = models.DateField(auto_now_add=True)
    knowledge = models.IntegerField(default=3, choices=KNOWLEDGE)
    skill_type = models.CharField(choices=SKILL_TYPES, max_length=15)
