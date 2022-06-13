from turtle import title
from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils.text import slugify
from random import randint
from ckeditor.fields import RichTextField

# Create your models here.


class BaseModel(models.Model):
    uuid = models.UUIDField(
        editable=False, primary_key=True, default=uuid.uuid4, null=False
    )
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class PersonalInfo(BaseModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField()
    message = models.CharField(max_length=500)
    desc = models.TextField()

    image = models.ImageField(upload_to="profile/", blank=True)

    def __str__(self):
        return f"{self.first_name} , {self.last_name}"


class PersonalDetailInfo(BaseModel):
    person = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE)
    CHOICES = (("Available", "Available"), ("", "UnAvailable"))
    nationality = models.CharField(max_length=100)
    freelance = models.CharField(max_length=200, choices=CHOICES)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    langauge = models.CharField(max_length=200)
    expreience = models.CharField(max_length=100)
    complete_project = models.PositiveIntegerField()
    happy_customer = models.PositiveIntegerField()
    award_won = models.PositiveIntegerField()
    phonenumber = models.CharField(max_length=20)
    cv = models.FileField(upload_to="cv/", blank=True)

    def __str__(self) -> str:
        return self.person.first_name


class Skill(BaseModel):
    person = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    plang = models.CharField(max_length=200)
    level = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.plang


class Education(BaseModel):
    person = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    desc = models.TextField()
    sucess_date = models.DateField()
    instute_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title


class MyPortFolio(BaseModel):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="portimg/", blank=True)
    project = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    langauge = models.CharField(max_length=200)
    preview = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class ContactUs(BaseModel):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.name


class Blog(BaseModel):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blog/", blank=True)
    desc = RichTextField(blank=True,null=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if Blog.objects.filter(title=self.title).exists():
            extra = str(randint(1, 10000))
            self.slug = f"{slugify(self.title)}-{extra}"
        else:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
