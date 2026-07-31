# 🎮 CS2 Stats Tracker

Веб-приложение для отслеживания и анализа личной статистики матчей в **Counter-Strike 2**. 
Позволяет сохранять результаты игр, отслеживать прогресс и анализировать ключевые показатели эффективности (K/D, винрейт).

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?logo=flask)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap)

## ✨ Возможности

- ➕ **Добавление матчей:** Удобная форма для ввода результатов (карта, счет, K/D/A, MVP).
-  **Глобальная статистика:** Подсчет общего винрейта, среднего K/D, количества побед и поражений.
- 📜 **История матчей:** Красивые карточки с историей всех сыгранных игр.
- 🗑️ **Управление:** Возможность удалять старые или ошибочно добавленные матчи.
-  **Темная тема:** Стильный дизайн с оранжевыми акцентами, приятный для глаз.
- 📱 **Адаптивность:** Полностью корректно отображается на мобильных устройствах и ПК.

## ️ Технологический стек

- **Backend:** Python, Flask, Flask-SQLAlchemy
- **Database:** SQLite
- **Frontend:** HTML5, CSS3, Bootstrap 5, Bootstrap Icons

## 🚀 Локальный запуск

Чтобы запустить проект локально на своем компьютере, выполните следующие шаги:

git clone https://github.com/ВАШ_НИК/cs2-stats.git
cd cs2-stats
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
