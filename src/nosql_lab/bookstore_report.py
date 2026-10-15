import os
import logging
from pymongo import MongoClient

MONGODB_ATLAS_URL = os.getenv("MONGODB_ATLAS_URL")
MONGODB_ATLAS_USER = os.getenv("MONGODB_ATLAS_USER")
MONGODB_ATLAS_PWD = os.getenv("MONGODB_ATLAS_PWD")

logging.basicConfig(level=logging.INFO)


def main():
    """Connect to MongoDB Atlas and print a bookstore report."""

    client = None

    try:
        client = MongoClient(
            MONGODB_ATLAS_URL,
            username=MONGODB_ATLAS_USER,
            password=MONGODB_ATLAS_PWD
        )

        client.admin.command("ping")
        logging.info("Connected to MongoDB Atlas")








        db = client["bookstore"]
        authors = db["authors"]
        books = db["books"]

    
        author_ids = ["author_001", "author_004", "author_005"]

        
        total = authors.count_documents({"_id": {"$in": author_ids}})
        print(f"Authors: {total}\n")

        
        for author in authors.find({"_id": {"$in": author_ids}}):
            print(author["name"])

            for book in books.find({"author_ids": author["_id"]}):
                print(f'  {book["title"]} ({book["published_year"]})')

            print()

    except Exception as error:
        logging.error("Error: %s", error)

    finally:
        if client is not None:
            client.close()


if __name__ == "__main__":
    main()
