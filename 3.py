import logging
logger = logging.getLogger("script2")
logging.basicConfig(level=logging.INFO)
while True:
    try:
        usr_input = int(raw_input("enter a number to check even or odd"))
        break
    except ValueError:
        logger.info("user input not valid try again with integer number")
if usr_input % 2 == 0:
    logger.info("Given number is even ({})".format(usr_input))
else:
    logger.info("Given number is odd ({})".format(usr_input))
