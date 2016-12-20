# 3_bars

##Описание:
Скрипт bars.py позволяет найти ближайший, наибольший, и наименьший бары в списке. Файл со списком баров должен быть отдельно загружен: [список московских баров](http://data.mos.ru/opendata/7710881420-bary). 

##Запуск:
При запуске скрипта единственным параметром должен быть передан файл со списком баров. Скрипт предложит ввести ваши координаты широту и долготу; это могут быть дробные числа с разделителем точкой <.> .

Ошибки которые могут возникнуть:

1. Ошибка чтения: возможное повреждение файла, неправильная кодировка (должна быть utf-8).
2. Ошибка в поиске баров: возможное повреждение данных файла.
