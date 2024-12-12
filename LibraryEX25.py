import mysql.connector
#https://github.com/Molapour80/Learning_Python
class Post:
    def __init__(self, id_, title, content, category):
        self.id_ = id_
        self.title = title
        self.content = content
        self.category = category
    
    def __str__(self):
        return f"ID: {self.id_}, Title: {self.title}, Content: {self.content}, Category: {self.category}"

class DB:
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.connection = None 
    
    def connection(self):
        self.connection = mysql.connector.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.database
        )

    def execute_query(self, query, data=None, fetch=False):
        try:
            self.connection()
            cursor = self.connection.cursor() 
            cursor.execute(query, data)
        except Exception as e:
            print(f"Error: {e}")
        else:
            if fetch:
                return cursor.fetchall()
            affected_rows = cursor.rowcount
            self.connection.commit()
            return affected_rows
        finally:
            if self.connection.is_connected():
                cursor.close()
                self.connection.close()

    def add_post(self, post):
        query = "INSERT INTO posts (id, title, content, category) VALUES (%s, %s, %s, %s)"
        data = (post.id_, post.title, post.content, post.category)
        self.execute_query(query, data)

    def remove_post(self, post_id):
        query = "DELETE FROM posts WHERE id = %s"
        data = (post_id,)
        result = self.execute_query(query, data)
        if result:
            print(f"Post with ID {post_id} removed!")
        else:
            print("No record found!")

    def display_posts(self):
        query = "SELECT * FROM posts"
        result = self.execute_query(query, fetch=True)
        if result:
            for row in result:
                print(f"ID: {row[0]}, Title: {row[1]}, Content: {row[2]}, Category: {row[3]}")
        else:
            print("No posts found!")

    def update_post(self, post_id, data_column, name_column):
        query = f"UPDATE posts SET {name_column} = %s WHERE id = %s"
        data = (data_column, post_id)
        result = self.execute_query(query, data)
        if result:
            print(f"Post with ID {post_id} updated!")
        else:
            print("No record found!")

if __name__ == "__main__":
    db = DB("admin", "2001", "localhost", "Library")
    
    
    post1 = Post("1", "Title 1", "Content of the first post", "Category 1")
    db.add_post(post1)
    

    db.display_posts()
    
    
    db.update_post("1", "Updated Title", "title")
    
    db.display_posts()
    
    db.remove_post("1")
   
    db.display_posts()