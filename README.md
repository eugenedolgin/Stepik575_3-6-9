# Stepik575_3-6-9
Repository Stepik575_3-6-9
https://stepik.org/course/575 "Автоматизация тестирования с помощью Selenium и Python"
https://stepik.org/lesson/237240/step/9?unit=209628  лекция 3.6 шаг 9
1. Репозиторий, в котором будут лежать файлы conftest.py и test_items.py.
2. Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.
3. Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя. Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
4. В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину. Например, можно проверять товар, доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
5. Тест должен запускаться с параметром language следующей командой:
   > pytest --language=es test_items.py

и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.
