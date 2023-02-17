from django.db import models

# Create your models here.
class HTMLModel(models.Model):
    clients = models.PositiveIntegerField(default=0)
    projects = models.PositiveIntegerField(default=0)
    support = models.PositiveIntegerField(default=0)
    workers = models.PositiveIntegerField(default=0)

    html_skills_percentage = models.PositiveIntegerField(default=0)
    css_skills_percentage = models.PositiveIntegerField(default=0)
    js_skills_percentage = models.PositiveIntegerField(default=0)
    py_skills_percentage = models.PositiveIntegerField(default=0)
    db_skills_percentage = models.PositiveIntegerField(default=0)

#   Creating testimonial models with predefined scores
class Testimonials(models.Model):
    AVAILABLE_SCORES_RANGE = (
        (1, "Awful"),
        (2, "Bad"),
        (3, "Regular"),
        (4, "Good"),
        (5, "Exelent"),
    )
    full_name = models.CharField(max_length=80)
    score = models.PositiveSmallIntegerField(choices=AVAILABLE_SCORES_RANGE, default=5)
    comments = models.TextField(max_length=500)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
