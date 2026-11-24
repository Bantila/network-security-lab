# ROADMAP — Network Security Lab

## Версии и этапы

### v0.1 — Foundation ✅
**Цель**: работающий скелет проекта.

Задачи:
- [x] Структура проекта (src layout, модули)
- [x] pyproject.toml с зависимостями
- [x] CLI-команды: `nsl info`, `nsl network status`
- [x] Конфигурация приложения (AppSettings)
- [x] Логирование
- [x] Базовые тесты (pytest)
- [x] README, ARCHITECTURE, ROADMAP

Критерий: `pip install -e .` и `nsl --version` работают, `pytest` проходит.

---

### v0.2 — Network Core 🔄
**Цель**: базовые сетевые операции через CLI.

Задачи:
- [ ] `NetworkInterface` — перечисление интерфейсов, IP-адреса
- [ ] `PingProbe` — ICMP ping, измерение RTT
- [ ] `DnsResolver` — DNS-запросы, анализ ответов
- [ ] `TcpProbe` — проверка TCP-доступности порта
- [ ] CLI: `nsl network interfaces`, `nsl network ping`, `nsl network dns`, `nsl network tcp-check`
- [ ] Тесты с mock для сетевых вызовов

Критерий: `nsl network ping 8.8.8.8` выводит RTT, тесты проходят.

---

### v0.3 — Proxy Engine 🔄
**Цель**: создание и проверка прокси-соединений.

Задачи:
- [ ] `Socks5Client` — учебная реализация SOCKS5 на Python
- [ ] `HttpConnectProxy` — учебная реализация HTTP CONNECT
- [ ] `XrayManager` — управление процессом xray-core
- [ ] CLI: `nsl proxy test`, `nsl proxy start`, `nsl proxy stop`
- [ ] Тесты: unit для парсинга ответов, integration с mock-сервером

Критерий: приложение может установить соединение через SOCKS5.

---

### v0.4 — VPN Manager 🔄
**Цель**: управление WireGuard-подключениями.

Задачи:
- [ ] `WireGuardManager` — импорт конфигураций, start/stop, статус
- [ ] Поддержка Windows (`wg.exe`, `wireguard.exe`) и Linux (`wg-quick`)
- [ ] Валидация конфигураций перед применением
- [ ] CLI: `nsl vpn import`, `nsl vpn connect`, `nsl vpn disconnect`, `nsl vpn status`

Критерий: `nsl vpn status` показывает состояние WireGuard.

---

### v0.5 — Traffic Analyzer 🔄
**Цель**: захват и анализ сетевых пакетов.

Задачи:
- [ ] `PacketCapture` — захват через Scapy, поддержка Npcap (Windows)
- [ ] `PacketParser` — разбор IP, TCP, UDP, DNS заголовков
- [ ] `CaptureSession` — управление сессиями захвата
- [ ] Экспорт в PCAP/PCAPNG
- [ ] CLI: `nsl capture start`, `nsl capture stop`, `nsl capture export`

Критерий: `nsl capture start --iface eth0 --duration 10` создаёт файл захвата.

---

### v0.6 — Benchmark Engine 🔄
**Цель**: сравнительные эксперименты по производительности.

Задачи:
- [ ] `BenchmarkEngine` — измерение RTT, jitter, throughput, packet loss
- [ ] `ExperimentRunner` — повторяемые тесты, сравнение сценариев
- [ ] Сценарии: Direct / SOCKS5 / HTTP CONNECT / WireGuard / Xray
- [ ] Экспорт результатов в CSV и JSON

Критерий: `nsl bench run --scenario direct` сохраняет результаты.

---

### v0.7 — Database 🔄
**Цель**: персистентное хранение данных.

Задачи:
- [ ] SQLAlchemy модели: `ConnectionProfile`, `Experiment`, `ExperimentResult`, `CaptureSession`
- [ ] SQLite + Alembic миграции
- [ ] Репозитории для каждой модели
- [ ] Привязка к сервисам

Критерий: данные сохраняются между запусками.

---

### v0.8 — Desktop GUI 🔄
**Цель**: полноценный desktop-интерфейс.

Задачи:
- [ ] PySide6 главное окно, тёмная тема
- [ ] Dashboard: состояние сети, активное подключение, IP
- [ ] Connections: список профилей, подключение/отключение
- [ ] Traffic Analyzer: таблица пакетов, фильтрация, графики
- [ ] Experiments: создание, запуск, результаты
- [ ] History: история экспериментов, экспорт

Критерий: основные функции доступны через GUI.

---

### v1.0 — Release 🔄
**Цель**: готовое к демонстрации приложение.

Задачи:
- [ ] Интеграционные тесты
- [ ] Проверка на Windows
- [ ] PyInstaller сборка
- [ ] Документация для защиты
- [ ] Демонстрационный сценарий

---

## Технические риски

| Риск | Вероятность | Митигация |
|------|------------|-----------|
| Npcap требует прав администратора на Windows | Высокая | Добавить UAC-манифест, документировать требование |
| WireGuard API различается на Windows/Linux | Средняя | Абстракция `WireGuardManager` с платформо-специфичными бэкендами |
| Scapy медленно на больших объёмах трафика | Средняя | Ограничение фильтрами BPF, сохранение в PCAP |
| PySide6 + asyncio интеграция | Средняя | Использовать `asyncio` в отдельном потоке + сигналы Qt |
