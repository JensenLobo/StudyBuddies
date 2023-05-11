from src.models import users, db

def refresh_db():
    users.query.delete()
    db.session.commit()

def create_user(usersname='testing@uncc.edu', password_hash='abc123', user_major='no major', first_name='John', last_name='Smith', major_changed_count=0) -> users:
    test_user = users(username=usersname, password_hash=password_hash, major=user_major, first_name=first_name, last_name=last_name, major_changed_count=major_changed_count)
    db.session.add(test_user)
    db.session.commit()
    return test_user