import pytest
from my_pytest.analytics import (
    filter_orders,
    calculate_total_revenue,
    count_orders_by_user,
    validate_order
)

# ---- Фикстура ----
@pytest.fixture
def orders():
    return [
        {"id": 1, "user": "alice", "amount": 100.0, "status": "completed"},
        {"id": 2, "user": "bob", "amount": 200.0, "status": "pending"},
        {"id": 3, "user": "alice", "amount": 50.0, "status": "completed"},
        {"id": 4, "user": "eve", "amount": 300.0, "status": "cancelled"},
    ]

# ---- Тесты фильтрации ----
def test_filter_completed(orders):
    completed = filter_orders(orders, "completed")
    assert len(completed) == 2
    assert all(o['status'] == "completed" for o in completed)

def test_filter_pending(orders):
    pending = filter_orders(orders, "pending")
    assert len(pending) == 1
    assert pending[0]['user'] == "bob"

def test_filter_invalid_status_type(orders):
    with pytest.raises(TypeError):
        filter_orders(orders, 123)

# ---- Тесты подсчёта выручки ----
def test_calculate_total_revenue(orders):
    assert calculate_total_revenue(orders) == 650.0

def test_calculate_total_revenue_empty():
    assert calculate_total_revenue([]) == 0.0

def test_calculate_total_revenue_invalid_order():
    with pytest.raises(ValueError):
        calculate_total_revenue([
            {"id": 1, "user": "alice", "amount": -100, "status": "completed"}
        ])

# ---- Подсчёт заказов по пользователю ----
def test_count_orders_by_user(orders):
    result = count_orders_by_user(orders)
    assert result == {"alice": 2, "bob": 1, "eve": 1}

def test_count_orders_empty():
    assert count_orders_by_user([]) == {}

# ---- Проверка валидации ----
def test_validate_order_valid():
    order = {"id": 5, "user": "mike", "amount": 120, "status": "completed"}
    assert validate_order(order) is True

def test_validate_order_missing_fields():
    with pytest.raises(ValueError):
        validate_order({"id": 5, "user": "mike", "amount": 120})

def test_validate_order_wrong_amount_type():
    with pytest.raises(ValueError):
        validate_order({"id": 5, "user": "mike", "amount": -10, "status": "completed"})

def test_validate_order_user_not_string():
    with pytest.raises(TypeError):
        validate_order({"id": 5, "user": 123, "amount": 100, "status": "completed"})
