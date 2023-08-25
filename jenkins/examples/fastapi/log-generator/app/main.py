from fastapi import FastAPI, HTTPException
import random
import logging

app = FastAPI()

log_filename = "one.log"
logger = logging.getLogger(__name__)

console_handler = logging.StreamHandler()
# file_handler = logging.FileHandler('./output.log')

formatter = logging.Formatter('%(message)s')
console_handler.setFormatter(formatter)
# file_handler.setFormatter(formatter)


logger.addHandler(console_handler)
# logger.addHandler(file_handler)
logger.setLevel(level=logging.INFO)


@app.get("/")
async def log():
    return "app for log test"


@app.get("/generate_oneline_log/")
async def generate_log():

    result = ""

    with open(log_filename, "r") as logfile:
        lines = logfile.readlines()
        size = len(lines)
        line_number = random.randrange(0, size)
        logger.info(lines[line_number])
        result = lines[line_number]

    return result


@app.get("/generate_multi_log/")
async def generate_log():
    result = "success"
    logfile = "multi.log"

    with open(logfile, "r") as multi:
        lines = multi.readlines()
        for line in lines:
            logger.info(line.rstrip('\n'))

    return result
