import os

HERE = os.path.dirname(os.path.abspath(__file__))
HERO = os.path.join(os.path.dirname(HERE), '..', 'clinical-journal-hero.html')
HERO = os.path.normpath(os.path.join(HERE, '..', 'clinical-journal-hero.html'))

with open(os.path.join(HERE, 'src-hero.html'), encoding='utf-8') as f:
    hero = f.read()
with open(os.path.join(HERE, 'sections.html'), encoding='utf-8') as f:
    sections = f.read()

FAVICON = "data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20100%20100'%3E%3Ctext%20y='.9em'%20font-size='90'%3E%F0%9F%AB%80%3C/text%3E%3C/svg%3E"

head = """<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>История болезни № 001 — для Наташи</title>
<meta name="description" content="Личный клинический журнал. Доступ только для одного читателя.">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#efe7d2">
<meta property="og:title" content="История болезни № 001">
<meta property="og:description" content="Диагноз поставлен. Лечение назначено. Прогноз: навсегда.">
<meta property="og:type" content="website">
<link rel="icon" href="__FAVICON__">
<style>html{background:#efe7d2}body{margin:0}</style>
</head>
<body>
""".replace('__FAVICON__', FAVICON)

tail = "\n</body>\n</html>\n"

index = head + "\n" + hero.strip() + "\n" + sections.strip() + tail

out = os.path.join(HERE, 'index.html')
with open(out, 'w', encoding='utf-8', newline='\n') as f:
    f.write(index)
print('index.html собран:', os.path.getsize(out), 'байт')
