from model.patient_model import Patient


class PatientDTO:

    def __init__(self, **entries):
        self.id_patient = None
        self.firstname = None
        self.last_name = None
        self.middle_name = None
        self.date_of_birth = None
        self.address = None
        self.phone = None
        self.polis_oms = None
        self.snils = None
        self.document = None
        self.gender = None
        self.__dict__.update(entries)


def getPatient(patient_dto_back: PatientDTO):
    p = Patient()
    p.id_patient = patient_dto_back.id_patient
    p.firstname = patient_dto_back.firstname
    p.surname = patient_dto_back.last_name
    p.middlename = patient_dto_back.middle_name
    p.snils = patient_dto_back.snils
    p.document = patient_dto_back.document
    p.phone = patient_dto_back.phone
    p.date_of_birth = patient_dto_back.date_of_birth
    p.address = patient_dto_back.address
    p.polis_oms = patient_dto_back.polis_oms
    p.gender = patient_dto_back.gender
    return p


def getPatientList(patient_dto_back: list[PatientDTO]):
    patient_list = list[Patient]()
    for i in range(len(patient_dto_back)):
        patient = Patient()
        patient.id_patient = patient_dto_back[i].id_patient

        patient.firstname = patient_dto_back[i].firstname
        patient.last_name = patient_dto_back[i].last_name
        patient.middle_name = patient_dto_back[i].middle_name
        patient.snils = patient_dto_back[i].snils
        patient.document = patient_dto_back[i].document
        patient.phone = patient_dto_back[i].phone
        patient.date_of_birth = patient_dto_back[i].date_of_birth
        patient.address = patient_dto_back[i].address
        patient.polis_oms = patient_dto_back[i].polis_oms
        patient.gender = patient_dto_back[i].gender
        patient_list.append(patient)
    return patient_list

def getPatientDTO(patient_model_back: PatientDTO) -> PatientDTO:
    dto = PatientDTO()
    dto.id_patient = patient_model_back.id_patient
    dto.firstname = patient_model_back.firstname
    dto.last_name = patient_model_back.last_name
    dto.middle_name = patient_model_back.middle_name
    dto.snils = patient_model_back.snils
    dto.document = patient_model_back.document
    dto.date_of_birth = patient_model_back.date_of_birth
    dto.gender = patient_model_back.gender
    dto.phone = patient_model_back.phone
    dto.polis_oms = patient_model_back.polis_oms
    return dto


