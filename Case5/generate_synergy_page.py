from datetime import datetime
from pathlib import Path


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Наименование организации на базе, которой Вы проходите практическую подготовку</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="page-header">
        <h1>Наименование организации на базе, которой Вы проходите практическую подготовку</h1>
        <p class="subtitle">Университет «Синергия»</p>
    </header>
    <main class="content">
        <section class="card">
            <h2>Об организации</h2>
            <p>Университет «Синергия» — один из крупнейших негосударственных вузов России, основанный в 1988 году. Университет объединяет традиции фундаментального образования и современные технологии, уделяя повышенное внимание практической подготовке студентов.</p>
            <p>Сегодня «Синергия» реализует более 100 образовательных программ, охватывающих экономику, менеджмент, информационные технологии, гуманитарные науки, дизайн и искусство. Более 40&nbsp;000 студентов из 80 стран мира обучаются в кампусах и онлайн.</p>
        </section>
        <section class="card info-grid">
            <div>
                <h3>Основные направления</h3>
                <ul>
                    <li>Экономика, финансы и бизнес-администрирование</li>
                    <li>Информационные технологии и анализ данных</li>
                    <li>Менеджмент, маркетинг и предпринимательство</li>
                    <li>Психология, педагогика и творческие индустрии</li>
                </ul>
            </div>
            <div>
                <h3>Факты</h3>
                <ul>
                    <li>Более 30 лет успешной работы</li>
                    <li>Входит в топ частных вузов России</li>
                    <li>Собственная образовательная платформа Synergy Online</li>
                    <li>Партнерство с международными университетами и бизнесом</li>
                </ul>
            </div>
        </section>
        <section class="card contacts">
            <h3>Контакты</h3>
            <p><span class="label">Адрес:</span> 125284, г. Москва, Ленинградский проспект, д.&nbsp;80, корп.&nbsp;Г</p>
            <p><span class="label">Телефон:</span> +7&nbsp;(495)&nbsp;800-10-01</p>
            <p><span class="label">Сайт:</span> <a href="https://synergy.ru" target="_blank" rel="noopener noreferrer">synergy.ru</a></p>
        </section>
    </main>
    <footer class="page-footer">
        <p>&copy; {year} Университет «Синергия». Все права защищены.</p>
    </footer>
</body>
</html>
"""


CSS_TEMPLATE = """@import url('https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700&display=swap');

:root {
    --brand-red: #ed131c;
    --brand-dark: #1c1c1c;
    --brand-light: #f5f5f6;
    --card-bg: #ffffff;
    --border-color: #e0e1e5;
    --radius-lg: 24px;
    --radius-md: 16px;
    --shadow: 0 20px 60px rgba(0, 0, 0, 0.08);
}

*,
*::before,
*::after {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: 'Raleway', 'Helvetica Neue', Arial, sans-serif;
    font-weight: 400;
    color: var(--brand-dark);
    background: linear-gradient(180deg, var(--brand-light) 0%, #ffffff 40%, var(--brand-light) 100%);
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

.page-header {
    text-align: center;
    padding: 4rem 1.5rem 2rem;
    background: radial-gradient(circle at 50% 0%, rgba(237, 19, 28, 0.12), transparent 60%);
}

.page-header h1 {
    font-weight: 700;
    font-size: clamp(1.8rem, 2.5vw, 2.6rem);
    margin-bottom: 0.75rem;
    letter-spacing: -0.01em;
}

.subtitle {
    font-size: clamp(1.2rem, 1.8vw, 1.6rem);
    font-weight: 500;
    color: var(--brand-red);
}

.content {
    width: min(980px, 92vw);
    margin: 0 auto;
    display: grid;
    gap: 1.5rem;
    padding: 0 0 3rem;
}

.card {
    background-color: var(--card-bg);
    border-radius: var(--radius-lg);
    padding: 2.25rem;
    box-shadow: var(--shadow);
}

.card h2,
.card h3 {
    font-weight: 600;
    margin-bottom: 1rem;
}

.card p {
    line-height: 1.6;
    margin-bottom: 1rem;
}

.card ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.card li {
    position: relative;
    padding-left: 1.5rem;
    margin-bottom: 0.75rem;
}

.card li::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0.55rem;
    width: 0.7rem;
    height: 0.7rem;
    border-radius: 50%;
    background: var(--brand-red);
    box-shadow: 0 0 0 6px rgba(237, 19, 28, 0.1);
}

.info-grid {
    display: grid;
    gap: 1.5rem;
}

@media (min-width: 768px) {
    .info-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

.contacts .label {
    display: inline-block;
    min-width: 6.8rem;
    font-weight: 600;
    color: var(--brand-red);
}

.contacts a {
    color: var(--brand-dark);
    font-weight: 500;
    text-decoration: none;
    border-bottom: 1px solid rgba(237, 19, 28, 0.4);
    transition: color 0.2s ease, border-color 0.2s ease;
}

.contacts a:hover {
    color: var(--brand-red);
    border-color: var(--brand-red);
}

.page-footer {
    margin-top: auto;
    text-align: center;
    padding: 2rem 1rem;
    color: rgba(28, 28, 28, 0.7);
    font-size: 0.95rem;
}
"""


def generate_files(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    year = datetime.now().year
    html_content = HTML_TEMPLATE.format(year=year)
    (output_dir / "index.html").write_text(html_content, encoding="utf-8")
    (output_dir / "styles.css").write_text(CSS_TEMPLATE, encoding="utf-8")


def main() -> None:
    target_dir = Path(__file__).parent
    generate_files(target_dir)
    print(f"Страница сгенерирована в {target_dir.as_posix()}/index.html")


if __name__ == "__main__":
    main()

