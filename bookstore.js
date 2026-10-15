db = db.getSiblingDB("bookstore")

db.authors.drop()
var authors = JSON.parse(fs.readFileSync("authors.json", "utf8"))
db.authors.insertMany(authors)

db.books.drop()
var books = JSON.parse(fs.readFileSync("books.json", "utf8"))
db.books.insertMany(books)

db.authors.find()
db.books.find()

db.books.insertMany([
  {title: "Holes", published_year: 1998, author_ids: ["author_004"]},
  {title: "The Age of Innocence", published_year: 1920, author_ids: ["author_005"]}])

db.authors.insertMany([
  {_id: "author_004", name: "Louis Sachar",nationality: "American", bio: {short: "American author of children's books.",long: "Louis Sachar is an American author best known for writing Holes."}},
  {_id: "author_005",name: "Edith Wharton",nationality: "American", bio: {short: "American novelist.", long: "Edith Wharton was an American novelist known for writing The Age of Innocence."}}])

db.books.find({ author_ids: { $in: ["author_001", "author_004"] } })
