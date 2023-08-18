from fastapi import FastAPI, HTTPException
import time

# https통신을 위해 수정
app = FastAPI(title='EKS Project',
              description='EFK Test',
              openapi_url='/api/openapi.json')

log_filename = "tenant.log"
output = "output.log"


@app.get("/")
async def log():
    return "app for log test"


@app.get("/generate_raon_log/")
async def generate_log(interval: int):

    result = "success"

    with open(log_filename, "r") as logfile:
        with open(output, 'w+') as outlog:
            lines = logfile.readlines()
            for line in lines:
                print(line)
                outlog.write(line)
                outlog.flush()
                time.sleep(interval)

    return result
