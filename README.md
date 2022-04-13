# HITS-testing-1
https://www.codewars.com/kata/61419e8f0d12db000792d21a  
Testing/main.py - решение задачи  
## Unit-тесты
Testing/test.py - тестирование  
Testing/main.py - решение задачи  
## Интеграционные тесты
Для интеграционного тестирования была создана копия БД с аналогичной структурой (чтобы имеющиеся данные не помешали тестирования, и тестирование не повредило имеющиеся данные)  
Testing/integrations_tests.py - тестирование  
Ниже представлено краткое описание проведенных тестов:  
![image](https://user-images.githubusercontent.com/80841734/162576806-fdc37f18-dc5b-42b3-ad2c-85c6c50e3a81.png)  
## E2E тесты  
Testing/Frontend/pages/index_testing.html - web страница, при помощи которой можно получать данные о формуле. Выполнено с использованием bootstrap.  
Testing/server.py - простой python сервер, к которому приходят запросы с frontend-а. Написан с использованием модуля http.server  
Testing/E2E/main.py - тестирование при помощи библиотеки selenium. Проверяется корректность работы системы, в зависимости от действий пользователя.  
