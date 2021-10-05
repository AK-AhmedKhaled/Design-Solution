# You are asked to contribute to the design for a very simple New Year's
# Eve countdown display. You already have the data definition given below.
# You need to design a function that consumes Countdown and produces an
# image showing the current status of the countdown.

# # no need for possiblw structure
# Countdown is one-of:
#     - false
#     - Natural [0, 10]
#     - 'complete'                  # Type Commment

# Interpretation: false not started yet, [0-10] current Countdown state, and 'complete' this dipaly message just done

#
countdown1 = False
countdown2 = 9    # just started
countdown3 = 2    # almost finishes
countdown4 = 0    # last tick
countdown5 = 'complete'   # Done

# # Template
# def fn_for_countDown(cd):
#     if (cd == False):
#         (...cd)
#     elif ( type(cd) == int && cd >= 0 && cd <= 10):
#         (...cd)
#     elif(cd == 'complete'):
#         (...cd)
# ;; Template rules used:
# ;;  - one of: 3 cases
# ;;  - atomic distinct: false
# ;;  - atomic non-distinct: Natural[1, 10]
# ;;  - atomic distinct: "complete"


#
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Countdown -> image   # signature

# purpose: consumes Countdown and produces an image showing the current status of the countdown.

# some Constants:
WIDTH = 220
HEIGHT = 190
FONT = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 26)

# stub
# def visualize_status(cd):
#     return Image.new("RGB", (0, 0))


# Function body: template was copied: Countdown Driven Temolate
def visualize_status(cd):
    img = Image.new("RGB", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    if (cd == False):
        status = 'SOON'
        draw.text((100, 80), status, font = FONT, align ="center")
        return img
    elif ( type(cd) is int and cd >= 0 and cd <= 10):
        status = str(cd)
        draw.text((100, 80), status, font = FONT, align ="center")
        return img
    elif(cd == 'complete'):
        status = 'COMPLETED'
        draw.text((100, 80), status, font = FONT, align ="center")
        return img
    else:
        raise Exception("This CountDown Counter can only recieve distict values: False, 'complete' and non distinct integer [0, 10]")

# Unit Tests and Examples:
def standard_image(status):
    img = Image.new("RGB", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    text = status
    draw.text((100, 80), text, font = FONT, align ="center")
    return img

def test_case_one():
    assert visualize_status(countdown3) == standard_image('2')
def test_case_two():
    assert visualize_status(countdown1) == standard_image('SOON')

if  __name__ == "__main__":
    test_case_one()
    test_case_two()
    print('All Tests Passed!')

# Debugging and Testing:
countdowns = [False, True, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1, 'finish','complete']
# countdowns = [False, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1,'complete']
for cd in countdowns:
    visualize_status(cd).show()
    # standard_image('2').save('countdown.png')
