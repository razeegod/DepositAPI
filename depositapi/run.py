import uvicorn


def main():
    uvicorn.run("main:app", host="localhost", port=80, reload=False)


if __name__ == "__main__":
    main()