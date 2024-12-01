# -ue19-lab-05
1. Run the script:
   ```bash
   python app.py
   ```

   This will fetch and print a random joke.

## Docker Instructions

1. Build the Docker image:
   ```bash
   docker build -t joke-fetcher .
   ```

2. Run the Docker container:
   ```bash
   docker run --rm joke-fetcher
   ```

## Files in the Repository

- **app.py**: The main script to fetch and display jokes.
- **requirements.txt**: Lists the Python dependencies.
- **Dockerfile**: Defines the container environment for the application.
- **README.md**: Instructions on installation, usage, and setup.

Enjoy your jokes!
