from app.models import Account, Admin, Lesson, Product, User, Viewing
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Displays current time"
    _names_users = [
        "James",
        "John",
        "Robert",
        "Michael",
        "William",
        "David",
        "Richard",
        "Charles",
        "Joseph",
        "Thomas",
    ]
    _names_products = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    _names_lessons = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

    def handle(self, *args, **kwargs):
        admin = Admin.objects.create(name="all")
        user_all = User.objects.create(name="all")
        product_all = Product.objects.create(name="all", proprietor_name=admin)
        account_all = Account.objects.create(
            user=user_all, login="login", password="password"
        )
        account_all.products.add(product_all)
        lesson_all = Lesson.objects.create(
            name="all", link_video="https://ya.ru/", duration=1000
        )
        product_all.lessons.add(lesson_all)
        for i in range(10):
            user = User.objects.create(name=self._names_users[i])
            product = Product.objects.create(
                name=self._names_products[i], proprietor_name=admin
            )
            account = Account.objects.create(
                user=user, login=f"login{i}", password="password"
            )
            account.products.add(product, product_all)
            lesson = Lesson.objects.create(
                name=self._names_lessons[i],
                link_video=f"https://ya.ru/{i}",
                duration=i * 10 + 10 + i * 5,
            )
            product.lessons.add(lesson, lesson_all)
            viewing1 = Viewing.objects.create(
                account=account, lesson=lesson, viewing_time=i * 10 + 10
            )
            viewing2 = Viewing.objects.create(
                account=account, lesson=lesson_all, viewing_time=i * 10 + 10
            )
            viewing3 = Viewing.objects.create(
                account=account_all, lesson=lesson, viewing_time=i * 10 + 10
            )
        self._add_status_viewing()

    @staticmethod
    def _add_status_viewing():
        viewings = Viewing.objects.all()
        for viewing in viewings:
            if (
                round(viewing.viewing_time / viewing.lesson.duration * 100)
                >= 80
            ):
                viewing.status = "se"
                viewing.save()
