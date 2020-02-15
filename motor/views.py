from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, UserpageForm, PasswordForm, SaveFormFirst, SaveFormComments, SaveFormRating
from .models import User, AdvertiseCar, AdvertiseComments, Ratings
from django.http import Http404
import logging
from django.contrib.auth.decorators import login_required
from django.db import connection


logger = logging.getLogger(__name__)


class FormWrapper:
    def __init__(self, form, error=False):
        self.form = form
        self.error = error


def index(request):
    signup_form = FormWrapper(SignUpForm())
    login_form = FormWrapper(LoginForm())
    user_id = request.session.get('user_id', None)

    cursor = connection.cursor()

    cursor.execute("SELECT name_rus FROM public.car_mark")
    car_mark = cursor.fetchall()
    cars = []
    for i in car_mark:
        cars.append(i[0])
    cursor.execute("SELECT name, id_car_model, id_car_mark FROM public.car_model")
    name_model_mark = cursor.fetchall()
    cursor.execute("SELECT id_car_model, name, year_begin, year_end FROM public.car_generation")
    generation_model_begin_end = cursor.fetchall()
    all_models_begin = {}
    all_models_end = {}
    for i in name_model_mark:
        for j in generation_model_begin_end:
            if i[1] not in all_models_begin:
                if i[1] == j[0]:
                    all_models_begin[i[1]] = [j[2]]
            else:
                if j[2] not in all_models_begin[i[1]]:
                    all_models_begin[i[1]].append(j[2])
    for i in name_model_mark:
        for j in generation_model_begin_end:
            if i[1] not in all_models_end:
                if i[1] == j[0]:
                    all_models_end[i[1]] = [j[3]]
            else:
                if j[3] not in all_models_end[i[1]]:
                    all_models_end[i[1]].append(j[3])
    cursor.execute("SELECT id_car_model, name FROM public.car_modification")
    model_gear = cursor.fetchall()
    gears = {}
    for item in model_gear:
        if item[0] not in gears.keys():
            gears[item[0]] = [item[1]]
        else:
            if item[1] not in gears[item[0]]:
                gears[item[0]].append(item[1])
    cursor.execute("SELECT id_car_model, name, id_car_generation FROM public.car_serie")
    model_name_generation = cursor.fetchall()
    kuzov = {}
    for item in model_name_generation:
        if item[0] not in kuzov.keys():
            kuzov[item[0]] = [item[1]]
        else:
            if item[1] not in kuzov[item[0]]:
                kuzov[item[0]].append(item[1])
    series = {}
    for item in model_name_generation:
        if item[0] not in series.keys():
            series[item[0]] = [item[1]]
        else:
            series[item[0]].append(item[1])

    model_series_sum = {}
    for key, values in sorted(series.items()):
        q = 0
        series_sum = {}
        for i in values:
            if i not in values:
                q = 1
                series_sum[i] = q
            else:
                q += 1
                series_sum[i] = q
        model_series_sum[key] = series_sum
    models_cars = {}
    models_honda = []
    models_infinity = []
    for i in name_model_mark:
        if i[2] == '76':
            models_honda.append(i[0])
        else:
            models_infinity.append(i[0])
    models_cars = {'models_honda': models_honda, 'models_infinity': models_infinity}

    if user_id is not None:
        user = User.objects.filter(id=user_id).first()
        if user is None:
            raise Http404('Error 404')

    params = None
    if user_id is None:
        params = {'signup_form': signup_form,
                    'login_form': login_form,
                    'cars': cars,
                    'models_honda': models_honda,
                    'all_models_begin': all_models_begin,
                    'all_models_end': all_models_end,
                    'models_infinity': models_infinity,
                    'gears': gears,
                    'kuzov': kuzov,
                    'model_series_sum': model_series_sum,
                    'models_cars': models_cars}
    else:
        params = {'user_login': user.Login,
                    'cars': cars,
                    'models_honda': models_honda,
                    'all_models_begin': all_models_begin,
                    'all_models_end': all_models_end,
                    'gears': gears,
                    'kuzov': kuzov,
                    'model_series_sum': model_series_sum,
                    'models_infinity': models_infinity,
                    'models_cars': models_cars}
    return render(request, 'motor/comparison.html', params)


def auto(request):
    cursor = connection.cursor()

    cursor.execute("SELECT name_rus FROM public.car_mark")
    car_mark = cursor.fetchall()
    cars = []
    for i in car_mark:
        cars.append(i[0])
    params = {'cars': cars}
    return render(request, 'motor/auto.html', params)


