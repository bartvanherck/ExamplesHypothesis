from hypothesis import given, strategies as st

def sort_function(numbers):
    return sorted(numbers)

@given(st.lists(st.integers()))
def test_sort_list(numbers):
    result = sort_function(numbers)
    assert isinstance(result, list)
    assert len(result) == len(numbers)
    assert all(x <= y for x, y in zip(result, result[1:]))
