from collections.abc import Iterable, Sequence
from typing import Literal, TypeAlias

ColorType: TypeAlias = Literal["rgb", "tuple"]

def sample_colorscale(
    colorscale: Sequence[str] | str,
    samplepoints: Iterable[float] | int,
    low: float = 0.0,
    high: float = 1.0,
    colortype: ColorType = "rgb",
) -> list[str] | list[tuple[float, float, float]]: ...
