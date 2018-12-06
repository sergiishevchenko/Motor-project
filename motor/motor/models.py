from django.db import models


class User(models.Model):
    class Meta:
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'Пользователь {self.Login}'
    
    GENDER_LIST = [
        ('М', 'Мужской'),
        ('Ж', 'Женский')
    ]

    Login = models.CharField(max_length=30)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Gender = models.CharField(max_length=1, choices=GENDER_LIST)
    Phone = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)
    CreatedDate = models.DateTimeField()
    ModifiedDate = models.DateTimeField()
    # GroupID
    Active = models.BooleanField()
"""
class LoginAttempt(models.Model):
    LoginAttemptID
    UserID
    Password
    IPNumber
    BrowserType
    Success
    LastLogin
    CreatedDate

class Password(models.Model):
    PasswordID
    UserID
    Password
    PasswordQuestion
    PasswordAnswer

class UserGroup(models.Model):
    UserGroupID
    GroupType
    Active


"""