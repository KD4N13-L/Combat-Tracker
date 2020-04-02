import json
book ={
    "content": {"headings": ["Synopsis", {"Book Five": ["Minas Tirith", "The Passing of the Grey Company", "The Muster of Rohan",
                                                        "The Siege of Gondor", "The Ride of the Rohirrim", "The Battle of the Pelennor Fields",
                                                        "The Pyre of Denethor", "The Houses of Healing", "The Last Debate", "The Black Gate Opens"],
                                          "Book Six": ["The Tower of Cirith Ungol", "The Land of Shadow", "Mount Doom", "The Field of Cormallen",
                                                       "The Steward adn the King", "Many Partings", "Homeward Bound", "The Scouring of the Shire",
                                                       "The Grey Heavens"]
                                          }
                             ]
                },
    "pages": 998,
    "author": "J.R.R. Tolkien",
    "publishing_date": 1994
}

with open ("book.json", "w") as f:
    json.dump(book, f, indent=2)

with open ("book.json", "r") as f:
    book_info = json.load(f)

print(book_info)