class Article:
    all = []  # Created a list to store all articles

    def __init__(self, author, magazine, title):
        # Validated the title length (between 5 and 50 characters)
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Invalid Title")
        
        # Assigned instance variables
        self._title = title  # Set the article's title
        self._author = author  # Set the article's author
        self._magazine = magazine  # Set the article's magazine
        Article.all.append(self)  # Added  article to the global list of articles
        
        magazine.add_articles(self)  # Added  article to the magazine's list of articles
        author._articles_list.append(self)  # Added article to the author's list of articles

    @property
    def title(self):
        return self._title  # Return the article's title

    @property
    def author(self):
        return self._author  # Return the article's author

    @author.setter
    def author(self, new_author):
        #  new author is a valid instance of Author class
        if not isinstance(new_author, Author):
            raise ValueError("Author must be an instance of the Author class")
        self._author = new_author  # Set the new author for the article

    @property
    def magazine(self):
        return self._magazine  # Returned the magazine associated with the article

    @magazine.setter
    def magazine(self, new_magazine):
        # new magazine is a valid instance of Magazine class
        if not isinstance(new_magazine, Magazine):
            raise ValueError("Magazine must be an instance of the Magazine class")
        self._magazine = new_magazine  # Set the new magazine for the article


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a string")
        self._name = name  # Set the author's name
        self._articles_list = []  # Initialize an empty list to store the articles written by this author

    @property
    def name(self):
        return self._name  # Returned the author's name

    def articles(self):
        return self._articles_list  # Returned the list of articles written by the author

    def magazines(self):
        # Get all unique magazines the author has written for
        return list(set(article.magazine for article in self._articles_list))

    def add_article(self, magazine, title):
        #create and return a new article
        article = Article(self, magazine, title)
        self._articles_list.append(article)
        return article

    def topic_areas(self):
        # Get the unique categories of magazines the author has written 
        return list(set(article.magazine.category for article in self._articles_list))


class Magazine:
    def __init__(self, name, category):
        # Validate the magazine's name (should be between 2 and 16 characters)
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters")
        self._name = name  # Set the magazine's name
        self._category = category  # Set the magazine's category
        self._articles_list = []  # Initialize an empty list to store the magazine's articles

    @property
    def name(self):
        return self._name  # Returned the magazine's name

    @name.setter
    def name(self, new_name):
        # Validate the magazine's new name (must be between 2 and 16 characters)
        if not isinstance(new_name, str) or len(new_name) <= 2 or len(new_name) >= 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters")
        self._name = new_name  # Set the magazine's new name

    @property
    def category(self):
        return self._category  # Return the magazine's category

    @category.setter
    def category(self, new_category):
        # Ensure the new category is a valid non-empty string
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = new_category  # Set the new category for the magazine

    def add_articles(self, article):
        # Add an article to the magazine's list of articles
        self._articles_list.append(article)

    def articles(self):
        return self._articles_list  # Return the list of articles in the magazine

    def contributors(self):
        # Get the unique authors who have contributed to the magazine
        return list(set(article.author for article in self._articles_list))

    def article_titles(self):
        # Return a list of article titles in the magazine
        return [article.title for article in self._articles_list]

    def contributing_authors(self):
        # Return authors who have written more than 2 articles for the magazine
        return [author for author in self.contributors() if len([a for a in self._articles_list if a.author == author]) > 2]


# Create authors and magazines
author_1 = Author("Carry Bradshaw")
author_2 = Author("Nathaniel Hawthorne")
magazine_1 = Magazine("Vogue", "Fashion")
magazine_2 = Magazine("AD", "Architecture")

# Create articles for the authors and magazines
Article(author_1, magazine_1, "How to wear a tutu with style")
Article(author_1, magazine_1, "How to be single and happy")
Article(author_1, magazine_1, "Dating life in NYC")
Article(author_1, magazine_2, "Carrara Marble is so 2020")
Article(author_2, magazine_2, "2023 Eccentric Design Trends")

# Output the relationships between authors and magazines
print(f"Author {author_1.name} articles: {[article.title for article in author_1.articles()]}")
print(f"Author {author_1.name} magazines: {[magazine.name for magazine in author_1.magazines()]}")
print(f"Magazine {magazine_1.name} contributors: {[author.name for author in magazine_1.contributors()]}")
print(f"Magazine {magazine_2.name} articles: {[article.title for article in magazine_2.articles()]}")
print(f"Magazine {magazine_2.name} contributing authors: {[author.name for author in magazine_2.contributing_authors()]}")
