from django.shortcuts import render, redirect, reverse
# from django.contrib.auth.decorators import login_required

import csv, io
from django.contrib import messages
from users.models import User


def user_csv_import(request):
    template = "CSV_import.html"
    prompt = {
        'order': 'Order of the csv file should be'
                 'Email, Name, Password, Phone, Avatar, Status, Designation, Is Active, Is Staff, Is Admin, Is Viewer'
    }
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    print(data_set)
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):

        _, created = User.objects.update_or_create(
            email=column[0],
            name=column[1],
            password=column[2],
            phone=column[3],
            avatar=column[4],
            status=column[5],
            designation=column[6],
            is_active=column[7],
            is_staff=column[8],
            is_admin=column[9],
            is_viewer=column[10]
        )
    context = {}
    return render(request, template, context)


