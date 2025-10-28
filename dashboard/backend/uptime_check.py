import requests
import time
import json

def lambda_handler(event, context):
    urls = ["https://google.com", "https://audible.com"]
    results = []

    for url in urls:
        start = time.time()
        try:
            response = requests.get(url, timeout=5)
            status = "UP" if response.status_code == 200 else "DOWN"
        except Exception as e:
            status = "DOWN"
        end = time.time()
        results.append({"url": url, "status": status, "response_time": round(end - start, 2)})

    return {
        "statusCode": 200,
        "body": json.dumps(results)
    }

if __name__ == "__main__":
    mock_event = {}
    mock_context = None
    print(lambda_handler(mock_event, mock_context))

