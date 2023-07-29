from .categories import BasicEducation


def test_if_category_return_abstract_function():
    call = BasicEducation()
    call.create_user()
