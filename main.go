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

type ИмяСтруктуры struct {
    ИмяПоля1 ТипПоля1
    ИмяПоля2 ТипПоля2
    ...
}

type User struct {
    Name  string
    Email string
    Age   int
}

type Book struct {
    Title     string
    Author    string
    ISBN      string
    PageCount int
}

var u User

type Config struct {
    Port     int    // экспортируемое поле
    logLevel string // неэкспортируемое поле
}

// User представляет зарегистрированного пользователя системы.
type User struct {
    Name  string // Полное имя
    Email string // Адрес электронной почты
    Age   int    // Возраст
}

type Event struct {
    ID        int
    Name      string
    Handler   func()
    IsActive  bool
}

type Empty struct{}

flags := map[string]struct{}{}
flags["ready"] = struct{}{}

// В Go так делать нельзя:
type Bad struct {
    A, B, C int // Это ошибка
}

type Product struct {
    ID    int     // Уникальный идентификатор товара
    Name  string  // Название товара
    Price float64 // Цена
}

type User struct {
    Name string
    Age  int
}

var u User
u.Name = "Иван"
u.Age = 30

fmt.Println(u.Name) // Выведет: Иван
fmt.Println(u.Age)  // Выведет: 30

fmt.Println(getUser().Name)


type Point struct {
    X int
    Y int
}

p := Point{10, 20}
fmt.Println(p.X) // 10
fmt.Println(p.Y) // 20

p := Point{
    Y: 20,
    X: 10,
}


var u User
fmt.Println(u.Name) // пустая строка ""
fmt.Println(u.Age)  // 0


u := new(User) // *User
u.Name = "Анна"
fmt.Println(u.Name) // Анна


type Product struct {
    Name  string
    Price float64
}

func main() {
    var p Product
    p.Name = "Ноутбук"
    p.Price = 54999.90

    fmt.Println(p.Name)  // Ноутбук
    fmt.Println(p.Price) // 54999.9

    // Изменим цену:
    p.Price = 49999.90
    fmt.Println(p.Price) // 49999.9
}




type Employee struct {
    FirstName string
    LastName  string
    Position  string
    Salary    float64
}

func main() {
    e := Employee{
        FirstName: "Олег",
        LastName:  "Иванов",
        Position:  "Разработчик",
        Salary:    85000.0,
    }

    fmt.Println(e.FirstName, e.LastName) // Олег Иванов
    fmt.Println(e.Position)              // Разработчик

    // Повышение зарплаты
    e.Salary += 5000.0
    fmt.Println("Новая зарплата:", e.Salary) // 90000.0
}



type Car struct {
    Brand string
    Year  int
}

func main() {
    car := &Car{
        Brand: "Toyota",
        Year:  2021,
    }

    fmt.Println(car.Brand) // Toyota

    // Обновим год выпуска
    car.Year = 2022
    fmt.Println(car.Year) // 2022
}


func NewUser(name string, age int) User {
    return User{
        Name: name,
        Age:  age,
    }
}


type User struct {
    Name string
    Age  int
}

func updateAge(u User) {
    u.Age = u.Age + 1
    fmt.Println("Внутри функции:", u.Age)
}

func main() {
    user := User{Name: "Анна", Age: 30}
    updateAge(user)
    fmt.Println("Снаружи функции:", user.Age)
}



func updateAgePtr(u *User) {
    u.Age = u.Age + 1
    fmt.Println("Внутри функции:", u.Age)
}

func main() {
    user := User{Name: "Анна", Age: 30}
    updateAgePtr(&user)
    fmt.Println("Снаружи функции:", user.Age)
}


type Product struct {
    Name  string
    Price float64
}

func printProduct(p Product) {
    fmt.Println("Товар:", p.Name, "Цена:", p.Price)
}

func main() {
    pr := Product{"Ноутбук", 59990.0}
    printProduct(pr)
}


func applyDiscount(p *Product, discount float64) {
    p.Price = p.Price * (1 - discount)
}

func main() {
    pr := Product{"Телевизор", 89990.0}
    applyDiscount(&pr, 0.1) // скидка 10%
    fmt.Println("После скидки:", pr.Price)
}


func newUser(name string, age int) User {
    return User{Name: name, Age: age}
}

func main() {
    u := newUser("Алексей", 28)
    fmt.Println(u.Name, u.Age)
}


func newUserPtr(name string, age int) *User {
    return &User{Name: name, Age: age}
}

