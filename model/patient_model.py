import datetime


class Patient(object):
    def __init__(self, **entries):
        self.id_patient = None
        self.firstname = None
        self.surname = None
        self.middlename = None
        self.date_of_birth = None
        self.gender = None
        self.address = None
        self.phone = None
        self.polis_oms = ''
        self.snils = None
        self.document = None
        self.dianosis = None
        self.date_healing_start = None
        self.date_healing_end = None
        self.history = None
        if entries:
            self.__dict__.update(entries)

    def to_dict(self):
        if isinstance(self.date_of_birth, datetime.date):
            self.date_of_birth = str(self.date_of_birth)
        return self.__dict__

    @property
    def full_name(self):
        return '{} {} {}'.format(self.surname, self.firstname, self.middlename)


