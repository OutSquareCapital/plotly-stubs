from collections.abc import Iterable, Sequence

def sample_colorscale(
    colorscale: Sequence[str] | str,
    samplepoints: Iterable[float] | int,
    low: float = 0.0,
    high: float = 1.0,
    colortype: str = "rgb",
) -> list[object]: ...
