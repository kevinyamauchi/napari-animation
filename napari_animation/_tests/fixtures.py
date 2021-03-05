import pytest
from napari.utils._testsupport import make_napari_viewer  # noqa: F401

from napari_animation import Animation


@pytest.fixture
def empty_animation(make_napari_viewer):  # noqa: F811
    viewer = make_napari_viewer()
    animation = Animation(viewer)
    return animation


@pytest.fixture
def animation_with_keyframes(empty_animation):
    for i in range(2):
        empty_animation.capture_keyframe()
        empty_animation.viewer.camera.zoom *= 2
    return empty_animation


@pytest.fixture
def viewer_state(empty_animation):
    return empty_animation._get_viewer_state()
