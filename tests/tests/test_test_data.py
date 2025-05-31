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

def test_extract_links():
    with_links_path = 'tests/test_data/withLinks.html'
    with open(with_links_path, 'r', encoding='utf-8') as file:
        html = file.read()
        links = extract_links(html)
        assert len(links) == 2


def extract_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    return [link.get('href') for link in soup.find_all('a')]

# __file__

from pathlib import Path

def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename

def read_file(filename):
    return get_test_data_path(filename).read_text(encoding='utf-8')

def test_read():
    html = read_file('withLinks.html')
    links = extract_links(html)
    assert len(links) == 2
    