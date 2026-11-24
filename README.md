# Network Security Lab

Исследовательский инструмент для изучения методов защиты сетевого трафика: VPN, Proxy, анализ пакетов.

Школьный индивидуальный проект по теме сетевой безопасности.

## Возможности

- Управление сетевыми профилями (VPN, Proxy)
- Захват и анализ сетевых пакетов
- Измерение производительности соединений
- Сравнительные эксперименты: без защиты / SOCKS5 / HTTP CONNECT / WireGuard / Xray
- Desktop-интерфейс (PySide6) и CLI

## Быстрый старт

```bash
git clone https://github.com/Bantila/network-security-lab.git
cd network-security-lab

python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate  # Linux/macOS

pip install -e ".[dev]"
nsl info
```

## Запуск тестов

```bash
pytest
```

## Стек технологий

| Область | Технология |
|---|---|
| Язык | Python 3.11+ |
| GUI | PySide6 |
| Анализ пакетов | Scapy |
| VPN | WireGuard |
| Proxy engine | Xray-core |
| База данных | SQLite + SQLAlchemy 2.x |
| Графики | pyqtgraph |
| CLI | Click |
| Тестирование | pytest |

## Статус разработки

| Этап | Статус |
|---|---|
| 1. Foundation | ✅ Завершён |
| 2. Network Core | 🔄 В разработке |
| 3. Proxy Engine | ⏳ Запланировано |
| 4. VPN Manager | ⏳ Запланировано |
| 5. Traffic Analyzer | ⏳ Запланировано |
| 6. Benchmark Engine | ⏳ Запланировано |
| 7. Database | ⏳ Запланировано |
| 8. Desktop GUI | ⏳ Запланировано |
| 9. Release | ⏳ Запланировано |

## Структура проекта

```
network-security-lab/
├── src/network_security_lab/   # Основной пакет
│   ├── cli/                    # CLI-интерфейс
│   ├── core/                   # Бизнес-логика (сеть, VPN, proxy, анализ)
│   ├── application/            # Сервисы и интерфейсы
│   ├── infrastructure/         # Конфигурация, процессы, захват пакетов
│   ├── database/               # Модели SQLAlchemy
│   └── desktop/                # PySide6 GUI
├── tests/                      # pytest-тесты
└── docs/                       # Документация
```

## Лицензия

Учебный проект. Предназначен для анализа собственных устройств и сетей.
