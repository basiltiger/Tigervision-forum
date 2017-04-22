from django.db import models
from django.forms import forms


# Create your models here.


class ForumCategorie(models.Model):
    cat_nom = models.CharField(max_length=30, null=False)
    cat_ordre = models.IntegerField(unique=True, null=False)


class ForumForum(models.Model):
    forum_cat_id = models.ForeignKey(ForumCategorie, on_delete=models.CASCADE())
    forum_name = models.CharField(max_length=30, null=False)
    forum_desc = models.TextField(null=False)
    forum_ordre = models.PoseitiveIntegerField(null=False)
    forum_last_post_id = models.PositiveIntegerField(null=False)
    forum__topic = models.PositiveIntegerField(null=False)
    forum_post = models.PositiveIntegerField(null=False)
    auth_view = models.PositiveIntegerField(null=False)
    auth_post = models.PositiveIntegerField(null=False)
    auth_topic = models.PositiveIntegerField(null=False)
    auth_annonce = models.PositiveIntegerField(null=False)


class ForumMembres(models.Model):
    membre_pseudo = models.CharField(max_length=30, null=False)
    membre_password = models.CharField(max_length=32, null=False)
    membre_email = models.EmailField(null=False)
    membre_msn = models.CharField(max_length=250, null=False)
    membre_siteweb = models.URLField(null=False)
    membre_avatar = models.ImageField(upload_to="/images", null=False)
    membre_signature = models.CharField(max_length=200, null=False)
    membre_localisation = models.CharField(max_length=100, null=False)
    membre_inscrit = models.PositiveIntegerField(max_length=11, null=False)
    membre_derniere_visite = models.PositiveIntegerField(max_length=11, null=False)
    membre_rang = models.PositiveIntegerField(null=False)
    membre_post = models.PositiveIntegerField(null=False)


class ForumTopic(models.Model):
    form_id = models.ForeignKey(ForumForum, on_delete=models.CASCADE())
    topic_titre = models.CharField(max_length=60, null=False)
    topic_createur = models.PositiveIntegerField(max_length=11, null=False)
    topic_vu = models.PositiveIntegerField(null=False)


class ForumPost(models.Model):
    post_createur = models.PositiveIntegerField(max_length=11, null=False)
    post_texte = models.TextField(null=False)
    post_time = models.PositiveIntegerField(max_length=11, null=False)


class ForumTopic(models.Model):
    forum = models.ForeignKey(ForumForum, on_delete=models.CASCADE())