import allure


@allure.feature('test_module_01')
@allure.story('test_story_o1')
def test_answer():
    """
    用例描述1：test case 01

    """
    assert 1 + 2 == 2
