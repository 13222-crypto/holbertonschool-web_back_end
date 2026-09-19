# NoSQL - MongoDB

This project covers the fundamentals of NoSQL databases with a primary focus on MongoDB and Python integration using PyMongo. It addresses database creation, CRUD operations, aggregation pipelines, and Python database scripting.

## Learning Objectives

By the end of this project, you should be able to explain:
* What NoSQL means and how it differs from relational (SQL) databases
* What ACID properties are and how they apply in database management
* The concept of document-oriented storage
* The main types of NoSQL databases (Document, Key-Value, Columnar, Graph)
* The benefits of using a NoSQL database
* How to query, insert, update, and delete documents in MongoDB
* How to interact with MongoDB using PyMongo in Python 3.9

## Requirements

### MongoDB Command Files
* Environment: Ubuntu 20.04 LTS running MongoDB version 4.4
* All command files must end with a new line
* The first line of every command file must be a comment starting with `//`
* File length will be verified using `wc`

### Python Scripts
* Environment: Ubuntu 20.04 LTS running Python 3.9 and PyMongo version 4.8.0
* Code style: Mandatory adherence to `pycodestyle` (version 2.5.*)
* File structure:
  * First line: `#!/usr/bin/env python3`
  * All files must end with a new line
  * Modules and functions must include full documentation string (`__doc__`)
  * Code must not execute when imported (`if __name__ == "__main__":`)

## Directory Structure

| File | Description |
| :--- | :--- |
| `0-list_databases` | MongoDB script that lists all databases |
| `1-use_or_create_db` | MongoDB script that creates or switches to a database |
| `2-insert` | MongoDB script that inserts a document into a collection |
| `3-all` | MongoDB script that lists all documents in a collection |
| `4-match_all` | MongoDB script that matches all documents with specific attributes |
| `5-count` | MongoDB script that counts the total number of documents in a collection |
| `6-update` | MongoDB script that updates specified documents in a collection |
| `7-delete` | MongoDB script that deletes specified documents from a collection |
| `8-all.py` | Python function that lists all documents in a collection |
| `9-insert_school.py` | Python function that inserts a new document in a collection based on kwargs |
| `10-update_topics.py` | Python function that changes all topics of a school document based on the name |
| `11-schools_by_topic.py` | Python function that returns the list of school having a specific topic |
| `12-log_stats.py` | Python script that provides stats about Nginx logs stored in MongoDB |

## Installation & Setup (MongoDB 4.4 on Ubuntu)

To run local tests, start the MongoDB daemon:

```bash
sudo mkdir -p /var/lib/mongodb /var/log/mongodb
sudo chown -R mongodb:mongodb /var/lib/mongodb /var/log/mongodb
sudo -u mongodb /usr/bin/mongod --config /etc/mongod.conf &
