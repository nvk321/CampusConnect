from app import create_app, db
from app.models import User

def run():
    app = create_app()
    with app.app_context():
        admin = User.query.filter_by(username="admin").first()
        if not admin:
            db.session.add(User(username="admin"))
            db.session.commit()
            print("✅ Seeded: admin user")
        else:
            print("ℹ️ Admin user already exists, skipping.")

if __name__ == "__main__":
    run()