def add_model(request, car):
    cursor = connection.cursor()

    cursor.execute("SELECT name, id_car_model, id_car_mark FROM public.car_model")
    name_model_mark = cursor.fetchall()
    cursor.execute("SELECT id_car_model, name, year_begin, year_end FROM public.car_generation")
    generation_model_begin_end = cursor.fetchall()

    all_models_begin = {}
    all_models_end = {}
    for i in name_model_mark:
        for j in generation_model_begin_end:
            if i[1] not in all_models_begin:
                if i[1] == j[0]:
                    all_models_begin[i[1]] = [j[2]]
            else:
                if j[2] not in all_models_begin[i[1]]:
                    all_models_begin[i[1]].append(j[2])
    for i in name_model_mark:
        for j in generation_model_begin_end:
            if i[1] not in all_models_end:
                if i[1] == j[0]:
                    all_models_end[i[1]] = [j[3]]
            else:
                if j[3] not in all_models_end[i[1]]:
                    all_models_end[i[1]].append(j[3])
    models_cars = {}
    models_honda = []
    models_infinity = []
    for i in name_model_mark:
        if i[2] == '76':
            models_honda.append(i[0])
        else:
            models_infinity.append(i[0])
    models_cars = {'Хонда': models_honda, 'Инфинити': models_infinity}
    for items in models_cars.keys():
        if car == items:
            models = models_cars[items]
    params = {'car': car,
                'models': models}
    return render(request, 'motor/add_model.html', params)


def add_seria(request, car, seria):
    cursor = connection.cursor()

    cursor.execute("SELECT name_rus FROM public.car_mark")
    car_mark = cursor.fetchall()
    cars = []
    for i in car_mark:
        cars.append(i[0])
    cursor.execute("SELECT name, id_car_model, id_car_mark FROM public.car_model")
    name_model_mark = cursor.fetchall()
    cursor.execute("SELECT id_car_model, name, year_begin, year_end FROM public.car_generation")
    generation_model_begin_end = cursor.fetchall()
    seria_years = {}
    for i in name_model_mark:
        for j in generation_model_begin_end:
            if i[1] == j[0]:
                seria_years[i[0]] = j[2:4]
    years = []
    for item in seria_years.keys():
        if item == seria:
            for i in range(int(seria_years[item][0]), int(seria_years[item][1]), 1):
                years.append(i)
    params = {'car': car,
                'seria': seria,
                'years': years}
    return render(request, 'motor/add_seria.html', params)


def add_year(request, car, seria, year):
    cursor = connection.cursor()

    cursor.execute("SELECT name FROM public.car_serie")
    serias = cursor.fetchall()
    all_kuzov = []
    for i in serias:
        if i[0] not in all_kuzov:
            all_kuzov.append(i[0])
    params = {'car': car,
                'seria': seria,
                'year': year,
                'all_kuzov': all_kuzov}
    return render(request, 'motor/add_year.html', params)


