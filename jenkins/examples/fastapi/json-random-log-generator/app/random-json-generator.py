from fastapi import FastAPI, HTTPException
import json
import random
import time

app = FastAPI()

######################################################################################
# Apache log generation
######################################################################################

# 로그 파일 경로 및 이름
apache_logfile = "apache_logs.json"

# 사용자 정보 목록
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    # 다른 사용자 에이전트를 추가할 수 있습니다.
]

# 요청 메서드 목록
request_methods = ["GET", "POST", "PUT", "DELETE"]

# URL 경로 목록
url_paths = ["/home", "/about", "/contact", "/products", "/services"]

# 상태 코드 목록
status_codes = [200, 201, 204, 400, 404, 500]


def generate_random_apache_json_log():
    # 현재 시간 생성
    timestamp = int(time.time())

    # 랜덤한 사용자 에이전트 선택
    user_agent = random.choice(user_agents)

    # 랜덤한 요청 메서드 선택
    request_method = random.choice(request_methods)

    # 랜덤한 URL 경로 선택
    url_path = random.choice(url_paths)

    # 랜덤한 상태 코드 선택
    status_code = random.choice(status_codes)

    # 로그 메시지 생성
    log_data = {
        "timestamp": timestamp,
        "user_agent": user_agent,
        "request_method": request_method,
        "url_path": url_path,
        "status_code": status_code
    }

    return log_data

######################################################################################
# random json og generation
######################################################################################


def generate_random_json():
    data = {
        "random_number": random.randint(1, 100),
        "random_string": ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10)),
        "timestamp": int(time.time())
    }
    return data


@app.get("/generate_random_json/")
async def generate_random_json_endpoint(count: int, interval: int):
    if count <= 0:
        raise HTTPException(status_code=400, detail="count는 1 이상이어야 합니다.")
    if interval <= 0:
        raise HTTPException(status_code=400, detail="interval은 1 이상이어야 합니다.")

    filename = "output.json"
    result = []

    with open(filename, "a") as jsonfile:

        for i in range(count):
            data = generate_random_json()
            result.append(data)
            print(data)
            json.dump(data, jsonfile, separators=(',', ': '))
            jsonfile.write('\n')
            # interval 초만큼 대기
            time.sleep(interval)

    return result


@app.get("/generate_apache_log_json/")
async def generate_random_json_endpoint(count: int, interval: int):
    if count <= 0:
        raise HTTPException(status_code=400, detail="count는 1 이상이어야 합니다.")
    if interval <= 0:
        raise HTTPException(status_code=400, detail="interval은 1 이상이어야 합니다.")

    result = []

    with open(apache_logfile, "a") as jsonfile:

        for i in range(count):
            data = generate_random_apache_json_log()
            result.append(data)
            print(data)
            json.dump(data, jsonfile, separators=(',', ': '))
            jsonfile.write('\n')
            # interval 초만큼 대기
            time.sleep(interval)

    return result
