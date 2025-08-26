# How to Run the FastAPI + SQLModel POC

1. **Build the Docker images:**

   ```sh
   make build
   ```

2. **Start the services in the background:**

   ```sh
   make up
   ```


3. **Test the API endpoints:**

   You can use the HTTP files in the `test` directory with the REST Client extension in VS Code, or copy the requests to your preferred tool:

   - `test/endpoints.http` contains example requests for creating a company, creating a customer, and listing customers.

   To use in VS Code:
   1. Open the `.http` file you want to test (e.g., `Test/endpoints.http`).
   2. Click the `Send Request` link above each request (requires the REST Client extension).

4. **Access the API documentation:**

   Open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser.

5. **View application logs:**

   ```sh
   make logs
   ```

6. **Stop and remove the containers:**

   ```sh
   make down
   ```

---

- The API will be available at `http://localhost:8000`.
- The database will persist data in a Docker volume named `pgdata`.
- The `DATABASE_URL` is set automatically for the API service in `docker-compose.yml`.
