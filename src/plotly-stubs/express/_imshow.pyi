from collections.abc import Iterable, Sequence
from typing import Any, Literal

import plotly.graph_objs as go
from plotly._stubs_helpers import ArrayLike, Templates

def imshow(
    img: ArrayLike,
    zmin: float | int | Iterable[float] | Iterable[int] | None = None,
    zmax: float | int | Iterable[float] | Iterable[int] | None = None,
    origin: Literal["upper", "lower"] | None = None,
    labels: dict[str, str] = {},
    x: Sequence[Any] | None = None,
    y: Sequence[Any] | None = None,
    animation_frame: int | str | None = None,
    facet_col: int | str | None = None,
    facet_col_wrap: int | None = None,
    facet_col_spacing: float | None = None,
    facet_row_spacing: float | None = None,
    color_continuous_scale: list[str] | str | None = None,
    color_continuous_midpoint: float | int | None = None,
    range_color: list[int] | list[float] | None = None,
    title: str | None = None,
    template: Templates | None = None,
    width: float | int | None = None,
    height: float | int | None = None,
    aspect: Literal["equal", "auto"] | None = None,
    contrast_rescaling: Literal["minmax", "infer"] | None = None,
    binary_string: bool | None = None,
    binary_backend: Literal["auto", "pil", "pypng"] = "auto",
    binary_compression_level: int = 4,
    binary_format: Literal["png", "jpg"] = "png",
    text_auto: bool | str = False,
) -> go.Figure: ...
