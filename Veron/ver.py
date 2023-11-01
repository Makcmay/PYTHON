import pandas as pd

# Считываем CSV файл с контактами из телефона
contacts_phone = pd.read_csv('contacts.csv')

# Считываем Excel файл с дополнительной информацией о контактах
contacts_excel = pd.read_excel('Выборн.xlsx')

# # Объединяем данные из CSV и Excel файлов по полю 'Имя' контакта
# merged_contacts = contacts_phone.merge(contacts_excel, on='Имя', how='left')

# # Сохраняем объединенные контакты в новый CSV файл
# merged_contacts.to_csv('merged_contacts.csv', index=False)
