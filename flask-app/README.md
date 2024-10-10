# Creating a small Flask app and running it in a container together with a MongoDB container

## Steps:

### 1. Create a virtual environment
```
python -m venv flask-env
```

### 2. Activate the environment
```
.\flask-env\Scripts\activate
```

### 3. Run your containers
```
docker-compose up --build    
```

### 4. Test your webpage in the browser
```
Go to the address provided in the terminal
```
```
Enter and sumbit some data
```

### 5. Check your database
```
docker exec -it mongo_db bash
```
```
mongosh
```
```
show dbs
```
```
use user_profiles
```
```
show collections
```
```
db.profiles.find()
```