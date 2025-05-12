if условие {
    // блок кода
} else if другое_условие {
    // блок кода
} else {
    // блок кода
}
if условие {
    // блок кода
} else if другое_условие {
    // блок кода
} else {
    // блок кода
}
age := 20
if age < 18 {
    fmt.Println("Несовершеннолетний")
} else if age < 65 {
    fmt.Println("Взрослый")
} else {
    fmt.Println("Пожилой")
}
if x > 0 {
    fmt.Println("Положительное число")
}
if (x > 0) { // ❌

if condition {
    // тело условия
}

if x := getValue(); x > 10 {
    fmt.Println("Значение больше 10")
}

switch day := 3; day {
case 1:
    fmt.Println("Понедельник")
case 2:
    fmt.Println("Вторник")
case 3:
    fmt.Println("Среда")
default:
    fmt.Println("Другой день")
}

switch {
case x > 0:
    fmt.Println("Положительное")
case x < 0:
    fmt.Println("Отрицательное")
default:
    fmt.Println("Ноль")
}

if (x > 0) { // ❌ Ошибка

if x > 0 { // ✅ Правильно

if x > 0
    fmt.Println("Да") // ❌

if x := getValue(); x > 10 {
    fmt.Println(x)
}

// Здесь x больше не существует ❌

for i := 1; i <= 10; i++ {
    fmt.Println(i)
}

i := 1
for i <= 10 {
    fmt.Println(i)
    i++
}
for x != 0 {
    // выполняем действия
}

for {
    // бесконечный цикл
}

for {
    var input string
    fmt.Print("Введите 'стоп' для выхода: ")
    fmt.Scanln(&input)

    if input == "стоп" {
        break
    }

    fmt.Println("Вы ввели:", input)
}

for i := 1; i <= 10; i++ {
    if i%2 == 0 {
        continue
    }
    fmt.Println(i) // напечатает только нечётные числа
}

for i := 1; i <= 10; {
    fmt.Println(i) // ❌ i не увеличивается
}
for i := 1; i > 10; i++



for i := 0; i < 3; i++ {}
fmt.Println(i)  // ❌ i не существует вне цикла

var age int
fmt.Scan(&age)

package main // Объявляем основной пакет программы

import (
    "fmt" // Импортируем пакет fmt для ввода/вывода
)

func main() {
    var age int // Объявляем переменную age типа int (целое число)

    fmt.Print("Введите ваш возраст: ") // Выводим приглашение ко вводу

    fmt.Scan(&age) // Считываем введённое пользователем число и сохраняем в переменную age

    // Начинаем конструкцию if-else для проверки возраста
    if age < 18 { // Если возраст меньше 18
        fmt.Println("Вы несовершеннолетний.") // Выводим соответствующее сообщение
    } else if age < 65 { // Иначе, если возраст меньше 65
        fmt.Println("Вы совершеннолетний.") // Выводим сообщение о совершеннолетии
    } else { // Во всех остальных случаях (то есть от 65 и выше)
        fmt.Println("Вы пенсионер.") // Сообщаем, что человек пенсионер
    }
}

package main // Основной пакет программы

import (
    "fmt" // Импортируем пакет fmt для ввода и вывода
)

func main() {
    var n int // Объявляем переменную n типа int

    fmt.Print("Введите положительное целое число: ") // Просим пользователя ввести число

    fmt.Scan(&n) // Считываем значение n с клавиатуры

    sum := 0 // Объявляем переменную sum и инициализируем её нулём — в ней будет храниться сумма

    // Цикл от 1 до n включительно
    for i := 1; i <= n; i++ {
        sum += i // На каждой итерации добавляем i к текущему значению sum
        // Например, при i = 1 → sum = 0 + 1
        // затем i = 2 → sum = 1 + 2 и т.д.
    }

    // После завершения цикла выводим итоговую сумму
    fmt.Printf("Сумма чисел от 1 до %d равна %d\n", n, sum)
}

if условие {
    // действия, если условие истинно
} else if другое_условие {
    // действия, если второе условие истинно
} else {
    // действия, если ни одно из условий не выполнено
}

package main

import "fmt"

func main() {
    age := 18

    if age >= 18 {
        fmt.Println("Доступ разрешён")
    }
}

package main

import "fmt"

func main() {
    temperature := 12

    if temperature < 10 {
        fmt.Println("Холодно")
    } else {
        fmt.Println("Тепло")
    }
}


package main

import "fmt"

func main() {
    score := 75

    if score >= 90 {
        fmt.Println("Оценка: A")
    } else if score >= 75 {
        fmt.Println("Оценка: B")
    } else if score >= 60 {
        fmt.Println("Оценка: C")
    } else {
        fmt.Println("Оценка: F")
    }
}

package main

import "fmt"

func main() {
    if x := 5; x%2 == 0 {
        fmt.Println("Чётное число")
    } else {
        fmt.Println("Нечётное число")
    }
}
