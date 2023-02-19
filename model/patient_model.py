class Patient:
    def __init__(self):
        self._id_patient = 0
        self._firstname = None
        self._surname = None
        self._middle_name = None
        self._date_of_birth = None
        self._gender = None
        self._address = None
        self._phone = None
        self._polis_oms = ''
        self._snils = None
        self._document = None
        self._dianosis = None
        self._date_healing_start = None
        self._date_healing_end = None
        self._history_healing = None


    @property
    def id_patient(self):
        return self._id_patient

    @id_patient.setter
    def id_patient(self, value):
        self._id_patient = value

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        self._firstname = value

    @property
    def last_name(self):
        return self._surname

    @last_name.setter
    def last_name(self, value):
        self._surname = value

    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value):
        self._middle_name = value


    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self._date_of_birth = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def polis_oms(self):
        return self._polis_oms

    @polis_oms.setter
    def polis_oms(self, value):
        self._polis_oms = value

    @property
    def document(self):
        return self._document

    @document.setter
    def document(self, value):
        self._document = value
        
    @property
    def snils(self):
        return self._snils
    
    @snils.setter
    def snils(self, value):
        self._snils = value

    @property
    def full_name(self):
        return '{} {} {}'.format(self.last_name, self.firstname, self.middle_name)

    @property
    def dianosis(self):
        return self._dianosis

    @dianosis.setter
    def dianosis(self, value):
        self._dianosis = value
