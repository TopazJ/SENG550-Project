# SENG 550 final project

## Instructions

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop).
2. Start the local containers.
   ```
   docker-compose up
   ```
3. In a new terminal, load the remote data.
   ```
   docker-compose exec mongo bash -c "mongodump --uri mongodb+srv://[username]:[password]@seng550.i7xxz.mongodb.net/seng550"
   docker-compose exec mongo bash -c "mongorestore"
   ```
    - Replace `[username]` and `[password]` with the remote database credentials.
4. Navigate to http://localhost:22085/notebooks/work/clean_data.ipynb.
5. Run the notebook.
