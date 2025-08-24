import pytest
from typing import List, Dict, Tuple, Set, Union, Any
from answer2 import convert_ints_to_strs


def test_simple_list() -> None:
    """测试简单列表转换"""
    input_obj: List[int] = [1, 2, 3]
    expected: List[str] = ["1", "2", "3"]
    result = convert_ints_to_strs(input_obj)
    assert result == expected


def test_nested_list() -> None:
    """测试嵌套列表转换"""
    input_obj: List[List[int]] = [[1, 2, 3]]
    expected: List[List[str]] = [["1", "2", "3"]]
    result = convert_ints_to_strs(input_obj)
    assert result == expected


def test_simple_dict() -> None:
    """测试简单字典转换"""
    input_obj: Dict[int, int] = {1: 2}
    expected: Dict[str, str] = {"1": "2"}
    result = convert_ints_to_strs(input_obj)
    assert result == expected


def test_dict_with_list() -> None:
    """测试字典包含列表的情况"""
    input_obj: Dict[int, List[int]] = {1: [1, 2, 3]}
    expected: Dict[str, List[str]] = {"1": ["1", "2", "3"]}
    result = convert_ints_to_strs(input_obj)
    assert result == expected


def test_complex_nested_structure() -> None:
    """测试复杂的嵌套数据结构"""
    # 修复第一个错误：在字典值类型中添加 None
    input_obj: Dict[str, Union[int, List[Any], Dict[Any, Any], Tuple[Any, ...], Set[Any], None]] = {
        "key1": 1,
        "key2": [2, 3, {"nested_key": 4}],
        "key3": (5, 6),
        "key4": {7, 8},
        "key5": None
    }

    result = convert_ints_to_strs(input_obj)
    assert isinstance(result, dict)

    # 修复第二个错误：移除冗余的 cast，直接使用 result
    assert result["key1"] == "1"
    assert result["key2"] == ["2", "3", {"nested_key": "4"}]
    assert result["key3"] == ("5", "6")
    assert set(result["key4"]) == {"7", "8"}
    assert result["key5"] is None


def test_mixed_types() -> None:
    """测试混合类型的数据结构"""
    input_obj: List[Union[int, str, float, bool, None]] = [1, "hello", 2.5, True, None]
    expected: List[Union[str, float, bool, None]] = ["1", "hello", 2.5, True, None]
    result = convert_ints_to_strs(input_obj)
    assert result == expected


def test_empty_structures() -> None:
    """测试空数据结构"""
    assert convert_ints_to_strs([]) == []
    assert convert_ints_to_strs({}) == {}
    assert convert_ints_to_strs(()) == ()
    assert convert_ints_to_strs(set()) == set()


def test_single_values() -> None:
    """测试单个值的转换"""
    assert convert_ints_to_strs(42) == "42"
    assert convert_ints_to_strs("hello") == "hello"
    assert convert_ints_to_strs(3.14) == 3.14
    assert convert_ints_to_strs(True) is True
    assert convert_ints_to_strs(False) is False
    assert convert_ints_to_strs(None) is None


def test_tuple_conversion() -> None:
    """测试元组转换"""
    input_obj: Tuple[int, int, int] = (1, 2, 3)
    expected: Tuple[str, str, str] = ("1", "2", "3")
    result = convert_ints_to_strs(input_obj)
    assert result == expected


def test_set_conversion() -> None:
    """测试集合转换"""
    input_obj: Set[int] = {1, 2, 3}
    result = convert_ints_to_strs(input_obj)
    assert isinstance(result, set)
    assert result == {"1", "2", "3"}
    assert len(result) == 3


@pytest.mark.parametrize("input_obj,expected", [
    (1, "1"),
    ([1, 2], ["1", "2"]),
    ({"a": 1}, {"a": "1"}),
    ((1,), ("1",)),
])
def test_parametrized_examples(input_obj: Any, expected: Any) -> None:
    """使用参数化测试多个示例"""
    result = convert_ints_to_strs(input_obj)
    assert result == expected