from celery import Celery 

app = Celery("app",
             broker="redis://localhost:6379",
             backend="db+sqlite:///results.db")

@app.task
def multiply(num1, num2):
    return num1 * num2