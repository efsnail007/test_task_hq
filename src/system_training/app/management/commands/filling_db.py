from django.core.management.base import BaseCommand
from app.models import User, Product, Account, Admin, Lesson, Viewing


class Command(BaseCommand):
    help = 'Displays current time'
    _names_users = ["James",
                    "John",
                    "Robert",
                    "Michael",
                    "William",
                    "David",
                    "Richard",
                    "Charles",
                    "Joseph",
                    "Thomas"]
    _names_products = ["1",
                       "2",
                       "3",
                       "4",
                       "5",
                       "6",
                       "7",
                       "8",
                       "9",
                       "10"]
    _names_lessons = ["a",
                      "b",
                      "c",
                      "d",
                      "e",
                      "f",
                      "g",
                      "h",
                      "i",
                      "j"]

    def handle(self, *args, **kwargs):
        admin = Admin.objects.create(name="all")
        user_all = User.objects.create(name="all")
        product_all = Product.objects.create(name="all", proprietor_name=admin)
        lesson_all = Lesson.objects.create(name="all", link_video="https://ya.ru/", duration=10)
        for i in range(10):
            user = User.objects.create(name=self._names_users[i])
            product = Product.objects.create(name=self._names_products[i], proprietor_name=admin)
            account = Account.objects.create(user=user, login=f"login{i}", password="password")
            account.products.add(product, product_all)
            lesson = Lesson.objects.create(name=self._names_lessons[i], link_video=f"https://ya.ru/{i}",
                                           duration=i * 10 + 10 + i * 5)
            product.lessons.add(lesson, lesson_all)
            viewing1 = Viewing.objects.create(user=user, lesson=lesson, viewing_time=i * 10 + 10)
            viewing2 = Viewing.objects.create(user=user, lesson=lesson_all, viewing_time=i * 10 + 10)
            viewing3 = Viewing.objects.create(user=user_all, lesson=lesson, viewing_time=i * 10 + 10)