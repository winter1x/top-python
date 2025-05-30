import requests
import re

def clean_html(raw_html):
    """Удаляет HTML-теги из текста."""
    cleanr = re.compile('<.*?>')
    return re.sub(cleanr, '', raw_html or '')

def search_show(query):
    url = f"https://api.tvmaze.com/search/shows?q={query}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_seasons(show_id):
    url = f"https://api.tvmaze.com/shows/{show_id}/seasons"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_episodes(show_id):
    url = f"https://api.tvmaze.com/shows/{show_id}/episodes"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def main():
    query = "Friends"
    shows = search_show(query)

    if not shows:
        print("Шоу не найдено")
        return

    print(f"Результаты поиска для '{query}':\n")

    for idx, item in enumerate(shows[:5], start=1):  # Покажем первые 5 шоу
        show = item['show']
        name = show.get('name', 'N/A')
        premiered = show.get('premiered', 'N/A')
        genres = ', '.join(show.get('genres', []))
        summary = clean_html(show.get('summary', ''))
        summary_short = summary[:200] + ('...' if len(summary) > 200 else '')

        print(f"{idx}. {name} (Премьера: {premiered})")
        print(f"   Жанры: {genres}")
        print(f"   Описание: {summary_short}\n")

    # Возьмём первое шоу для дальнейшего анализа
    show_id = shows[0]['show']['id']
    print(f"Информация о сезонах шоу ID={show_id}:\n")

    seasons = get_seasons(show_id)
    for season in seasons:
        num = season.get('number', 'N/A')
        start = season.get('premiereDate', 'N/A')
        end = season.get('endDate', 'N/A')
        print(f"Сезон {num}: с {start} по {end}")

    print("\nИнформация об эпизодах:\n")
    episodes = get_episodes(show_id)
    print(f"Всего эпизодов: {len(episodes)}")
    for ep in episodes[:5]:
        ep_num = ep.get('number', 'N/A')
        ep_name = ep.get('name', 'N/A')
        ep_airdate = ep.get('airdate', 'N/A')
        print(f"Эпизод {ep_num}: {ep_name} (Дата выхода: {ep_airdate})")

if __name__ == "__main__":
    main()
