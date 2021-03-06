from django.db import models
from django.contrib.postgres.fields import ArrayField


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

    NameCar = models.CharField(max_length=55, verbose_name='Марка автомобиля')
    SeriaCar = models.CharField(max_length=55, verbose_name='Серия автомобиля')
    YearCar = models.CharField(max_length=55, verbose_name='Год выпуска автомобиля')
    KuzovCar = models.CharField(max_length=55, verbose_name='Кузов автомобиля')
    GenerationCar = models.CharField(max_length=55, verbose_name='Поколение автомобиля')
    GearCar = models.CharField(max_length=55, verbose_name='Коробка автомобиля')
    DriveCar = models.CharField(max_length=55, verbose_name='Привод автомобиля')
    MotorCar = models.CharField(max_length=55, verbose_name='Двигатель автомобиля')
    ModificationCar = models.CharField(max_length=55, verbose_name='Модификация автомобиля')
    ColorCar = models.CharField(max_length=55, verbose_name='Название автомобиля')
    ImageCar = models.ImageField(upload_to='cars/')
    MediaCar = models.CharField(max_length=55, verbose_name='Мультмедиа автомобиля')
    MediaSystemCar = models.CharField(max_length=55, verbose_name='Мультмедиасистемы автомобиля')
    MediaAudioSystemCar = models.CharField(max_length=55, verbose_name='Мультмедиааудиосистемы автомобиля')
    ComfortCar1 = models.CharField(max_length=55, verbose_name='Комфорт1 автомобиля')
    ComfortCar2 = models.CharField(max_length=55, verbose_name='Комфорт2 автомобиля')
    ComfortCar3 = models.CharField(max_length=55, verbose_name='Комфорт3 автомобиля')
    SecurityCar1 = models.CharField(max_length=55, verbose_name='Безопасность1 автомобиля')
    SecurityCar2 = models.CharField(max_length=55, verbose_name='Безопасность2 автомобиля')
    SecurityCar3 = models.CharField(max_length=55, verbose_name='Безопасность3 автомобиля')
    BuyYearCar = models.CharField(max_length=55, verbose_name='Год покупки автомобиля')
    BuyMonthCar = models.CharField(max_length=55, verbose_name='Месяц покупки автомобиля')
    WheelCar = models.CharField(max_length=55, verbose_name='Расположение руля')
    RemontCar = models.CharField(max_length=55, verbose_name='Нужен ли ремонт?')
    PasswordCar = models.CharField(max_length=55, verbose_name='ПТС')
    CustomCar = models.CharField(max_length=55, verbose_name='Нужна ли растаможка?')
    ChangeCar = models.CharField(max_length=55, verbose_name='Нужна ли растаможка?')
    RunCar = models.CharField(max_length=55, verbose_name='Пробег автомобиля')
    PriceCar = models.CharField(max_length=55, verbose_name='Цена автомобиля')
    OwnerCar = models.CharField(max_length=55, verbose_name='Владелец автомобиля')
    DopCar = models.CharField(max_length=55, verbose_name='Дополнительное описание автомобиля')
    YourName = models.CharField(max_length=55, verbose_name='Ваше имя')
    YourPhone = models.CharField(max_length=55, verbose_name='Ваш телефон')
    YourMail = models.CharField(max_length=55, verbose_name='Ваша почта')
    YourCity = models.CharField(max_length=55, verbose_name='Город продажи')
    Time = models.DateTimeField(auto_now_add=True, blank=True)
    ID = models.ForeignKey(User, to_field="id", on_delete=models.CASCADE)


class AdvertiseComments(models.Model):
    class Meta:
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Комментарий {self.Name}'

    Name = models.CharField(max_length=30, verbose_name='Имя пользователя')
    Email = models.CharField(max_length=30, verbose_name='Емейл пользователя')
    Comment = models.CharField(max_length=30, verbose_name='Комментарий пользователя')
    ID_Advertisement = models.CharField(max_length=30, verbose_name='Номер комментария')
    Time = models.DateTimeField(auto_now_add=True, blank=True)


class Ratings(models.Model):
    class Meta:
        verbose_name_plural = 'Голосование'

    def __str__(self):
        return f'Комментарий {self.kuzov}'

    kuzov = models.CharField(max_length=30, verbose_name='Целостность кузова')
    kuzov_average = models.CharField(max_length=30, verbose_name='Целостность кузова (среднее)')
    cover = models.CharField(max_length=30, verbose_name='Лакокрасочное покрытие')
    cover_average = models.CharField(max_length=30, verbose_name='Целостность кузова (среднее)')
    salon = models.CharField(max_length=30, verbose_name='Салон и интерьер')
    salon_average = models.CharField(max_length=30, verbose_name='Целостность кузова (среднее)')
    exterer = models.CharField(max_length=30, verbose_name='+1 пункт по экстерьеру')
    exterer_average = models.CharField(max_length=30, verbose_name='Целостность кузова (среднее)')
    electro = models.CharField(max_length=30, verbose_name='Электрооборудование')
    electro_average = models.CharField(max_length=30, verbose_name='Целостность кузова (среднее)')
    hod = models.CharField(max_length=30, verbose_name='Ходовая часть')
    hod_average = models.CharField(max_length=30, verbose_name='Целостность кузова (среднее)')
    motor = models.CharField(max_length=30, verbose_name='Двигатель')
    motor_average = models.CharField(max_length=30, verbose_name='Целостность кузова (среднее)')
    gearbox = models.CharField(max_length=30, verbose_name='Коробка передач')
    gearbox_average = models.CharField(max_length=30, verbose_name='Целостность кузова (среднее)')
    ID = models.CharField(max_length=30, verbose_name='Номер объявления')


class ComparisonFirst(models.Model):
    ID_Advertisement = models.CharField(max_length=30, verbose_name='Номер объявления')
    ID_User = models.CharField(max_length=30, verbose_name='Номер пользователя')


class ComparisonGeneral(models.Model):
    ID_LIST = ArrayField(models.CharField(max_length=200), blank=True)
    ID_User = models.CharField(max_length=30, verbose_name='Номер пользователя')


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
