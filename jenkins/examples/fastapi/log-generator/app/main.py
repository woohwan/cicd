from fastapi import FastAPI, HTTPException
import time

app = FastAPI()
log_filename = "tenant.log"


@app.get("/generate_raon_log/")
async def generate_log(count: int, interval: int):
    if count <= 0:
        raise HTTPException(status_code=400, detail="count는 1 이상이어야 합니다.")
    if interval <= 0:
        raise HTTPException(status_code=400, detail="interval은 1 이상이어야 합니다.")

    result = "success"

    with open(log_filename, "r") as logfile:
        lines = logfile.readlines()
        for line in lines:
            print(line)
            time.sleep(interval)

    return result
