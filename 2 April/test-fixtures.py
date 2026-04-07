"""
setup -  All code written before the yield statement executes first. This typically includes initializing the Selenium WebDriver (e.g., driver = Chrome()) and configuring initial settings like implicit waits or window sizing.
teardown -  Once the test completes (whether it passes or fails), pytest resumes the fixture at the line immediately following the yield. This is where you place cleanup commands like driver.quit(), ensuring the browser process is terminated and system resources are freed.

what goes bw setup and teardown is yield

fixture == setup+yield+teardown

usually a part test-conf file
"""

import pytest

@pytest.fixture(autouse=True) #scope as class or func can also be given
def greet():
    print("hello")
    yield
    print("goodbye")

def test_morning():
    print("goodmorning")

def test_evening():
    print("evening")