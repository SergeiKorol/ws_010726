import requests


def test_add():
    """
    тест про добавление новой задачи
    """
    body = {"title": "generated", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]

    body = {"completed": True}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['completed'] == True
