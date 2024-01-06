import openpyxl
from account.models import User
from django.conf import settings

EXCEL_PATH = settings.BASE_DIR / 'utils'
BASE_EXCEL_PATH = EXCEL_PATH / 'base.xlsx'
SAVE_EXCEL_PATH = EXCEL_PATH


def to_excel(queryset: User):
    datas = list(queryset)

    wb = openpyxl.load_workbook(BASE_EXCEL_PATH)
    ws = wb.active
    for data in datas:
        print((data.phone_number, data.full_name, data.type, data.study_center,
               data.subject, data.passport_or_id_number, data.created_at, data.salary_percentage))

        if data.subject:
            ws.append((data.phone_number, data.full_name, data.type, data.study_center.name,
                      data.subject.name, data.passport_or_id_number, data.created_at, data.salary_percentage))
        elif not data.subject:
            ws.append((data.phone_number, data.full_name, data.type, data.study_center.name,
                      ' ', data.passport_or_id_number, data.created_at, data.salary_percentage))
        
        if data.subject:
            ws.append((data.phone_number, data.full_name, data.type, data.study_center.name,
                      data.subject.name, data.passport_or_id_number, data.created_at, data.salary_percentage))
        elif not data.subject:
            ws.append((data.phone_number, data.full_name, data.type, data.study_center.name,
                      ' ', data.passport_or_id_number, data.created_at, data.salary_percentage))
        
    wb.save('teacher.xlsx')
    return f'{EXCEL_PATH}/teacher.xlsx'
