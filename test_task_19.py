import pytest
from app.application import Application


@pytest.fixture
def program(request):
    program = Application()
    request.addfinalizer(program.quit)
    return program


def test_work_with_cart(program):
    needed_products_in_cart = 3
    program.open_main_page()

    program.add_products(needed_products_in_cart)

    program.goto_cart_page()

    program.empty_cart()