def add_kuzov(request, car, seria, year, kuzov):
    cursor = connection.cursor()

    cursor.execute("SELECT name, id_car_model, id_car_mark FROM public.car_model")
    name_model_mark = cursor.fetchall()
    cursor.execute("SELECT name FROM public.car_serie")
    serias = cursor.fetchall()
    cursor.execute("SELECT id_car_model, name, year_begin, year_end FROM public.car_generation")
    generation_model_begin_end = cursor.fetchall()
    generations = {}
    for i in name_model_mark:
        if seria == i[0]:
            for j in generation_model_begin_end:
                if i[1] == j[0]:
                    if seria not in generations.keys():
                        generations[seria] = [j[1:]]
                    else:
                        generations[seria].append(j[1:])
    all_generations = []
    for i in generations[seria]:
        all_generations.append(("{}, {} - {}".format(i[0], i[1], i[2])))
    all_kuzov = []
    for i in serias:
        if i[0] not in all_kuzov:
            all_kuzov.append(i[0])
    cursor.execute("SELECT id_car_model, name FROM public.car_modification")
    model_gear = cursor.fetchall()
    gears = {}
    for item in model_gear:
        if item[0] not in gears.keys():
            gears[item[0]] = [item[1]]
        else:
            if item[1] not in gears[item[0]]:
                gears[item[0]].append(item[1])
    for i in name_model_mark:
        if seria == i[0]:
            for j in gears:
                if int(i[1]) == int(j):
                    modifications = gears[j]
    if request.method == 'POST':
        save_form = SaveFormFirst(request.POST, request.FILES)
        if save_form.is_valid():
            user_id = request.session.get('user_id', None)
            advertisement = AdvertiseCar()
            advertisement.ID_id = user_id
            advertisement.NameCar = car
            advertisement.SeriaCar = seria
            advertisement.YearCar = year
            advertisement.KuzovCar = kuzov
            advertisement.GenerationCar = save_form.data.get("generation", None)
            advertisement.GearCar = save_form.data.get("box", None)
            advertisement.DriveCar = save_form.data.get('drive', None)
            advertisement.MotorCar = save_form.data.get('motor', None)
            advertisement.ModificationCar = save_form.data.get('modification', None)
            advertisement.ColorCar = save_form.data.get("color", None)
            advertisement.ImageCar = request.FILES['image']
            advertisement.MediaCar = save_form.data.get('media', None)
            advertisement.MediaSystemCar = save_form.data.get('media_system', None)
            advertisement.MediaAudioSystemCar = save_form.data.get('media_audio_system', None)
            advertisement.ComfortCar1 = save_form.data.get('comfort1', None)
            advertisement.ComfortCar2 = save_form.data.get('comfort2', None)
            advertisement.ComfortCar3 = save_form.data.get('comfort3', None)
            advertisement.SecurityCar1 = save_form.data.get('security1', None)
            advertisement.SecurityCar2 = save_form.data.get('security2', None)
            advertisement.SecurityCar3 = save_form.data.get('security3', None)
            advertisement.BuyYearCar = save_form.data.get('year_buy', None)
            advertisement.BuyMonthCar = save_form.data.get('month', None)
            advertisement.RunCar = save_form.data.get('run', None)
            advertisement.PriceCar = save_form.data.get('price', None)
            advertisement.OwnerCar = save_form.data.get('owner', None)
            advertisement.DopCar = save_form.data.get('dop', None)
            advertisement.YourName = save_form.data.get('name', None)
            advertisement.YourPhone = save_form.data.get('phone', None)
            advertisement.YourMail = save_form.data.get('mail', None)
            advertisement.YourCity = save_form.data.get('city', None)
            advertisement.save()
            return redirect('LK')
        else:
            raise Http404("Some Errors - Invalid forms!!!", save_form.errors)
    params = {'car': car,
                'seria': seria,
                'year': year,
                'all_kuzov': all_kuzov,
                'kuzov': kuzov,
                'modifications': modifications,
                'generations': all_generations}
    return render(request, 'motor/add_kuzov.html', params)


@login_required
def LK(request):
    user_id = request.session.get('user_id', None)
    notes = AdvertiseCar.objects.filter(ID_id=user_id)
    params = {'notes': notes}
    return render(request, 'motor/LK.html', params)


@login_required
def add_cabinet(request):
    signup_form = FormWrapper(SignUpForm())
    login_form = FormWrapper(LoginForm())
    user_id = request.session.get('user_id', None)

    cursor = connection.cursor()

    cursor.execute("SELECT name_rus FROM public.car_mark")
    car_mark = cursor.fetchall()
    cars = []
    for i in car_mark:
        cars.append(i[0])
    cursor.execute("SELECT name, id_car_model, id_car_mark FROM public.car_model")
    name_model_mark = cursor.fetchall()
    cursor.execute("SELECT id_car_model, name, year_begin, year_end FROM public.car_generation")
    generation_model_begin_end = cursor.fetchall()
    all_models_begin = {}
    all_models_end = {}
    for i in name_model_mark:
        for j in generation_model_begin_end:
            if i[1] not in all_models_begin:
                if i[1] == j[0]:
                    all_models_begin[i[1]] = [j[2]]
            else:
                if j[2] not in all_models_begin[i[1]]:
                    all_models_begin[i[1]].append(j[2])
    for i in name_model_mark:
        for j in generation_model_begin_end:
            if i[1] not in all_models_end:
                if i[1] == j[0]:
                    all_models_end[i[1]] = [j[3]]
            else:
                if j[3] not in all_models_end[i[1]]:
                    all_models_end[i[1]].append(j[3])
    cursor.execute("SELECT id_car_model, name FROM public.car_modification")
    model_gear = cursor.fetchall()
    gears = {}
    for item in model_gear:
        if item[0] not in gears.keys():
            gears[item[0]] = [item[1]]
        else:
            if item[1] not in gears[item[0]]:
                gears[item[0]].append(item[1])
    cursor.execute("SELECT id_car_model, name, id_car_generation FROM public.car_serie")
    model_name_generation = cursor.fetchall()
    kuzov = {}
    for item in model_name_generation:
        if item[0] not in kuzov.keys():
            kuzov[item[0]] = [item[1]]
        else:
            if item[1] not in kuzov[item[0]]:
                kuzov[item[0]].append(item[1])
    series = {}
    for item in model_name_generation:
        if item[0] not in series.keys():
            series[item[0]] = [item[1]]
        else:
            series[item[0]].append(item[1])

    model_series_sum = {}
    for key, values in sorted(series.items()):
        q = 0
        series_sum = {}
        for i in values:
            if i not in values:
                q = 1
                series_sum[i] = q
            else:
                q += 1
                series_sum[i] = q
        model_series_sum[key] = series_sum
    models_cars = {}
    models_honda = []
    models_infinity = []
    for i in name_model_mark:
        if i[2] == '76':
            models_honda.append(i[0])
        else:
            models_infinity.append(i[0])
    models_cars = {'models_honda': models_honda, 'models_infinity': models_infinity}

    if user_id is not None:
        user = User.objects.filter(id=user_id).first()
        if user is None:
            raise Http404('Error 404')

    params = None
    if user_id is None:
        params = {'signup_form': signup_form,
                    'login_form': login_form,
                    'cars': cars,
                    'models_honda': models_honda,
                    'all_models_begin': all_models_begin,
                    'all_models_end': all_models_end,
                    'models_infinity': models_infinity,
                    'gears': gears,
                    'kuzov': kuzov,
                    'model_series_sum': model_series_sum,
                    'models_cars': models_cars}
    else:
        params = {'user_login': user.Login,
                    'cars': cars,
                    'models_honda': models_honda,
                    'all_models_begin': all_models_begin,
                    'all_models_end': all_models_end,
                    'gears': gears,
                    'kuzov': kuzov,
                    'model_series_sum': model_series_sum,
                    'models_infinity': models_infinity,
                    'models_cars': models_cars}
    return render(request, 'motor/auto_cabinet.html', params)


