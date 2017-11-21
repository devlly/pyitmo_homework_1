from abc import ABCMeta, abstractmethod
import datetime

class Validator(metaclass=ABCMeta):
    types = {}
    def __init__(self, name):
        self.name = name

    def validate(self):
        pass

    @classmethod
    def get_instance(cls, name):
        if name not in types[keys]:
            raise ValidatorException(
        'Validator with name "{}" not found!'.format(name)
        )
        klass = cls.types.get(name)
        return klass(name, *args, **kwargs)


    @staticmethod
    def add_type(name, klass):
        if name is None:
            raise ValidatorException(
                'Validator must have name!'
        )
        if not issubclass(klass, Validator):
            raise ValidatorException(
                'Class "{}" is not Validator!'.format(klass)
        )
        types[name] = klass


    @staticmethod
    def get_instance(name):
        if name not in types:
            raise ValidatorException(
            'Validator with name "{}" not found'.format(name)
        )


class ValidatorException(Exception):
    pass

class EMailValidator(Validator):
    @staticmethod
    def validate(email):
        if '@' not in email:
            raise ValidatorException(
                'The "{}" is not an email adress!'.format(email)
                )
            if '.' not in email.rsplit('@'):
                raise ValidatorException(
                    'The "{}" is not an email adress1!'.format(email)
                    )

        else:
            return True

#EMailValidator.validate('info@itmo-it.org')
#EMailValidator.validate('break_email')


class DateTimeValidator(Validator):

    def validate(datetm):
        datetm = datetm.split(' ')
        print(datetm)
        if len(datetm) >= 1:
            date = datetm[0]
            print(date)
            date = date.rstrip(',')
            print(date)
            if '-' or '.' or '/' not in date:
                raise ValidatorException(
            'This is "{}" wrong format of the date1!'.format(date)
            )

            else:
                date = date.replace('-.', '/')
                year, month, day = date.split('/')
                print(year, month, day)
                year = year.lstrip('0')
                month = month.lstrip('0')
                day = day.lstrip('0')
                year, month, day = int(year), int(month), int(day)
                print(year, month, day)
                if year <= 31:
                    year, day = day, year
                    print(year, day)
                    datetime.date(year, month, day)
                datetime.date(year, month, day)

        if len(datetm) == 2:
            time = datetm[1]
            print(time)
            if ':' not in time:
                raise ValidatorException(
                'Wrong format of the time!'
                )
            else:
                time = time.split(':')
                print(time)
                if len(time) >= 2:
                    hour = time[0].replace('0', '', 1)
                    minut = time[1].replace('0', '', 1)
                    hour = int(hour)
                    minut = int(minut)
                    datetime.time(hour, minut)
                    print(hour, minut)
                    if len(time) == 3:
                        second = time[2].replace('0', '', 1)
                        second = int(second)
                        print(second)
                        datetime.time(hour, minut, second)





# DateTimeValidator.validate('1#9#2017')
# DateTimeValidator.validate('01/09/2017, 12:00:06')