func main() {
    u := newUserPtr("Ольга", 35)
    fmt.Println(u.Name, u.Age)
}


type Address struct {
    City    string
    ZipCode string
}

type User struct {
    Name    string
    Age     int
    Address Address
}


type ContactInfo struct {
    Email string
    Phone string
}

type Employee struct {
    Name        string
    Department  string
    Contact     ContactInfo
}


type Person struct {
    Name string
    Age  int
}

type Employee struct {
    Person     // анонимное встраивание
    Position   string
    Department string
}


type Address struct {
    City    string
    ZipCode string
}

type User struct {
    Name    string
    Address Address
}
Объявим переменную:

user := User{
    Name: "Ольга",
    Address: Address{
        City:    "Москва",
        ZipCode: "101000",
    },
}

fmt.Println(user.Address.City) // Выведет: Москва

user.Address.ZipCode = "105005"

user.Profile.Contact.Email




type Address struct {
    City    string
    Street  string
    ZipCode string
}

type User struct {
    Name    string
    Age     int
    Address Address
}

func main() {
    user := User{
        Name: "Андрей",
        Age:  27,
        Address: Address{
            City:    "Казань",
            Street:  "Улица Ленина",
            ZipCode: "420000",
        },
    }

    fmt.Println("Город:", user.Address.City)
    fmt.Println("Улица:", user.Address.Street)
}



type Position struct {
    Title string
    Level int
}

type Employee struct {
    Name     string
    Position Position
}

func promote(e *Employee) {
    e.Position.Level++
}

func main() {
    emp := Employee{
        Name: "Сергей",
        Position: Position{
            Title: "Инженер",
            Level: 1,
        },
    }

    promote(&emp)
    fmt.Println("Новый уровень:", emp.Position.Level) // 2
}



type ContactInfo struct {
    Email string
    Phone string
}

type Profile struct {
    Username    string
    ContactInfo ContactInfo
}

type Account struct {
    ID      int
    Profile Profile
}

func main() {
    acc := Account{
        ID: 1001,
        Profile: Profile{
            Username: "ivan_dev",
            ContactInfo: ContactInfo{
                Email: "ivan@example.com",
                Phone: "+79991234567",
            },
        },
    }

    fmt.Println("Email:", acc.Profile.ContactInfo.Email)
}


type User struct {
    Name string
}

func (u User) Greet() {
    fmt.Println("Привет,", u.Name)
}

user := User{Name: "Анна"}
user.Greet() // Привет, Анна


func (r TypeName) MethodName() {
    // тело метода
}


type Rectangle struct {
    Width  float64
    Height float64
}

// Метод, привязанный к Rectangle
func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}


type Counter struct {
    Value int
}

// Метод с получателем-значением
func (c Counter) IncrementByValue() {
    c.Value++
}

// Метод с получателем-указателем
func (c *Counter) IncrementByPointer() {
    c.Value++
}



func main() {
    c := Counter{Value: 10}

    c.IncrementByValue()
    fmt.Println(c.Value) // 10 — значение не изменилось

    c.IncrementByPointer()
    fmt.Println(c.Value) // 11 — значение изменилось
}


type Rectangle struct {
    Width  float64
    Height float64
}

func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}

func main() {
    rect := Rectangle{Width: 5, Height: 3}
    fmt.Println("Площадь:", rect.Area()) // 15
}


type User struct {
    Name string
    Age  int
}

func (u *User) SetAge(newAge int) {
    u.Age = newAge
}

func main() {
    user := User{Name: "Иван", Age: 25}
    user.SetAge(30)
    fmt.Println(user.Age) // 30
}



type BankAccount struct {
    Owner  string
    Balance float64
}

// Метод просмотра баланса
func (b BankAccount) GetBalance() float64 {
    return b.Balance
}

// Метод пополнения
func (b *BankAccount) Deposit(amount float64) {
    b.Balance += amount
}

// Метод списания
func (b *BankAccount) Withdraw(amount float64) bool {
    if amount > b.Balance {
        return false
    }
    b.Balance -= amount
    return true
}

func main() {
    account := BankAccount{Owner: "Мария", Balance: 1000}
    account.Deposit(500)
    success := account.Withdraw(300)

    fmt.Println("Баланс:", account.GetBalance()) // 1200
    fmt.Println("Списание прошло:", success)    // true
}


func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}
Функция:

func Area(r Rectangle) float64 {
    return r.Width * r.Height
}