@login_required
def auto_profile(request, id):
    note = AdvertiseCar.objects.filter(id=id)[0]
    comments = AdvertiseComments.objects.filter(ID_Advertisement=id)
    all_ratings = Ratings.objects.filter(ID=id)
    if len(all_ratings) > 0:
        last_rating = all_ratings[len(all_ratings) - 1]
    else:
        last_rating = []
    if request.method == 'POST':
        save_form = SaveFormComments(request.POST)
        rating_form = SaveFormRating(request.POST)
        if save_form.is_valid():
            comment = AdvertiseComments()
            comment.Name = save_form.data.get('Name', None)
            comment.Email = save_form.data.get('Email', None)
            comment.Comment = save_form.data.get('Comment', None)
            comment.ID_Advertisement = id
            comment.save()
        elif rating_form.is_valid():
            rating = Ratings()
            rating.kuzov = save_form.data.get('kuzov', None)
            rating.cover = save_form.data.get('cover', None)
            rating.salon = save_form.data.get('salon', None)
            rating.exterer = save_form.data.get('exterer', None)
            rating.electro = save_form.data.get('electro', None)
            rating.hod = save_form.data.get('hod', None)
            rating.motor = save_form.data.get('motor', None)
            rating.gearbox = save_form.data.get('gearbox', None)
            rating.ID = id
            rating.save()
            summ_kuzov = 0
            summ_cover = 0
            summ_salon = 0
            summ_exterer = 0
            summ_electro = 0
            summ_hod = 0
            summ_motor = 0
            summ_gearbox = 0
            for i in Ratings.objects.filter(ID=id):
                summ_kuzov = summ_kuzov + float(i.kuzov)
                summ_salon = summ_salon + float(i.salon)
                summ_cover = summ_cover + float(i.cover)
                summ_exterer = summ_exterer + float(i.exterer)
                summ_electro = summ_electro + float(i.electro)
                summ_hod = summ_hod + float(i.hod)
                summ_motor = summ_motor + float(i.motor)
                summ_gearbox = summ_gearbox + float(i.gearbox)
            rating.kuzov_average = round(summ_kuzov / len(Ratings.objects.filter(ID=id)), 1)
            rating.salon_average = round(summ_salon / len(Ratings.objects.filter(ID=id)), 1)
            rating.cover_average = round(summ_cover / len(Ratings.objects.filter(ID=id)), 1)
            rating.exterer_average = round(summ_exterer / len(Ratings.objects.filter(ID=id)), 1)
            rating.electro_average = round(summ_electro / len(Ratings.objects.filter(ID=id)), 1)
            rating.hod_average = round(summ_hod / len(Ratings.objects.filter(ID=id)), 1)
            rating.motor_average = round(summ_motor / len(Ratings.objects.filter(ID=id)), 1)
            rating.gearbox_average = round(summ_gearbox / len(Ratings.objects.filter(ID=id)), 1)
            rating.save()
    params = None
    if id is None:
        params = {'note': note,
                    'last_rating': last_rating,
                    'comments': comments}
    else:
        params = {'note': note,
                    'last_rating': last_rating,
                    'comments': comments}
    return render(request, 'motor/auto_profile.html', params)


