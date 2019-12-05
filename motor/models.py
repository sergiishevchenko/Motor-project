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

    Login = models.CharField(max_length=30, verbose_name='Логин пользователя')
    FirstName = models.CharField(max_length=30, verbose_name='Имя пользователя')
    LastName = models.CharField(max_length=30, verbose_name='Фамилия пользователя')
    Gender = models.CharField(max_length=1, choices=GENDER_LIST, verbose_name='Пол пользователя')
    Phone = models.CharField(max_length=30, verbose_name='Мобильный телефон пользователя')
    Email = models.CharField(max_length=30, verbose_name='Емейл пользователя', unique=True)
    Password = models.CharField(max_length=30, verbose_name='Пароль пользователя', default='None')
    CreatedDate = models.DateTimeField(verbose_name='Дата создания', help_text='День, когда был создан аккаунт', auto_now_add=True)
    ModifiedDate = models.DateTimeField(verbose_name='Дата последнего изменения', help_text='Когда было изменено что-нибудь в аккаунте', auto_now_add=True)
    Active = models.BooleanField(verbose_name='Статус пользователя', help_text='Активен / Не активен', default=True)
    GroupID = models.ForeignKey('UserGroup', on_delete=models.SET_NULL, verbose_name='Группа пользователя', help_text='К какой группе относится пользователь', null=True)


class UserGroup(models.Model):
    class Meta:
        verbose_name_plural = 'Пользовательские группы'

    def __str__(self):
        return f'Группа {self.GroupType}'

    GroupType = models.CharField(max_length=15, verbose_name='Группа пользователя')
    Active = models.BooleanField(verbose_name='Статус группы', help_text='Активена / Не активена')


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
"""
