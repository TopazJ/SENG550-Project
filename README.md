# SENG 550 final project

## Details about the included files

The Python and Bash script files in the Data Retrieval folder were used to pull the dataset required from the selected APIs and store it in the centralized MongoDB database instance.

Once the data retrieval is complete, a the Docker Compose file is used for setting up a local environment to process and run the machine learning model on the data.

## Instructions for running the notebook

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop).
2. Start the local containers.
   ```
   sudo docker-compose up
   ```
3. In a new terminal, load the remote data.
   ```
   sudo docker-compose exec mongo bash -c "mongodump --uri mongodb+srv://[username]:[password]@[database address]/[table name]"
   sudo docker-compose exec mongo bash -c "mongorestore"
   ```
    - Replace `[username]`, `[password]`, `[database address]`, and `[table name]` with the remote database credentials.
4. Navigate to http://localhost:22085/notebooks/work/notebook.ipynb.
5. Run the notebook.
