from django.db import models

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE,related_name = 'profile')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='profile/')


    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles

class Location(models.Model):
    name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name

    #     class Category(models.Model):
    # name = models.CharField(max_length=30)

    # def save_category(self):
    #     self.save()

    # def delete_category(self):
    #     self.delete()

    # def __str__(self):
    #     return self.name
