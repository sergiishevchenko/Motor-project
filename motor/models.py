from django.db import models
import os


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


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


class AdvertiseCar(models.Model):
    class Meta:
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return f'Объявление {self.NameCar}'

    NameCar = models.CharField(max_length=15, verbose_name='Марка автомобиля')
    SeriaCar = models.CharField(max_length=25, verbose_name='Серия автомобиля')
    YearCar = models.CharField(max_length=15, verbose_name='Год выпуска автомобиля')
    KuzovCar = models.CharField(max_length=25, verbose_name='Кузов автомобиля')
    GenerationCar = models.CharField(max_length=30, verbose_name='Поколение автомобиля')
    GearCar = models.CharField(max_length=15, verbose_name='Коробка автомобиля')
    DriveCar = models.CharField(max_length=25, verbose_name='Привод автомобиля')
    MotorCar = models.CharField(max_length=25, verbose_name='Двигатель автомобиля')
    ModificationCar = models.CharField(max_length=35, verbose_name='Модификация автомобиля')
    ColorCar = models.CharField(max_length=15, verbose_name='Название автомобиля')
    ImageCar = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    MediaCar = models.CharField(max_length=25, verbose_name='Мультмедиа автомобиля')
    ComfortCar = models.CharField(max_length=25, verbose_name='Комфорт автомобиля')
    BuyYearCar = models.CharField(max_length=25, verbose_name='Год покупки автомобиля')
    BuyMonthCar = models.CharField(max_length=25, verbose_name='Месяц покупки автомобиля')
    RunCar = models.CharField(max_length=25, verbose_name='Пробег автомобиля')
    PriceCar = models.CharField(max_length=25, verbose_name='Цена автомобиля')
    OwnerCar = models.CharField(max_length=25, verbose_name='Владелец автомобиля')
    DopCar = models.CharField(max_length=25, verbose_name='Дополнительное описание автомобиля')
    YourName = models.CharField(max_length=25, verbose_name='Ваше имя', default='None')
    YourPhone = models.CharField(max_length=25, verbose_name='Ваш телефон', default='None')
    YourMail = models.CharField(max_length=25, verbose_name='Ваша почта', unique=True, default='None')
    YourCity = models.CharField(max_length=25, verbose_name='Город продажи', default='None')


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
