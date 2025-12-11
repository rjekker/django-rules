from django.contrib import admin
from django.urls import re_path

from .views import (
    BookCreateView,
    BookDeleteView,
    BookUpdateErrorView,
    BookUpdateView,
    ViewThatRaises,
    ViewWithPermissionList,
    car_view_with_permission_list,
    car_view_with_permission_list_for_class,
    change_book,
    crash,
    crash_car,
    crash_car_default,
    delete_book,
    drive_car,
    drive_car_default,
    view_that_raises,
    view_with_object,
    view_with_permission_list,
    wash,
    wash_car,
    wash_car_default,
)

admin.autodiscover()

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    # Function-based views
    re_path(r"^(?P<book_id>\d+)/change/$", change_book, name="change_book"),
    re_path(r"^(?P<book_id>\d+)/delete/$", delete_book, name="delete_book"),
    re_path(r"^(?P<book_id>\d+)/raise/$", view_that_raises, name="view_that_raises"),
    re_path(r"^(?P<book_id>\d+)/object/$", view_with_object, name="view_with_object"),
    re_path(
        r"^(?P<book_id>\d+)/list/$",
        view_with_permission_list,
        name="view_with_permission_list",
    ),
    # Class-based views
    re_path(r"^cbv/create/$", BookCreateView.as_view(), name="cbv.create_book"),
    re_path(
        r"^cbv/(?P<book_id>\d+)/change/$",
        BookUpdateView.as_view(),
        name="cbv.change_book",
    ),
    re_path(
        r"^cbv/(?P<book_id>\d+)/delete/$",
        BookDeleteView.as_view(),
        name="cbv.delete_book",
    ),
    re_path(
        r"^cbv/(?P<book_id>\d+)/raise/$",
        ViewThatRaises.as_view(),
        name="cbv.view_that_raises",
    ),
    re_path(
        r"^cbv/(?P<book_id>\d+)/list/$",
        ViewWithPermissionList.as_view(),
        name="cbv.view_with_permission_list",
    ),
    re_path(
        r"^cbv/(?P<book_id>\d+)/change-error/$",
        BookUpdateErrorView.as_view(),
        name="cbv.change_book_error",
    ),
    re_path(r"^(?P<car_id>\d+)/drive/$", drive_car, name="drive_car"),
    re_path(r"^(?P<car_id>\d+)/wash/$", wash_car, name="wash_car"),
    re_path(r"^(?P<car_id>\d+)/crash/$", crash_car, name="crash_car"),
    re_path(
        r"^(?P<car_id>\d+)/permlist/$",
        car_view_with_permission_list,
        name="car_view_with_permission_list",
    ),
    re_path(
        r"^(?P<id>\d+)/drive_default/$", drive_car_default, name="drive_car_default"
    ),
    re_path(r"^(?P<id>\d+)/wash_default/$", wash_car_default, name="wash_car_default"),
    re_path(
        r"^(?P<id>\d+)/crash_default/$", crash_car_default, name="crash_car_default"
    ),
    re_path(r"^wash$", wash, name="wash_class"),
    re_path(r"^crash$", crash, name="crash_class"),
    re_path(
        r"^permlist$",
        car_view_with_permission_list_for_class,
        name="car_view_with_permission_list_for_class",
    ),
]
