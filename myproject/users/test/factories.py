import factory
from django.contrib.auth import get_user_model
from users.models import Admin, Manager, Roles


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = get_user_model()
        django_get_or_create = ('username', 'email')

    first_name = factory.Sequence(lambda n: "User %03d" % n)
    last_name = factory.Sequence(lambda n: "Last %03d" % n)
    username = factory.Sequence(lambda n: "agent%03d" % n)
    email = factory.Sequence(lambda n: "user%03d@example.com" % n)
    is_active = True

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        # By using this method password can never be set to `None`!
        self.raw_password = 'default_password' if extracted is None else extracted
        self.set_password(self.raw_password)
        if create:
            self.save()


class AdminFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Admin

    email = factory.Sequence(lambda n: "admin%03d@example.com" % n)
    username = factory.Sequence(lambda n: "admin%03d" % n)
    role = Roles.ADMIN


class ManagerFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Manager

    email = factory.Sequence(lambda n: "manager%03d@example.com" % n)
    username = factory.Sequence(lambda n: "manager%30d" % n)
    role = Roles.NORMAL_USER