def register(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = User()
            user.Email = signup_form.data.get("email", None)
            user.Login = signup_form.data.get("username", None)
            user.Password = signup_form.data.get('password', None)
            user.save()
            return redirect('login')
        else:
            signup_form = FormWrapper(signup_form, True)
            login_form = FormWrapper(LoginForm())
            return render(request, 'motor/registration/register.html', {'signup_form': signup_form, 'login_form': login_form})
    return render(request, 'motor/registration/register.html')


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.data.get("email", None)
            password = login_form.data.get("password", None)
            user = User.objects.filter(Email=email, Password=password).first()
            if user is not None:
                request.session['user_id'] = user.id
                return redirect('user_page')
        else:
            return render(request, 'motor/404page.html')
    return render(request, 'motor/registration/login.html')


def logout(request):
    if 'user_id' in request.session.keys():
        del request.session['user_id']
    return redirect('index')


def change_password(request):
    if request.method == 'POST':
        userpage_form = PasswordForm(request.POST)
        user_id = request.session.get('user_id', None)
        if user_id is None:
            return redirect('index')
        if userpage_form.is_valid():
            user = User.objects.filter(id=user_id)[0]
            if user is None:
                raise Http404('User {} not found'.format(user_id))
            user_password = user.Password
            password = request.POST.get('password')
            new_password = request.POST.get('new_password')
            new_password2 = request.POST.get('new_password2')
            if password == user_password:
                if new_password == new_password2:
                    user.Password = new_password
            user.save()
            return redirect('change_password')
        else:
            return render(request, 'motor/404page.html')
    else:
        signup_form = FormWrapper(SignUpForm())
        login_form = FormWrapper(LoginForm())
        user_id = request.session.get('user_id', None)
        if user_id is not None:
            user = User.objects.filter(id=user_id).first()
            if user is None:
                return render(request, 'motor/404page.html')
        params = None
        if user_id is None:
            params = {'signup_form': signup_form, 'login_form': login_form}
        else:
            params = {'user_login': user.Login, 'user_email': user.Email}
        return render(request, 'motor/change_password.html', params)


@login_required
def user_page(request):
    if request.method == 'POST':
        userpage_form = UserpageForm(request.POST)
        user_id = request.session.get('user_id', None)
        if user_id is None:
            return redirect('index')
        if userpage_form.is_valid():
            user = User.objects.filter(id=user_id)[0]
            if user is None:
                raise Http404('User {} not found'.format(user_id))
            if 'email' in userpage_form.data:
                user.Email = userpage_form.data.get('email')
            if 'username' in userpage_form.data:
                user.Login = userpage_form.data.get('username')
            if 'firstname' in userpage_form.data:
                user.FirstName = userpage_form.data.get('firstname')
            if 'lastname' in userpage_form.data:
                user.LastName = userpage_form.data.get('lastname')
            if 'phone' in userpage_form.data:
                user.Phone = userpage_form.data.get('phone')
            if 'gender' in userpage_form.data:
                user.Gender = userpage_form.data.get('gender')
            user.save()
            return redirect('user_page')
        else:
            return render(request, 'motor/404page.html')
    else:
        signup_form = FormWrapper(SignUpForm())
        login_form = FormWrapper(LoginForm())
        user_id = request.session.get('user_id', None)
        if user_id is not None:
            user = User.objects.filter(id=user_id).first()
            if user is None:
                return render(request, 'motor/404page.html')
        params = None
        if user_id is None:
            params = {'signup_form': signup_form, 'login_form': login_form}
        else:
            params = {'user_login': user.Login, 'user_email': user.Email, 'firstname': user.FirstName,
                      'lastname': user.LastName, 'user_phone': user.Phone, 'gender': user.Gender}
        return render(request, 'motor/user_page.html', params)


def test_view(request):
    if request.method == 'POST':
        logger.debug('POST data: {}'.format(request.POST))
    elif request.method == 'GET':
        logger.debug('GET data: {}'.format(request.GET))
    else:
        raise RuntimeError('Invalid usage')
