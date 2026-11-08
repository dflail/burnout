import config
import sys
from repositories import ApplicationRepository, LocalSQLiteRepository

def manage_data():
    if config.APP_ENV == "development":
        repo: ApplicationRepository = LocalSQLiteRepository(db_path=config.DB_PATH)
        run_app_workflow(repo)
    else:
        sys.exit("Data management is currently only allowed in development environment.")

def run_app_workflow(repo: ApplicationRepository) -> None:
    # Initialize the database
    repo.init_db()

    # Create a new application
    company = "ZXS Tech"
    role = "Software Engineer"
    app_id = repo.create(company, role)
    print(f"Created application with ID: {app_id}")

    # List all applications
    applications = repo.list_all()
    print("All applications:")
    for app in applications:
        print(app)

    # Get application by ID
    record = repo.get_by_id(app_id)
    if record is None:
        print(f"Application #{app_id} not found.")
    else:
        print(f"Found record: {record['company']} - {record['role']}")
        repo.update(app_id, "ZXS Tech", "Senior Software Engineer")
        print(f"Updated application #{app_id}.")

    # Delete the application
    repo.delete(app_id)
    print(f"Deleted application #{app_id}.")

    # List all applications
    applications = repo.list_all()
    print("All applications:")
    for app in applications:
        print(app)

    
    


if __name__ == "__main__":
    manage_data()
