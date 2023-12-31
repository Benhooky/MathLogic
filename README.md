# Лексическтй анализатор LexAnalyzer
 
Лабораторная работа № 1
Написать программу, которая выполняет лексический анализ входного текста в
соответствии с заданием и порождает таблицу лексем с указанием их типов и значений.
Текст на входном языке задается в виде символьного (текстового) файла. Программа
должна выдавать сообщения о наличие во входном тексте ошибок, которые могут быть
обнаружены на этапе лексического анализа.
Длина идентификатора и строковых констант ограничена 16 символами.
Программа должна допускать наличие комментариев неограниченной длины во входном
файле (форма комментариев выбирается самостоятельно).

Мой вариант

Входной язык содержит арифметические выражения, разделенные символом ; (точка с
запятой). Арифметические выражения состоят из идентификаторов, шестнадцатеричных
чисел, знака присваивания (:=), знаков операций +, –, *, / и круглых скобок.
Шестнадцатеричными числами считать последовательность цифр и символов a, b, c, d, e,
f, начинающуюся с цифры (например, 89, 45ac, 0abc).


# Конечный автомат для разделения больших чисел DeterAutomateForStrings

Этот проект представляет собой пример реализации детерминированного конечного автомата (DFA), спроектированного для анализа разделения в числах. Проект включает в себя два основных класса:

## Задача

По	заданному	регулярному	выражению	построить	вначале	
недетерминированный	конечный	автомат,	затем	детерминировать	его	
(переходы	можно	задавать	диапазонами).	Реализовать	программу,	которая	
проверяет	введенный	текст,	через	реализацию	конечного	автомата	
(варианты	ответа:	строка	соотвествует,	не	соотвествует,	символы	не	из	
алфавита).	Также	необходимо	реализовать	функцию	случайной	генерации	
верной	строки	по	полученному	конечному	автомату

### Мой вариант
6. Разделитель в больших числах
```regex
/\d{1,3}(?=(\d{3})+(?!\d))/g
```

## `State` (Состояние)
Представляет состояние конечного автомата. Класс `State` имеет методы для добавления переходов между состояниями и установки состояния по умолчанию.

## `FiniteAutomaton` (Детерминированный Конечный Автомат)
Создает и управляет конечным автоматом. Этот класс инициализирует состояния и определяет переходы между ними в соответствии с правилами анализа.

### Пример использования:
1. Создайте объект конечного автомата:

```python
automaton = FiniteAutomaton()
```
2. Вызовете метод process_string для строки:
```python
result = automaton.process_string(input_string)
```
Проект также включает вывод ошибок, указывая позицию и символ, вызвавший ошибку, для удобства отладки.

Этот простой конечный автомат можно легко настроить или расширить для анализа строк в соответствии с вашими собственными правилами.
