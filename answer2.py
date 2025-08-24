from typing import Union, List, Dict, Tuple, Set, Any

# 定义返回类型别名以提高可读性
ReturnType = Union[str, float, bool, List[Any], Dict[Any, Any], Tuple[Any, ...], Set[Any], None]


def convert_ints_to_strs(obj: Union[int, str, float, bool, None,
List[Any], Dict[Any, Any], Tuple[Any, ...], Set[Any]]) -> ReturnType:
    """
    递归地将数据结构中的所有int转换为str

    Args:
        obj: 任意Python数据结构

    Returns:
        转换后的数据结构，所有int变为str
    """
    # 处理基本类型 - 特别注意bool不是int
    if isinstance(obj, int) and not isinstance(obj, bool):
        return str(obj)
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, float):
        return obj  # 直接返回，不需要 cast
    elif isinstance(obj, bool):
        return obj  # 直接返回，不需要 cast
    elif obj is None:
        return None

    # 处理列表
    elif isinstance(obj, list):
        result_list: List[Any] = []
        for item in obj:
            converted_item = convert_ints_to_strs(item)
            result_list.append(converted_item)
        return result_list

    # 处理字典
    elif isinstance(obj, dict):
        result_dict: Dict[Any, Any] = {}
        for key, value in obj.items():
            converted_key = convert_ints_to_strs(key)
            converted_value = convert_ints_to_strs(value)
            result_dict[converted_key] = converted_value
        return result_dict

    # 处理元组
    elif isinstance(obj, tuple):
        converted_items = []
        for item in obj:
            converted_items.append(convert_ints_to_strs(item))
        result_tuple: Tuple[Any, ...] = tuple(converted_items)
        return result_tuple

    # 处理集合
    elif isinstance(obj, set):
        result_set: Set[Any] = set()
        for item in obj:
            converted_item = convert_ints_to_strs(item)
            result_set.add(converted_item)
        return result_set

    # 其他类型直接返回
    return obj  # 直接返回，不需要 cast


if __name__ == "__main__":
    # 示例展示
    examples: List[Any] = [
        [1, 2, 3],
        [[1, 2, 3]],
        {1: 2},
        {1: [1, 2, 3]}
    ]

    for i, example in enumerate(examples, 1):
        result = convert_ints_to_strs(example)
        print(f"示例 {i}: {example} -> {result}")