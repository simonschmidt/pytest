from dataclasses import dataclass
from dataclasses import field


def test_sequence_of_dataclasses() -> None:
    @dataclass
    class SimpleDataObject:
        field_a: int = field()
        field_c: list[str] = field()

    a = SimpleDataObject(1, ["foo", "bar"])
    b = SimpleDataObject(2, ["foo", "foo"])

    left = [a, a]
    right = [a, b]
    assert left == right

