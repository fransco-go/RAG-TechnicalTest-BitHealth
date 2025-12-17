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
```md
### Design Decisions
I refactored the original single-file implementation into clearly separated layers: API (FastAPI routing), services (embedding, storage, and workflow), and application bootstrap. Each responsibility is encapsulated in its own class, making dependencies explicit through constructor injection rather than global state.

### Trade-off Considered
To keep behavior identical, I retained the simplistic ID generation and fake embedding logic, even though they are not production-safe. Improving these would enhance robustness but would change the scope of the exercise.

### Maintainability Improvements
This structure improves readability, testability, and extensibility. Each service can now be unit-tested in isolation, alternative implementations (e.g., real embeddings or different vector stores) can be swapped easily, and the API layer remains thin and focused solely on HTTP concerns.