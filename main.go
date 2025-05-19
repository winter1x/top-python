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

switch x := 1; x {
case 1:
    fmt.Println("Один")
    fallthrouagh
case 2:
    fmt.Println("Два")
}

switch x := getValue(); {
case x > 10:
    fmt.Println("Больше десяти")
case x > 5:
    fmt.Println("Больше пяти")
default:
    fmt.Println("Пять или меньше")
}

if (x > 0) { // ❌ Ошибка

if x > 0 { // ✅ Правильно

if x > 0
    fmt.Println("Да") // ❌

if x := getValue(); x > 10 {
    fmt.Println(x)
}

// Здесь x больше не существует ❌

switch x {
case 1:
    fmt.Println("Один")
    fallthrough
case 2:
    fmt.Println("Два")
}

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
for i := 1; i > 10; i++ {
    fmt.Println(i)
}




for i := 0; i < 3; i++ {
    fmt.Println(i)
}

fmt.Println(i) // ❌ ошибка — i не существует вне цикла


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


package main

import "fmt"

func main() {
    day := "суббота"

    switch day {
    case "суббота", "воскресенье":
        fmt.Println("Выходной") // если день — суббота или воскресенье
    default:
        fmt.Println("Будний день") // для всех остальных дней
    }
}


package main

import "fmt"

func main() {
    grade := 3

    switch grade {
    case 5:
        fmt.Println("Отлично")
    case 4:
        fmt.Println("Хорошо")
    case 3:
        fmt.Println("Удовлетворительно")
    default:
        fmt.Println("Неудовлетворительно")
    }
}


package main

import "fmt"

func main() {
    score := 82

    switch {
    case score >= 90:
        fmt.Println("Оценка: A")
    case score >= 75:
        fmt.Println("Оценка: B")
    case score >= 60:
        fmt.Println("Оценка: C")
    default:
        fmt.Println("Оценка: F")
    }
}


package main

import "fmt"

func main() {
    temp := -5

    switch {
    case temp < 0:
        fmt.Println("Мороз") // температура ниже нуля
    case temp >= 0 && temp < 20:
        fmt.Println("Прохладно") // от 0 до 19
    default:
        fmt.Println("Тепло") // всё остальное (20 и выше)
    }
}

package main

import "fmt"

func main() {
    temp := -5

    switch {
    case temp < 0:
        fmt.Println("Мороз") // температура ниже нуля
    case temp >= 0 && temp < 20:
        fmt.Println("Прохладно") // от 0 до 19
    default:
        fmt.Println("Тепло") // всё остальное (20 и выше)
    }
}


package main

import "fmt"

func main() {
    x := 0

    for x < 5 { // пока x меньше 5
        fmt.Println(x) // выводим значение
        x++            // увеличиваем x на 1
    }
}

package main

import "fmt"

func main() {
    for i := 0; i < 5; i++ { // начинаем с i = 0, пока i < 5, увеличиваем i на 1
        fmt.Println(i) // выводим i на каждой итерации
    }
}


package main

import "fmt"

func main() {
    counter := 0

    for { // бесконечный цикл
        fmt.Println("Цикл номер", counter)
        counter++

        if counter == 3 { // условие выхода
            break // выход из цикла
        }
    }
}


switch {
case x > 10:
    // ...
case x > 5:
    // ...
}


for i := 0; i < 10; i++ {
    // обычный цикл
}

for condition {
    // как while
}

for {
    // бесконечный цикл
}

for ; i < 10; {
    // цикл без инициализации и пост-выражения
}

i := 0
for i < 5 {
    fmt.Println(i)
    // забыли i++
}

x := 10
if x > 5 {
    fmt.Println("A")
} else if x > 2 {
    fmt.Println("B")
} else {
    fmt.Println("C")
}

if n := 5; n < 10 {
    fmt.Println("Less than 10")
}
fmt.Println(n)

score := 75
switch {
case score >= 90:
    fmt.Println("A")
case score >= 70:
    fmt.Println("B")
default:
    fmt.Println("C")
}

i := 0
for i < 5 {
    fmt.Println(i)
}

for i := 1; i <= 5; i++ {
    fmt.Println(i)
}

for {
    fmt.Println("Ping")
}

x := 10
y := 5
if x > y {
    fmt.Println("A")
} else if x == y {
    fmt.Println("B")
} else {
    fmt.Println("C")
}

x := 10
for x < 20 {
    fmt.Println(x)
}

x := 10
switch x {
case 5:
    fmt.Println("Five")
case 10:
    fmt.Println("Ten")
default:
    fmt.Println("Other")
}

x := 7
if x > 5 && x < 10 {
    fmt.Println("In range")
} else {
    fmt.Println("Out of range")
}

for i := 0; i < 10; {
    fmt.Println(i)
}

x := 3
switch {
case x > 5:
    fmt.Println("Greater")
case x == 3:
    fmt.Println("Equal to 3")
default:
    fmt.Println("Other")
}

x := 15
if x < 10 {
    fmt.Println("Less")
} else if x > 10 {
    fmt.Println("Greater")
}


if x > 10 
{
	fmt.Println("x is greater than 10")
}



x := 10
if x = 10 {
	fmt.Println("x is ten")
}


switch day {
case "Monday":
	fmt.Println("Start of the week")
case "Friday":
	fmt.Println("End of the week")
}


for i := 1; i < 10; i++ {
	if i == 4 {
		break
	}
	fmt.Print(i)
}



package main

import "fmt"

func main() {
    // Инициализация переменной для ввода
    var age int

    // Цикл для 5 пользователей
    for i := 0; i < 5; i++ {
        // Запрос возраста у пользователя
        fmt.Print("Введите возраст: ")
        fmt.Scan(&age)

        // Определение статуса в зависимости от возраста
        if age < 18 {
            fmt.Println("Ребёнок")
        } else if age >= 18 && age <= 65 {
            fmt.Println("Взрослый")
        } else {
            fmt.Println("Пенсионер")
        }
    }
}
