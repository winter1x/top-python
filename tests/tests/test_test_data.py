html = """
<div class="card mb-3"><div class="card-body"><div class="d-flex flex-column flex-sm-row">
<div class="d-flex flex-column mr-4"><div class="text-muted text-center mb-3">
<div class="h2 mb-0 font-weight-lighter">1</div><div class="small">Ответ</div></div>
<div class="text-muted text-center mb-3"><div class="h2 mb-0 font-weight-lighter">7</div>
<div class="small">Просмотров</div></div></div><div><h5 class="card-title">
<a href="/resumes/1">Backend Software Engineer</a></h5><div class="card-text">
<p>Программист-самоучка, избравший путь постоянного самосовершенствования.
Ценю красивый и лаконичный код, люблю функциональное программирование
(великая троица <code>map</code>, <code>filter</code>, <code>reduce</code>).</p>
<p>Использую JS, Ruby, PHP, Python, Elixir, Clojure в разной степени мастерства.</p>
<p>Восхищаюсь семейством LISP-языков, пишу свой интерпретатор LISP на Elixir.
В настоящий момент углубляюсь в ОС Unix, чтобы в дальнейшем улучшить навыки DevOps.</p>
</div><div class="text-right small"><span class="mr-3 text-muted">12 дней</span>
<a href="/users/6">Улугбек Туйчиев</a></div></div></div></div></div>
"""

"""links = extract_links(html)
print(links)"""
from bs4 import BeautifulSoup
import os
def extract_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    return [link.get('href') for link in soup.find_all('a')]

"""def test_extract_links():
    with_links_path = 'test_data/withLinks.html'
    with open(with_links_path, 'r', encoding='utf-8') as file:
        html = file.read()
        links = extract_links(html)
        assert len(links) == 2"""
# __file__ - путь к файлу, в котором вызывается функция
"""
current_dir = os.path.dirname(os.path.abspath(__file__))

before_html = open(os.path.join(current_dir, '..', 'test_data', 'before.txt'), 'r').read()
result = open(os.path.join(current_dir, '..', 'test_data', 'result.txt'), 'r').read()
"""

from pathlib import Path

def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename

def read_file(filename):
    return get_test_data_path(filename).read_text(encoding='utf-8')

def test_read():
    html = read_file('withLinks.html')
    links = extract_links(html)
    assert len(links) == 2

html = """
<div class="content">
   <a href="/home">Главная</a>
   <div class="nav">
       <a href="/about">О нас</a>
       <a href="/contacts">Контакты</a>
   </div>
   <div class="footer">
       <a href="/terms">Условия</a>
       <a href="https://external.com">Внешняя ссылка</a>
   </div>
</div>
"""

"""links = extract_links(html)
assert len(links) == 5
assert links == ['/home', '/about', '/contacts', '/terms', 'https://external.com']
"""

"""
if send_greeting_email(user):
    pass

assert send_greeting_email(user) is True
"""

# user_names = read_user_names(path='/etc/passwd')

"""def test_read_user_names():
    passwd_path = 'fixtures/passwd'
    user_name = read_user_names(passwd_path)
    assert user_name == ['root', 'test_user']

log = Logger('development.log')
log('first message')
#'development.log'
#'first message'
log('second message')
#'development.log'
#'first message'
#'second message'

"""

"""
params = {
    'email': 'lala@example.com',
    'password': 'qwerty',
}

# register_user(params)


from mailer import send_email
mailer.test = True

def register_user(send=send_email, **params):
    user = User(**params)
    user.save()
    send_email("registration", user)
    return user.id

def fake_send_email(*args, **kwargs):
    print('sending...', args, kwargs)

def test_register_user():
    id = register_user(name='Mike', send=fake_send_email)
    user = User.objects.get(id)
    assert user.name == 'Mike'
    
"""
#C:\Users\Ефимов\AppData\Local\
def test_create_file(tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()
    p = d / 'hello.txt'
    p.write_text('hello')

    assert p.read_text() == 'hello'
    assert len(list(tmp_path.iterdir())) == 1

def my_fakefs_test(fs):
    fs.create_file('/var/data/xx1.txt')
    assert os.path.exists('/var/data/xx1.txt')

"""
@pytest.fixture(autouse=True)
def transaction(conection):
    conection.begin()
    yield
    conection.rollback()

def test_register_user():
    id = register_user(name='Mike')
    user = User.objects.get(id)
    assert user.name == 'Mike'"""