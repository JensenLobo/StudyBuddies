from flask.testing import FlaskClient
from tests.utils import refresh_db, create_user
from src.models import users, db

#test to see if the home page (first route) is working, passed
def test_route(test_app: FlaskClient):
    res = test_app.get('/')
    assert res.status_code ==200
    assert b"Welcome to Study Buddies!" in res.data

#tests to see if the login page is working, passed
def test_login(test_app: FlaskClient):
    res = test_app.get('/login')
    assert res.status_code ==200

#tests to see if the profile Index page holds the values of the user's first and last name, failed
def test_get_user(test_app: FlaskClient):
    refresh_db()
    response = test_app.get('/profileIndex')
    assert response.status_code == 302
    with test_app.session_transaction() as session:
        session['id'] = 1
    res = test_app.post('/profile', data={
        'id': 1,
        'first_name': 'John',
        'last_name': 'Smith'
    }, follow_redirects=True)
    page_data = res.data.decode
    print(page_data)
    assert res.status_code == 200

    assert '<h1>Hi John Smith welcome to Study Buddies!</h1>' in page_data