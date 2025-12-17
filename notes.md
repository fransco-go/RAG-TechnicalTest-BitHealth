### Design Decisions
I refactored the original single-file implementation into **clearly separated layers**:
- **API layer** for HTTP routing (FastAPI)
- **Service layer** for core business logic (embedding, storage, and workflow)
- **Application bootstrap** for wiring dependencies

Each responsibility is encapsulated in its own class. Dependencies are passed explicitly through constructors instead of using global state, which makes the code easier to reason about and modify.

### Trade-off Considered
To preserve the original behavior and keep the scope focused on code quality, I intentionally retained the **fake embedding logic** and **simple document ID generation**. While these parts are not production-ready, improving them would introduce new functionality beyond the intent of the exercise.

### Maintainability Improvements
By separating concerns and removing global state, the code is now easier to read, test, and extend. Individual components can be unit-tested in isolation, implementations can be swapped (for example, real embeddings or a different vector store), and the API layer remains thin and focused only on HTTP request handling.