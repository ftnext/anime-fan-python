from fastapi import FastAPI

app = FastAPI()


@app.get("/sakana")
async def chisato():
    return "ちんあなごー🙌"
