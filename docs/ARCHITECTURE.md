# Architecture — Network Security Lab

## Архитектурный стиль

**Modular Monolith** — единое приложение, разделённое на независимые модули с чёткими границами ответственности.

Выбор обоснован: проект учебный, команда одна, desktop-приложение без микросервисного деплоя. Монолит с модульной границей проще в разработке и отладке, при этом модули легко переносятся при необходимости.

## Принципы

1. **Core независим от GUI** — бизнес-логика в `core/` не импортирует ничего из `desktop/`
2. **Одна логика для CLI и GUI** — оба используют `application/services/`
3. **Чёткая ответственность** — каждый модуль решает одну задачу
4. **Нет преждевременных абстракций** — интерфейсы добавляются при наличии реальных причин
5. **GUI не блокируется** — длительные операции выполняются в asyncio/threads, результат передаётся через сигналы PySide6

## Слои

```
┌─────────────────────────────────────────────┐
│          Desktop (PySide6 / QML)            │  UI-слой
├─────────────────────────────────────────────┤
│           CLI (Click)                       │  Второй UI-слой
├─────────────────────────────────────────────┤
│        Application / Services               │  Оркестрация
├──────────────┬──────────────────────────────┤
│    Core      │    Infrastructure            │  Бизнес-логика и системные операции
│  network/    │    processes/                │
│  proxy/      │    packet_capture/           │
│  vpn/        │    configuration/            │
│  analyzer/   │                              │
│  benchmark/  │                              │
├──────────────┴──────────────────────────────┤
│          Database (SQLite + SQLAlchemy)      │  Хранение данных
└─────────────────────────────────────────────┘
```

## Модули

### `core/network/`
Базовые сетевые операции: интерфейсы, IP, ping, DNS, TCP-проверки.
Зависимости: только stdlib + scapy.

### `core/proxy/`
SOCKS5 и HTTP CONNECT реализации. Управление Xray-core процессом.
Зависимости: socket, subprocess.

### `core/vpn/`
Управление WireGuard через системные вызовы. Импорт конфигураций.
Зависимости: subprocess, platform.

### `core/analyzer/`
Захват пакетов через Scapy. Парсинг заголовков. Экспорт PCAP.
Зависимости: scapy, pcapy (опционально).

### `core/benchmark/`
Измерение RTT, jitter, throughput, packet loss. Сравнение сценариев.
Зависимости: socket, asyncio, core/network.

### `application/services/`
Use cases: ExperimentService, ConnectionService, CaptureService.
Оркестрирует core-модули, сохраняет результаты через database.

### `infrastructure/configuration/`
Настройки приложения. Нет секретов — только пути и параметры окружения.

### `database/`
SQLAlchemy модели: ConnectionProfile, Experiment, ExperimentResult, CaptureSession.
Миграции через Alembic (добавляется в этапе 7).

### `cli/`
Click-команды. Только форматирование ввода/вывода, вся логика в services.

### `desktop/`
PySide6 приложение. ViewModels для привязки данных. QML или Widgets — решается в этапе 8.

## Поток данных (пример: запуск эксперимента)

```
CLI/GUI
  → ExperimentService.run(scenario, params)
    → BenchmarkEngine.measure(connection_type)
      → NetworkCore / ProxyEngine / VPNManager
    → ExperimentRepository.save(result)
  → Результат возвращается в CLI/GUI
```

## Решения по безопасности

- Приватные ключи WireGuard хранятся в зашифрованном хранилище ОС (keyring)
- Секреты не пишутся в логи — фильтр на уровне обработчиков
- Команды из импортируемых конфигураций не выполняются напрямую
- Scapy запускается с минимальными необходимыми правами
