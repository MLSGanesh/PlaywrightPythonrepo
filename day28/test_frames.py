import pytest
from playwright.sync_api import Page,expect

def test_frames(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")
    frames = page.frames
    print("Number of frames in page:", len(frames))

    # frame 1
    # frame1=page.frame_locator("frame[src="frame_1.html"]") # Option 1: get the frame using css
    frame1=page.frame(url="https://ui.vision/demo/webtest/frames/frame_1") # option 2: get the frame using url
    # frame1=page.frame(<"name of the frame">) # option 3: get the frame using name (here can't use this since name is not available)

    input_box=frame1.locator("input[name='mytext1']")
    input_box.fill("Hi")

    expect(input_box).to_have_value("Hi")

    page.wait_for_timeout(3000)