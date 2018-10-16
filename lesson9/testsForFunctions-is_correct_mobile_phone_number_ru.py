from yandex_testing_lesson import is_correct_mobile_phone_number_ru


print('YES' if [True, False, True, False, True, False, True, False, False, False] == [
    is_correct_mobile_phone_number_ru(phoneNumber) for phoneNumber in ['+7(902)123-4567',
                                                                       '504))635(22))9	9',
                                                                       '8(902)1-2-3-45-67',
                                                                       '8FOX1833FOX'
                                                                       '8-9606667788',
                                                                       ' +7	8 32 6	8		2((35))3		4',
                                                                       '+79669658863',
                                                                       '+7+7+7+7+7+7',
                                                                       '',
                                                                       '020']
] else 'NO')
