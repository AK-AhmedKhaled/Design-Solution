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
