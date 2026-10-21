from fastapi import FastAPI

app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "Zig Zagler",
        "title": "FastAPI is awesome Men!"
        "content": "This is a really cool framework and is super fast.",
        "date_posted": "October 11, 2026",
    },
    {
        "id": 2,
        "author": "Nso Peter",
        "title": "Getting Better at FastAPI"
        "content": "This is a really coming along.",
        "date_posted": "October 15, 2026",

    },
]


@app.get("/")
def home():
    return {"message": "Hello World!"}


@app.get("/api/posts")
def get_posts():
    return posts