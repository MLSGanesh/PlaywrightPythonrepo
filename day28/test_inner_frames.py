import pytest
from playwright.sync_api import Page,expect

def test_inner_frames(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    # frame 3
    frame3=page.frame(url="https://ui.vision/demo/webtest/frames/frame_3")
    frame3.locator("input[name='mytext3']").fill("Welcome")

    child_frames=frame3.child_frames
    print("Number of child frames:",len(child_frames))

    inner_frame=child_frames[0]
    radio=inner_frame.get_by_label("I am a human")
    radio.check()
    expect(radio).to_be_checked()

    page.wait_for_timeout(3000)